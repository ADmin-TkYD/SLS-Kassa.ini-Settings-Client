import sys
import subprocess
from set_logger_settings import *


py_logger.info(f'Loading module {__name__}...')


def get_command_stdout(command: str, stdout_decode: str = 'utf-8', view_stdout: bool = False) -> dict:
    command_result = {}
    py_logger.info(f'Command: {command}; Decode: {stdout_decode}; View: {view_stdout}')
    if DEBUG:
        print(f'Command: {command}{ln()}')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    command_result['StdOut'] = process.stdout.read().decode(stdout_decode).strip()
    command_result['StdErr'] = process.stderr.read().decode(stdout_decode).strip()
    command_result['ExitCode'] = process.returncode

    py_logger.info(f'Command Result: {command_result}')

    if DEBUG or view_stdout:
        print(f'Return:\n{command_result}{ln()}')

    if command_result['ExitCode']:
        py_logger.error(f'Command Result Error:\n{command_result}')
        print(f'Command Result Error:\n{command_result}{ln()}')

    return command_result


# for test:
if __name__ == '__main__':
    condition_to_restart = False
    already_updated = 'Already up to date.'
    com_spec_command = f'{config.COM_SPEC} cd "{config.SCRIPT_PATH}" && '


    if get_command_stdout(com_spec_command + 'git pull', config.CMD_DECODE) != already_updated:
        condition_to_restart = True

    if condition_to_restart:
        get_command_stdout(f'{com_spec_command}{config.VENC_ACTIVATE} && python main.py', config.CMD_DECODE)

    # get_command_stdout(f'{com_spec_command}{config.VENC_ACTIVATE} && python {sys.argv[0]}', config.CMD_DECODE)
    print(f'{com_spec_command}{config.VENC_ACTIVATE} && python {sys.argv[0]}')
