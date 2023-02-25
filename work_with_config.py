import configparser
from set_logger_settings import *


py_logger.debug(f"Loading module {__name__}...")


class config_ini():
    def __init__(self, cfg_path: str) -> None:
        self._cfg_path = cfg_path
        # обращаемся к конфигу как к обычному словарю!
        self.Config = configparser.ConfigParser()
        # По умолчанию имя преобразуется в нижний регистр, данная настройка оставляет имена как есть
        self.Config.optionxform = lambda option: option

    def get_config(self) -> None:
        self.Config.read(self._cfg_path)

    def set_params(self, section: str, params: dict = {}) -> None:
        self.get_config()
        # self.Config[section] = params
        for key, value in params.items():
            self.Config.set(section, key, value)

        # Сохранияем ini-файл с внесенными изменениями
        with open(self._cfg_path, 'w') as configFile:  # save
            self.Config.write(configFile)


# for test this class:
if __name__ == '__main__':
    conf = 'test/config_test.ini'
    ini_section = 'Kassa'
    test_write_conf = config_ini(conf)
    test_write_conf.set_params(ini_section,
                         {
                             'DiscontFindByTel': '1',
                             'DTCUse': '1',
                             'DTCCheck': '1',
                             'DTCDo': '2',
                             'DTCMaxBon': '100',
                             'DTCSender': 'BRAVISSIMO'
                         })
    test_read_conf = config_ini(conf)
    test_read_conf.get_config()
    for param_key, param_value in test_read_conf.Config[ini_section].items():
        print(f"{param_key}, {param_value}")

