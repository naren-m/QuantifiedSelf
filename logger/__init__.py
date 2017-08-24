import logging
import logging.handlers
import sys
import config as cfg
import os


def get_log_file():
    proj_root = os.environ['ProjectRoot']
    config = cfg.getConfig()

    log_file = proj_root + "/" + config.get('logging', 'log_file')

    if not os.path.exists(log_file):
        with open(log_file, 'wb') as f:
            f.write('')

    return log_file


def get_log_level():
    config = cfg.getConfig()
    log_level = config.get('logging', 'log_level')

    if log_level == 'debug':
        level = logging.DEBUG
    elif log_level == 'info':
        level = logging.INFO

    return level


def get_format():
    return "%(asctime)s-%(levelname).4s-%(funcName)s()-%(filename)s:%(lineno).3d : %(message)s"


def get_app_logger():
    logging.basicConfig(filename=get_log_file(),
                        format=get_format(),
                        level=get_log_level(),
                        datefmt='%m/%d/%Y %I:%M:%S')

    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(get_log_level())
    return app_logger


def log_on_screen(app_logger):
    config = cfg.getConfig()
    print_to_screen = config.get('logging', 'print_to_screen')
    # Printing to stdout
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(get_log_level())
    ch.setFormatter(logging.Formatter(get_format()))
    if print_to_screen == "true":
        app_logger.addHandler(ch)


APP_LOGGER = get_app_logger()

# Printing to stdout
log_on_screen(APP_LOGGER)

info = APP_LOGGER.info
debug = APP_LOGGER.debug
warning = APP_LOGGER.warning
error = APP_LOGGER.error
critical = APP_LOGGER.critical
log = APP_LOGGER.log
exception = APP_LOGGER.exception
