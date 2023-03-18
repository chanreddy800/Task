from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'/home/chandrakiran/PycharmProjects/pythonProject10/configurations/config.ini')
    return config.get(section, key)