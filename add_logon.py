import sys
import winreg
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


def add_to_registry() -> None:
    python_path = os.path.abspath(sys.executable)

    # hide mode
    python_path = python_path.replace('python.exe', 'pythonw.exe')

    if DEBUG:
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
