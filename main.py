#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/19'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.41'


import sys
import time
from identity_pc import get_identity_pc
from work_with_config import ConfigIni
from text_hash import GetHash
from exceptions import CantGetIdentityPC, CantGetJsonFromServer
from connect_to_server import srv_request
from getmac import get_mac_address as gma
from add_logon import add_to_registry
from send_command_to_cmd import send_cmd_command
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

    update_status = []
    resolve_host = False
    attempt = 10

    while not resolve_host:
        update_status = send_cmd_command(
            command=f'{com_spec_command} git pull',
            stdout_decode=config.CMD_DECODE
        )
        py_logger.info(f'Update status: {update_status}')

        print(f'Update status:\n{update_status["StdOut"]}{ln()}')
        if config.DEBUG:
            print(f'Update status:\n{update_status["StdErr"]}{ln()}')

        if (
                update_status['StdErr'].find("fatal") < 0 or not attempt
        ):
            resolve_host = True
        else:
            print(f'Wait, could not resolve host, attempt: {attempt}')
            attempt += -1
            time.sleep(10)

    if not update_status['ExitCode'] and update_status['StdOut'] != already_updated:
        condition_to_restart = True
        py_logger.info(f'Condition to Restart: {condition_to_restart}')

    if condition_to_restart:
        view_stdout = True
        py_logger.info(f'Launching a new version of the script')
        send_cmd_command(
            command=f'{com_spec_command}{config.VENV_ACTIVATE} && python {sys.argv[0]}',
            stdout_decode=config.CMD_DECODE
        )
        py_logger.info(f'Close old Version: {project_version}')
        exit(f'Close old Version: {project_version}{ln()}')

    # adding to autostart at user login
    add_to_registry()
    py_logger.info(f'Adding to autostart at user login')

    try:
        if project_status == config.SCRIPT_STATUS:
            identity_pc = get_identity_pc()
        else:
            identity_pc = get_identity_pc('TST-01-PC01-Tst')

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

    send_data = {
        'city': identity_pc.city_abbr,
        'shop_number': identity_pc.shop_number,
        'pc_number': identity_pc.pc_number,
        'pc_type': identity_pc.pc_type,
        'department_abbr': identity_pc.department_abbr,
        'name': hash_hostname.MD5,
        'mac': hash_mac.MD5,
        'version': project_version,
        'update': None,
    }
    if config.DEBUG:
        print(f'{config.SERVER_URL}: {config.SERVER_PORT}{config.SERVER_URI}{send_data}{ln()}')

    for num in range(2):
        # print(f'{num}: {send_data["update"]}{ln()}')
        try:
            response_data = srv_request(send_data)

            py_logger.info(f'Data sent to the server: {send_data}')
            py_logger.debug(f'Server response: {response_data}')

        except CantGetJsonFromServer:
            py_logger.error('CantGetJsonFromServer')
            exit(f'Не удалось получить корректные данные от сервера, при запросе данных для: '
                 f'{{'
                 f'city: {send_data["city"]}, '
                 f'name: {send_data["name"]}, '
                 f'mac: {send_data["mac"]}, '
                 f'version: {send_data["version"]}, '
                 f'update: {send_data["update"]}, '
                 f'}}')

        if config.DEBUG and response_data:
            print(f'Request from Server: {response_data["DTCLogin"]}{ln()}')

        # If num == 0 (first cycle)
        if not num:
            com_taskkill = f'{config.COM_SPEC} taskkill /f /im {config.SLSKASSA_EXECUTABLE}'
            view_stdout = True

            taskkill_status = send_cmd_command(
                command=f'{com_taskkill}',
                stdout_decode=config.CMD_DECODE
            )

            if not taskkill_status['ExitCode']:
                py_logger.info(f'TaskKill status: {taskkill_status}')
                print(f'TaskKill status:\n{taskkill_status["StdOut"]}{ln()}')

            if config.DEBUG:
                print(f'TaskKill status:\n{taskkill_status["StdErr"]}{ln()}')

            data_ini_conf = ConfigIni(config.SLSKASSA_CONFIG)
            is_update = data_ini_conf.set_params(section=config.CONFIG_INI_SECTION, params=response_data)

            py_logger.info(f'Update config: {is_update}')

            if config.DEBUG:
                print(f'Update config: {is_update}{ln()}')

            send_data['update'] = is_update

        # try:
        #     second_response_data = srv_request(send_data)
        #
        #     py_logger.info(f'Data sent to the server: {send_data}')
        #     py_logger.debug(f'Server response: {second_response_data}')
        # except CantGetJsonFromServer:
        #     py_logger.error('CantGetJsonFromServer')
        #     exit(f'Не удалось получить корректные данные от сервера, при запросе данных для: '
        #          f'{{'
        #          f'city: {send_data["city"]}, '
        #          f'name: {send_data["name"]}, '
        #          f'mac: {send_data["mac"]}, '
        #          f'version: {send_data["version"]}, '
        #          f'update: {send_data["update"]}, '
        #          f'}}')

    if config.DEBUG:
        py_logger.info(f'Script execution completed!')
        print(f'Script execution completed!{ln()}')


if __name__ == '__main__':
    main()
