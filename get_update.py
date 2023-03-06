import sys
import subprocess
from set_logger_settings import *


py_logger.info(f'Loading module {__name__}...')


def get_command_stdout(command: str, stdout_decode: str = 'utf-8', view_stdout: bool = False) -> str:
    py_logger.info(f'Command: {command}; Decode: {stdout_decode}; View: {view_stdout}')
    if DEBUG:
        print(f'Command: {command}{ln()}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    stdout = process.stdout.read().decode(stdout_decode).strip()
    stderr = process.stderr.read().decode(stdout_decode).strip()
    exitcode = process.returncode

    py_logger.info(f'ExitCode: {exitcode}')
    py_logger.info(f'StdErr: {stderr}')
    py_logger.info(f'StdOut: {stdout}')

    if not exitcode:
        if DEBUG or view_stdout:
            print(f'Return StdOut:\n{stdout}{ln()}')

        return stdout
    else:
        exit(f'ExitCode:\n{exitcode}{ln()}\nStdErr:\n{stderr}{ln()}\nStdOut:\n{stdout}{ln()}')


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

