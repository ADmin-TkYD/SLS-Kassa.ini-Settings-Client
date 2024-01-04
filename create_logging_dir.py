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


import os
import config


def make_log_dir() -> None:
    if not os.path.exists(config.LOGGER_DIR):
        os.makedirs(config.LOGGER_DIR)
        print(f'Create Dir: {config.LOGGER_DIR}')


# for test this class:
if __name__ == '__main__':
    print(f'{os.path.exists(config.LOGGER_DIR)}')
    print(f'{config.LOGGER_DIR}')
    make_log_dir()
    print(f'{os.path.exists(config.LOGGER_DIR)}')
    print(f'{config.LOGGER_DIR}')
