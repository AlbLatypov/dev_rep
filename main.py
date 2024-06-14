import logging, logging.config
from module_logging import settings

logging.config.dictConfig(settings.logging_config_dict)
logger = logging.getLogger(__name__)

def main():
    print('Первая версия приложения!')
    logger.info(f'Приложение завершено. Продолжение следует...')


if __name__ == '__main__':
    main()
