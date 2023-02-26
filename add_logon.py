import os
import sys
import winreg


def add_to_registry() -> None:
    python_path = os.path.abspath(sys.executable)
    script_path = os.path.dirname(os.path.realpath(__file__))

    # hide mode
    python_path = python_path.replace('python.exe', 'pythonw.exe')

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
        0,
        winreg.KEY_SET_VALUE)
    winreg.SetValueEx(
        key,
        "SLS-KassaINI-Updater",
        0,
        winreg.REG_SZ,
        f'{python_path} "{script_path}\\main.py"')
    key.Close()
