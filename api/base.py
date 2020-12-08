import configparser
import os


class Base:

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('{}/config.ini'.format(os.getcwd()))
        return config['DEFAULT']

