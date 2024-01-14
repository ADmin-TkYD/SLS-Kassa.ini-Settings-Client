#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/14'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.37'


import os
from datetime import datetime


max_number_len = 2
date = str(datetime.now().date())
year = datetime.today().year
month = f'{datetime.today().month:0{max_number_len}}'
day = f'{datetime.today().day:0{max_number_len}}'


SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_STATUS = 'Production'

COM_SPEC = f'cmd.exe /c '
VENV_ACTIVATE = r'venv\Scripts\activate'
CMD_DECODE = 'cp866'

DEBUG = None

# info / debug / or empty
LOGGER_LEVEL = 'info'
LOGGER_DIR = f'{SCRIPT_PATH}/Logs/{year}/{month}/{day}'
LOGGER_FILE = f'{LOGGER_DIR}/Logs_{date}'
LOGGER_FORMAT = '%(name)s\t%(asctime)s\t%(levelname)s\t%(message)s'

REGISTRY_PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
REGISTRY_KEY = 'SLS-KassaINI-Updater'

SLSKASSA_EXECUTABLE = 'Kassa_W.exe'

SLSKASSA_CONFIG = r'c:\SoftLand Systems\SLS-Kacca\Kassa_W.INI'
CONFIG_INI_SECTION = 'Kassa'

SERVER_URL = 'http://SLS.TkYD.ru'
SERVER_PORT = 80
SERVER_URI = '/kassa/settings'
