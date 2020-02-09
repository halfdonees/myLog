import logging

logger = logging.getLogger('default')

def foo():
    logger.debug('module debug')
    logger.info('module info')
    logger.warning('module warn')
