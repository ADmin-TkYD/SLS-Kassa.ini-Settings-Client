import os
import sys
import winreg

python_path = os.path.abspath(sys.executable)
script_path = os.path.dirname(os.path.realpath(__file__))

key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
    0,
    winreg.KEY_SET_VALUE)
winreg.SetValueEx(
    key,
    "SLS-Kassa-INI-Updater",
    0,
    winreg.REG_SZ,
    f'"{python_path}" "{script_path}\\main.py"')
key.Close()

