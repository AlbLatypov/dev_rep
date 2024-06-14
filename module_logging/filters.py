import logging


class InfoLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'INFO'


class DebugWarningLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')


class CriticalLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'CRITICAL'
