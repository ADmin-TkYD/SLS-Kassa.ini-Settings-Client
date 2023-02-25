import os
import config


def make_log_dir() -> None:
    if not os.path.exists(config.LOGGER_DIR):
        os.makedirs(config.LOGGER_DIR)
        print(f'Create Dir: {config.LOGGER_DIR}')


# for test this class:
if __name__ == '__main__':
    print(f'{os.path.exists(config.LOGGER_DIR)}')
    print(f'{config.LOGGER_DIR}')
    make_log_dir()
    print(f'{os.path.exists(config.LOGGER_DIR)}')
    print(f'{config.LOGGER_DIR}')
