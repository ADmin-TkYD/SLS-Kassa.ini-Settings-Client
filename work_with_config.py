#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/04'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.27'


import configparser
from set_logger_settings import *


py_logger.info(f'Loading module {__name__}...')


class ConfigIni:
    def __init__(self, cfg_path: str) -> None:
        self._cfg_path = cfg_path
        # обращаемся к конфигу как к обычному словарю!
        self.config = configparser.ConfigParser(interpolation=None)
        # По умолчанию имя преобразуется в нижний регистр, данная настройка оставляет имена как есть
        self.config.optionxform = lambda option: option

    def get_config(self) -> None:
        self.config.read(self._cfg_path)

    def set_params(self, section: str, params: dict = None) -> bool:
        change = False
        self.get_config()

        if params is None:
            params = {}

        # self.config[section] = params
        for key, value in params.items():
            if config.DEBUG:
                print(f'{key}: {value}')
            # если ключ не существует или значение ключа не равно новому значению
            if not self.config.has_option(section, key) or self.config.get(section, key) != value:
                self.config.set(section, key, value)
                change = True

        if change:
            # Сохранияем ini-файл с внесенными изменениями
            with open(self._cfg_path, 'w') as config_file:  # save
                self.config.write(config_file)

        print(f'Save the config: {change}{ln()}')

        return change


# for test this class:
if __name__ == '__main__':
    conf = r'test\Kassa_W.ini'
    ini_section = 'Kassa'
    test_conf = ConfigIni(conf)
    test_conf.set_params(
        ini_section,
        {
            'DiscontFindByTel': '1',
            'DTCUse': '1',
            'DTCCheck': '1',
            'DTCDo': '2',
            'DTCMaxBon': '10',
            'DTCSender': 'BRAVISSIMO',
            'DTCPassWord': '1%2345%6'
        }
    )
    '''
    for param_key, param_value in test_conf.config[ini_section].items():
        print(f'{param_key}, {param_value}')
    '''
