#!/usr/bin/env python3.11

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
    version = '1.5.20'
    print(f'Version: {version}{ln()}')
    py_logger.info(f'Version: {version}')

    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec = f'cmd.exe /c cd "{config.SCRIPT_PATH}" && '
    venv_activate = r'venv\Scripts\activate'
    cmd_decode = 'cp866'

    update_status = get_command_stdout(f'{com_spec} git pull', cmd_decode)
    print(f'Update status:\n{update_status}{ln()}')
    py_logger.info(f'Update status: {update_status}')

    if update_status != already_updated:
        condition_to_restart = True
        py_logger.info(f'Condition to Restart: {condition_to_restart}')

    if condition_to_restart:
        view_stdout = True
        py_logger.info(f'Launching a new version of the script')
        get_command_stdout(f'{com_spec}{venv_activate} && python {sys.argv[0]}', cmd_decode, view_stdout)
        py_logger.info(f'Close old Version: {version}')
        exit(f'Close old Version: {version}{ln()}')

    if DEBUG:
        print(f'{com_spec}{venv_activate} && python {sys.argv[0]}')
        print(f'{com_spec}"{sys.executable}" {sys.argv[0]}{ln()}')

    # adding to autostart at user login
    add_to_registry()
    py_logger.info(f'Adding to autostart at user login')

    try:
        identity_pc = get_identity_pc()
        py_logger.info(f'{identity_pc}')
    except CantGetIdentityPC:
        py_logger.error('CantGetIdentityPC')
        exit(f'Не удалось получить корректные идентификационные данные ПК')

    print(f'City: {identity_pc.city_abbr}')
    print(f'Shop Number: {identity_pc.shop_number}')
    print(f'HostName: {identity_pc.pc_name}{ln()}')

    hash_hostname = GetHash(identity_pc.pc_name.upper())
    py_logger.info(f'HostName: {identity_pc.pc_name}; Hash HostName: {hash_hostname.MD5}')
    if DEBUG:
        print(f'Hash HostName: {hash_hostname.MD5}{ln()}')

    pc_mac_address = gma()
    hash_mac = GetHash(pc_mac_address.upper())
    py_logger.info(f'MAC Address: {pc_mac_address}; Hash MAC Address: {hash_mac.MD5}')
    if DEBUG:
        print(f'MAC Address: {pc_mac_address}')
        print(f'Hash MAC Address: {hash_mac.MD5}{ln()}')
        # print(f'Version: {version}{ln()}')

    # ini section name
    ini_section = 'Kassa'

    try:
        first_send_data = {
                'city': identity_pc.city_abbr,
                'name': hash_hostname.MD5,
                'mac': hash_mac.MD5,
                'version': version,
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
             f'version: {version}, '
             f'}}')

    if DEBUG:
        print(f'Request from Server: {first_response_data["DTCLogin"]}{ln()}')

    data_ini_conf = ConfigIni(config.SLSKASSA_CONFIG)
    is_update = data_ini_conf.set_params(ini_section, first_response_data)

    py_logger.info(f'Update config: {is_update}')

    if DEBUG:
        print(f'Update config: {is_update}{ln()}')

    try:
        second_send_data = {
                'city': identity_pc.city_abbr,
                'name': hash_hostname.MD5,
                'mac': hash_mac.MD5,
                'version': version,
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
             f'version: {version}, '
             f'update: {is_update}, '
             f'}}')

    if DEBUG:
        py_logger.info(f'Script execution completed!')
        print(f'Script execution completed!{ln()}')


if __name__ == '__main__':
    main()
