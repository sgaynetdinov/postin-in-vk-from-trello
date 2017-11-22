# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()

try:
    config.read('config.ini')
except configparser.ParsingError as e:
    print(e)

TRELLO_KEY = config['TRELLO']['KEY']
TRELLO_TOKEN = config['TRELLO']['TOKEN']
TRELLO_BOARD = config['TRELLO']['BOARD']
VK_ACCESS_TOKEN = config['VK']['ACCESS_TOKEN']
VK_GROUP = config['VK']['GROUP']
