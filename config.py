import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def getConfig():
    return config
