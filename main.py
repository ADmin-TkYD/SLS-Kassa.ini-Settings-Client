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


py_logger.debug(f'Loading module {__name__}...')


def main():
    version = '1.5.18'
    print(f'Version: {version}{ln()}')

    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec = 'cmd.exe /c '
    venv_activate = r'venv\Scripts\activate'
    cmd_decode = 'cp866'

    update_status = get_command_stdout(com_spec + 'git pull', cmd_decode)
    print(f'Update status:\n{update_status}{ln()}')

    if update_status != already_updated:
        condition_to_restart = True

    if condition_to_restart:
        view_stdout = True
        get_command_stdout(f'{com_spec}{venv_activate} && python {sys.argv[0]}', cmd_decode, view_stdout)
        exit(f'Close old Version: {version}{ln()}')

    if DEBUG:
        print(f'{com_spec}{venv_activate} && python {sys.argv[0]}')
        print(f'{com_spec}"{sys.executable}" {sys.argv[0]}{ln()}')

    # adding to autostart at user login
    add_to_registry()

    try:
        identity_pc = get_identity_pc()
        py_logger.debug(f'{identity_pc}')
    except CantGetIdentityPC:
        py_logger.error('CantGetIdentityPC')
        exit(f'Не удалось получить корректные идентификационные данные ПК')

    print(f'City: {identity_pc.city_abbr}')
    print(f'Shop Number: {identity_pc.shop_number}')
    print(f'HostName: {identity_pc.pc_name}{ln()}')

    hash_hostname = GetHash(identity_pc.pc_name.upper())
    if DEBUG:
        print(f'Hash HostName: {hash_hostname.MD5}{ln()}')

    pc_mac_address = gma()
    hash_mac = GetHash(pc_mac_address.upper())
    if DEBUG:
        print(f'MAC Address: {pc_mac_address}')
        print(f'Hash MAC Address: {hash_mac.MD5}{ln()}')
        # print(f'Version: {version}{ln()}')

    # ini section name
    ini_section = 'Kassa'

    try:
        req_data = srv_request(
            {
                'city': identity_pc.city_abbr,
                'name': hash_hostname.MD5,
                'mac': hash_mac.MD5,
                'version': version,
            }
        )
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
        print(f'Request from Server: {req_data["DTCLogin"]}{ln()}')

    data_ini_conf = ConfigIni(config.SLSKASSA_CONFIG)
    is_update = data_ini_conf.set_params(ini_section, req_data)

    if DEBUG:
        print(f'Update config: {is_update}{ln()}')

    try:
        req_data = srv_request(
            {
                'city': identity_pc.city_abbr,
                'name': hash_hostname.MD5,
                'mac': hash_mac.MD5,
                'version': version,
                'update': is_update,
            }
        )
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
        print(f'Script execution completed!{ln()}')


if __name__ == '__main__':
    main()
