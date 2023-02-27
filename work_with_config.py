import configparser
from set_logger_settings import *


py_logger.debug(f"Loading module {__name__}...")


class ConfigIni:
    def __init__(self, cfg_path: str) -> None:
        self._cfg_path = cfg_path
        # обращаемся к конфигу как к обычному словарю!
        self.Config = configparser.ConfigParser()
        # По умолчанию имя преобразуется в нижний регистр, данная настройка оставляет имена как есть
        self.Config.optionxform = lambda option: option

    def get_config(self) -> None:
        self.Config.read(self._cfg_path)

    def set_params(self, section: str, params: dict = {}) -> bool:
        change = False
        self.get_config()
        # self.Config[section] = params
        for key, value in params.items():
            if self.Config.get(section, key) != value:
                self.Config.set(section, key, value)
                change = True

        if change:
            # Сохранияем ini-файл с внесенными изменениями
            with open(self._cfg_path, 'w') as configFile:  # save
                self.Config.write(configFile)

        print(f'Save the config: {change}{ln()}')

        return change


# for test this class:
if __name__ == '__main__':
    conf = 'test/config_test.ini'
    ini_section = 'Kassa'
    test_write_conf = ConfigIni(conf)
    test_write_conf.set_params(ini_section,
                         {
                             'DiscontFindByTel': '1',
                             'DTCUse': '1',
                             'DTCCheck': '1',
                             'DTCDo': '2',
                             'DTCMaxBon': '10 00',
                             'DTCSender': 'BRAVISSIMO'
                         })
    test_read_conf = ConfigIni(conf)
    test_read_conf.get_config()
    for param_key, param_value in test_read_conf.Config[ini_section].items():
        print(f"{param_key}, {param_value}")

