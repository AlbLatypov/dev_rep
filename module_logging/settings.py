import sys
from .filters import CriticalLogFilter, InfoLogFilter, DebugWarningLogFilter
# Когда мы указываем . (точку) перед файлом, мы говорим интерпретатору, что файл находится в этой директории.
#.. - когда файл находится в директорией выше.

logging_config_dict = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'info_filter': {
            '()': InfoLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'formatter_1'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_1',
            'filters': ['debug_warning_filter'],
            'stream': sys.stdout
        },
        # 'info_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': '_logging/warnings.log',
        #     'mode': 'w',
        #     'level': 'DEBUG',
        #     'formatter': 'formatter_1',
        #     'filters': ['info_filter']
        # },
        # 'critical_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': '_logging/critical.log',
        #     'mode': 'w',
        #     'formatter': 'formatter_3',
        #     'filters': ['critical_filter']
        # }
    },
    'loggers': {
        # 'censor_lib': {
        #     'level': 'DEBUG',
        #     'handlers': ['info_file']
        # },
        '_pandas.pandas_lib': {
            'level': 'DEBUG',
            'handlers': ['stdout']
        },
        '_requests.get_requests_': {
            'level': 'DEBUG',
            'handlers': ['stdout']
        },
        # 'module_3': {
        #     'handlers': ['stderr', 'critical_file']
        # }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['default']
    }
}
