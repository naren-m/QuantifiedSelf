import sys
import logger

logger = logger.app_logger

import config


def naren():
    logger.info('Start reading database')
    records = {'john': 55, 'tom': 66}
    logger.debug('Records: %s', records)
    logger.info('Updating records ...')
    logger.warning('warning records ...')
    logger.error('error records ...')
    logger.log(10, 'log records ...')
    logger.exception('exception records ...')


naren()
