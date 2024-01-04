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


import sys
import winreg
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


def add_to_registry() -> None:
    python_path = os.path.abspath(sys.executable)

    # hide mode
    python_path = python_path.replace('python.exe', 'pythonw.exe')

    if config.DEBUG:
        print(f'Python path: {python_path}')
        print(f'Script path: {config.SCRIPT_PATH}{ln()}')

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        config.REGISTRY_PATH,
        0,
        winreg.KEY_SET_VALUE)
    winreg.SetValueEx(
        key,
        config.REGISTRY_KEY,
        0,
        winreg.REG_SZ,
        f'{python_path} "{config.SCRIPT_PATH}'
        r'\main.py"'
    )
    key.Close()
