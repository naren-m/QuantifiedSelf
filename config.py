import configparser
import os


def get_config_file():
    proj_root = os.environ['ProjectRoot']
    return proj_root + '/' + 'config.ini'


config = configparser.ConfigParser()
config.read(get_config_file())


def getConfig():
    return config
