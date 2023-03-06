# import os
import sys
import winreg
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


def add_to_registry() -> None:
    python_path = os.path.abspath(sys.executable)
    script_path = os.path.dirname(os.path.realpath(__file__))

    # hide mode
    python_path = python_path.replace('python.exe', 'pythonw.exe')

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
        0,
        winreg.KEY_SET_VALUE)
    winreg.SetValueEx(
        key,
        'SLS-KassaINI-Updater',
        0,
        winreg.REG_SZ,
        f'{python_path} "{script_path}'
        r'\main.py"'
    )
    key.Close()
