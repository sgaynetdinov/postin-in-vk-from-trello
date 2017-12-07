# -*- coding: utf-8 -*-

import os
import configparser

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

try:
    config.read(config_file)
except configparser.ParsingError as e:
    print(e)

TRELLO_KEY = config['TRELLO']['KEY']
TRELLO_TOKEN = config['TRELLO']['TOKEN']
TRELLO_BOARD = config['TRELLO']['BOARD']

VK_ACCESS_TOKEN = config['VK']['ACCESS_TOKEN']
VK_GROUP = config['VK']['GROUP']
