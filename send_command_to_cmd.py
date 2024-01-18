#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/04'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.38'


import sys
import subprocess
from set_logger_settings import *


py_logger.info(f'Loading module {__name__}...')


# get the result of a command from stdout
def send_cmd_command(command: str, stdout_decode: str = 'utf-8') -> dict:
    command_result = {}
    py_logger.info(f'Command: {command}; Decode: {stdout_decode}')
    if config.DEBUG:
        print(f'Command: {command}{ln()}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    command_result['StdOut'] = process.stdout.read().decode(stdout_decode).strip()
    command_result['StdErr'] = process.stderr.read().decode(stdout_decode).strip()
    command_result['ExitCode'] = process.returncode

    py_logger.info(f'Command Result: {command_result}')

    if config.DEBUG:
        print(f'Return to DEBUG:\n{command_result}{ln()}')

    if command_result['ExitCode']:
        py_logger.error(f'Command Exit Code:\n{command_result}')
        print(f'Command Exit Code:\n{command_result["StdErr"]}{ln()}')

    return command_result


# for test:
if __name__ == '__main__':
    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec_command = f'{config.COM_SPEC} cd "{config.SCRIPT_PATH}" && '

    if send_cmd_command(command=com_spec_command + 'git pull', stdout_decode=config.CMD_DECODE) != already_updated:
        condition_to_restart = True

    if condition_to_restart:
        # get_command_stdout(
        #     command=f'{com_spec_command}{config.VENV_ACTIVATE} && python main.py', stdout_decode=config.CMD_DECODE)
        send_cmd_command(command=f'{com_spec_command}{config.VENV_ACTIVATE} && python main.py')

    # get_command_stdout(f'{com_spec_command}{config.VENV_ACTIVATE} && python {sys.argv[0]}', config.CMD_DECODE)
    print(f'{com_spec_command}{config.VENV_ACTIVATE} && python {sys.argv[0]}')
