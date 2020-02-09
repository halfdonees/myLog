import logging
import time


from myLog import configure_logger
configure_logger(console_level=logging.INFO)

import module


#配置logger，name為預設的'default'

#取得name為'default'的logger
logger = logging.getLogger('default')

logger.debug('main debug')
logger.warning('main warn')
logger.critical('main crit')

module.foo()

for i in range(15):
    logger.warning(i)
    time.sleep(0.5)
