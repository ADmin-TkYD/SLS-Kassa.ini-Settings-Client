#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/04'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.28'


import requests
import json
from exceptions import CantGetJsonFromServer
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


def srv_request(payload: dict, headers=None) -> dict:
    if headers is None:
        headers = {'content-type': 'application/json'}
    url = f'{config.SERVER_URL}:{config.SERVER_PORT}{config.SERVER_URI}'
    try:
        response = requests.get(url, params=payload, headers=headers)
    except requests.ConnectionError:
        py_logger.error('ConnectTimeout')
        exit(f'Error: Timed out waiting for a response from the server{ln()}')
    if response.status_code == requests.codes.ok:
        py_logger.info(f'Send payload: {payload}')
        py_logger.debug(f'Server response: {response.text}')
        if config.DEBUG:
            print(f'Send payload: {payload}{ln()}')
            print(f'Server response: {response.text}{ln()}')
        try:
            response = response.json()
        except json.decoder.JSONDecodeError:
            if __name__ == '__main__':
                exit(f'Error: Received data not in JSON format when requested: {payload}')

            py_logger.exception(f'Error: Received data not in JSON format when requested:  {payload}')
            raise CantGetJsonFromServer

        if response['result'].upper() == 'OK':
            py_logger.info(f'JSON: Result: {response["result"]}')
            if config.DEBUG:
                print(f'JSON: Result: {response["result"]}{ln()}')

            return response['data']
        else:
            if __name__ == '__main__':
                exit(f'Error: Server return error: {response["error"]}')

            py_logger.exception(f'Error: Server return error: {response["error"]}')
            raise CantGetJsonFromServer


# for test this class:
if __name__ == '__main__':
    test = {
        'city': 'EKB',
        'name': 'badd1c9b49801ac57e7edc3e0a359a3e',
        'mac': '65336ffbf765ee244fff277a7f6f31be',
        'version': '0.0.0',
        'update': False,
        'test': 'test',
    }
    print(f'JSON: Data: {srv_request(test)}{ln()}')

    test = {
        'city': 'EKB',
        'name': 'badd1c9b49801ac57e7edc3e0a359a3e',
        'mac': '65336ffbf765ee244fff277a7f6f31be',
        'version': '0.0.0',
        'update': True,
        'test': 'test',
    }
    print(f"JSON: Data: {srv_request(test)}{ln()}")

    test = {
        'city': 'EKB',
        'name': 'badd1c9b49801ac57e7edc3e0a359a3e',
        'mac': '65336ffbf765ee244fff277a7f6f31be',
        'version': '0.0.0',
        'test': 'test',
    }
    print(f'JSON: Data: {srv_request(test)}{ln()}')
