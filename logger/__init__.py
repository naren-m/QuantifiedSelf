import logging
import logging.handlers
import sys
import config as cfg

LOG_FILENAME = 'logs/application.log'
FORMAT = '%(asctime)s-%(levelname).4s-%(funcName)s()-%(filename)s:%(lineno).3d : %(message)s'

var = ('\n'
       'Level   Numeric value\n'
       'CRITICAL    50\n'
       'ERROR   	40\n'
       'WARNING 	30\n'
       'INFO    	20\n'
       'DEBUG   	10\n'
       'NOTSET  	0\n')

logging.basicConfig(filename=LOG_FILENAME,
                    format=FORMAT,
                    level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S')


config = cfg.getConfig()

print_to_screen = config.get('logging', 'print_to_screen')
# Printing to stdout
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter(FORMAT))

app_logger = logging.getLogger(__name__)
app_logger.setLevel(logging.DEBUG)

if print_to_screen == "true":
    app_logger.addHandler(ch)

info = app_logger.info
debug = app_logger.debug
warning = app_logger.warning
error = app_logger.error
critical = app_logger.critical
log = app_logger.log
exception = app_logger.exception
