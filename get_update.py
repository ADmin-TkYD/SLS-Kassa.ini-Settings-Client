import sys
import subprocess
from set_logger_settings import *


py_logger.debug(f'Loading module {__name__}...')


def get_command_stdout(command: str, stdout_decode: str = 'utf-8') -> str:
    if DEBUG:
        print(f'Command: {command}{ln()}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    stdout = process.stdout.read().decode(stdout_decode).strip()
    stderr = process.stderr.read().decode(stdout_decode).strip()
    exitcode = process.returncode

    if not exitcode:
        if DEBUG:
            print(f'StdOut:\n{stdout}{ln()}')

        return stdout
    else:
        exit(f'ExitCode:\n{exitcode}{ln()}StdErr:\n{stderr}{ln()}StdOut:\n{stdout}{ln()}')


# for test:
if __name__ == '__main__':
    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec = 'cmd.exe /c '
    venv_activate = r'venv\Scripts\activate'
    cmd_decode = 'cp866'

    if get_command_stdout(com_spec + 'git pull', cmd_decode) != already_updated:
        condition_to_restart = True

    if condition_to_restart:
        get_command_stdout(f'{com_spec}{venv_activate} && python main.py', cmd_decode)

    # get_command_stdout(f'{com_spec}{venv_activate} && python {sys.argv[0]}', cmd_decode)
    print(f'{com_spec}{venv_activate} && python {sys.argv[0]}')

