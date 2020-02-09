import logging
import logging.config
import os

def configure_logger(name='default',
                     log_path=None,
                     console_level=logging.WARN,
                     file_level=logging.DEBUG):
    '''配置logger
    brief:
        配置一個自定義的logger，包含一個FileHandler以及一個ConsoleHandler.

    args:
        name: (str) logger name, default='default'
        log_path: (str) path where logfile save at. Save in <name>.log if this argument isn't set.
        console_level: (int) StreamHandler level.
        file_level: (int) FileHandler level.

    output:
        None
    '''

    if not log_path:
        log_path = name + '.log'


    logging.config.dictConfig({
        'version':1,
        'formatters':{
            'basic':{
                'format': '%(asctime)s - %(levelname)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'advance':{
                'format': '%(asctime)s - << %(levelname)s >> - %(message)s %(filename)s: line %(lineno)d in function %(funcName)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers':{
            'console':{
                'level': console_level,
                'class': 'logging.StreamHandler',
                'formatter': 'basic',
                'stream': 'ext://sys.stdout'
            },
            'file':{
                'level': file_level,
                'class': 'logging.FileHandler',
                'formatter': 'advance',
                'filename': log_path,
            }
        },
        'loggers':{
            name:{
                'level': 'DEBUG',
                'handlers' :['console', 'file']
            }
        },
        'disable_exiting_loggers': False 
    })

if __name__ == '__main__':
    alog = configure_logger('default', 'log123.log')
    alog.debug('debug message')
    alog.warning('warn msg')
    alog.critical('crit msg')
