#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/04'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.27'


import sys
from identity_pc import get_identity_pc
from work_with_config import ConfigIni
from text_hash import GetHash
from exceptions import CantGetIdentityPC, CantGetJsonFromServer
from connect_to_server import srv_request
from getmac import get_mac_address as gma
from add_logon import add_to_registry
from get_update import get_command_stdout
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


def main():
    project_version = __version__
    project_status = __status__

    print(f'Version: {project_version}{ln()}')
    py_logger.info(f'Version: {project_version}')

    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec_command = f'{config.COM_SPEC} cd "{config.SCRIPT_PATH}" && '

    update_status = get_command_stdout(f'{com_spec_command} git pull', config.CMD_DECODE)
    print(f'Update status:\n{update_status}{ln()}')
    py_logger.info(f'Update status: {update_status}')

    if not update_status['ExitCode'] and update_status['StdOut'] != already_updated:
        condition_to_restart = True
        py_logger.info(f'Condition to Restart: {condition_to_restart}')

    if condition_to_restart:
        view_stdout = True
        py_logger.info(f'Launching a new version of the script')
        get_command_stdout(f'{com_spec_command}{config.VENC_ACTIVATE} && python {sys.argv[0]}',
                           config.CMD_DECODE, view_stdout)
        py_logger.info(f'Close old Version: {project_version}')
        exit(f'Close old Version: {project_version}{ln()}')

    # adding to autostart at user login
    add_to_registry()
    py_logger.info(f'Adding to autostart at user login')

    try:
        if project_status == 'Production':
            identity_pc = get_identity_pc()
        else:
            identity_pc = get_identity_pc('TST-01-PC01-Acc')

        py_logger.info(f'{identity_pc}')
    except CantGetIdentityPC:
        py_logger.error('CantGetIdentityPC')
        exit(f'Не удалось получить корректные идентификационные данные ПК')

    print(f'City: {identity_pc.city_abbr}')
    print(f'Shop Number: {identity_pc.shop_number}')
    print(f'HostName: {identity_pc.pc_name}{ln()}')

    hash_hostname = GetHash(identity_pc.pc_name.upper())
    py_logger.info(f'HostName: {identity_pc.pc_name}; Hash HostName: {hash_hostname.MD5}')
    if config.DEBUG:
        print(f'Hash HostName: {hash_hostname.MD5}{ln()}')

    pc_mac_address = gma()
    hash_mac = GetHash(pc_mac_address.upper())
    py_logger.info(f'MAC Address: {pc_mac_address}; Hash MAC Address: {hash_mac.MD5}')
    if config.DEBUG:
        print(f'MAC Address: {pc_mac_address}')
        print(f'Hash MAC Address: {hash_mac.MD5}{ln()}')
        # print(f'Version: {project_version}{ln()}')

    # ini section name
    # ini_section = config.CONFIG_INI_SECTION

    try:
        first_send_data = {
            'city': identity_pc.city_abbr,
            'name': hash_hostname.MD5,
            'mac': hash_mac.MD5,
            'version': project_version,
        }
        first_response_data = srv_request(first_send_data)

        py_logger.info(f'Data sent to the server: {first_send_data}')
        py_logger.debug(f'Server response: {first_response_data}')
    except CantGetJsonFromServer:
        py_logger.error('CantGetJsonFromServer')
        exit(f'Не удалось получить корректные данные от сервера, при запросе данных для: '
             f'{{'
             f'city: {identity_pc.city_abbr}, '
             f'name: {hash_hostname.MD5}, '
             f'mac: {hash_mac.MD5}, '
             f'version: {project_version}, '
             f'}}')

    if config.DEBUG:
        print(f'Request from Server: {first_response_data["DTCLogin"]}{ln()}')

    data_ini_conf = ConfigIni(config.SLSKASSA_CONFIG)
    is_update = data_ini_conf.set_params(config.CONFIG_INI_SECTION, first_response_data)

    py_logger.info(f'Update config: {is_update}')

    if config.DEBUG:
        print(f'Update config: {is_update}{ln()}')

    try:
        second_send_data = {
            'city': identity_pc.city_abbr,
            'name': hash_hostname.MD5,
            'mac': hash_mac.MD5,
            'version': project_version,
            'update': is_update,
        }
        second_response_data = srv_request(second_send_data)

        py_logger.info(f'Data sent to the server: {second_send_data}')
        py_logger.debug(f'Server response: {second_response_data}')
    except CantGetJsonFromServer:
        py_logger.error('CantGetJsonFromServer')
        exit(f'Не удалось получить корректные данные от сервера, при запросе данных для: '
             f'{{'
             f'city: {identity_pc.city_abbr}, '
             f'name: {hash_hostname.MD5}, '
             f'mac: {hash_mac.MD5}, '
             f'version: {project_version}, '
             f'update: {is_update}, '
             f'}}')

    if config.DEBUG:
        py_logger.info(f'Script execution completed!')
        print(f'Script execution completed!{ln()}')


if __name__ == '__main__':
    main()
