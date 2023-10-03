import argparse
import sys
import os
import configparser


class Configuration(object):

    def __init__(self, filename=None):
        if filename is None:
            filename = '../settings.ini'
        config = configparser.SafeConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__)) + '/' + filename)
        if not config.sections():
            print('No file named ' + filename + ' found.')
            print('Copy settings.ini.sample and make changes as appropriate.')
            sys.exit(1)
        config = config._sections
        self.settings = config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Reads an .ini file and returns a dict of the settings.',
        usage='python configuration.py [--file=filename]')
    parser.add_argument('--file',default='settings.ini',help='filename')
    args = parser.parse_args()
    file = args.file