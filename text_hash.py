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


import hashlib
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


class GetHash:
    def __init__(self, str2hash: str) -> None:
        # str2hash - initializing string
        self.MD5 = ''
        self._set_md5(str2hash)

        py_logger.debug(f'String: {str2hash} => MD5: {self.MD5}')

    def _set_md5(self, str2hash: str) -> None:
        # encoding string using encode()
        # then sending to md5()
        self.MD5 = hashlib.md5(str2hash.encode()).hexdigest()

    def _get_md5(self) -> str:
        return self.MD5


# for test this class:
if __name__ == '__main__':
    print(f'Empty parameter: {GetHash("op, la-lay-la").MD5}')
