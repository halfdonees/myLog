import logging

# 如果在main.py中還沒配置'default' logger，會得到一個沒有預設的logger
# 會變成單純的print
logger = logging.getLogger('default')

def foo():
    logger.debug('module debug')
    logger.info('module info')
    logger.warning('module warn')
