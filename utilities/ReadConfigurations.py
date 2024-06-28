
'''
    config = ConfigParser()
    config.read("directory/config.ini")
    return config.get(section, key)
'''
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
