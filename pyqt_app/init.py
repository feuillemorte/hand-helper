# author: Oleg Sushchenko <fmorte@ya.ru>

import logging
import os
import platform
import sys
import urllib.request
import zipfile
from os import remove
from os.path import isfile

import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Setup(metaclass=Singleton):
    def __init__(self):
        self.config = self.config = self.get_config()
        logging.basicConfig(level=self.config['common']['logging_level'])
        logging.info('Starting... Please, wait.')
        self.driver = None

    def start_browser(self):
        logging.info('Starting browser... Please, wait.')

        self.config['chromedriver_path'] = self.get_chromedriver_path()
        config = self.config

        chrome_options = Options()

        prefs = {'profile.password_manager_enabled': False, 'credentials_enable_service': False}
        chrome_options.add_experimental_option('prefs', prefs)

        browser = webdriver.Chrome(config['chromedriver_path'], chrome_options=chrome_options)
        browser.maximize_window()
        browser.implicitly_wait(config['common']['implicitly_wait'])
        browser.get(config['common']['default_url'])

        self.driver = browser

        return browser

    def get_config(self):
        if isfile(resource_path('config.yml')):
            with open(resource_path('config.yml'), 'r') as ymlfile:
                config = yaml.load(ymlfile)
        else:
            with open(resource_path('config_default.yml'), 'r') as ymlfile:
                config = yaml.load(ymlfile)

        return config

    def get_chromedriver_path(self):
        filename = 'chromedriver'
        os_name = platform.system().lower()
        if os_name == 'linux':
            os_version = 'linux64'
        elif os_name == 'darwin':
            os_version = 'mac64'
        elif os_name == 'windows':
            os_version = 'win32'
            filename = 'chromedriver.exe'

        dir = os.getcwd()
        if not isfile(os.path.join('{}'.format(dir), 'chromedriver', filename)):
            logging.info('Downloading chromedriver... Please, wait.')
            version = requests.request('GET', 'http://chromedriver.storage.googleapis.com/LATEST_RELEASE').json()
            urllib.request.urlretrieve(
                'http://chromedriver.storage.googleapis.com/{}/chromedriver_{}.zip'.format(version, os_version),
                os.path.join('{}'.format(dir), 'chromedriver_{}.zip'.format(os_version)))
            if not isfile(os.path.join('{}'.format(dir), 'chromedriver_{}.zip'.format(os_version))):
                raise Exception('Downloading is failed. Please, check your permissions for executing folder')
            zip_ref = zipfile.ZipFile(os.path.join('{}'.format(dir), 'chromedriver_{}.zip'.format(os_version)), 'r')
            zip_ref.extractall(os.path.join('{}'.format(dir), 'chromedriver'))
            zip_ref.close()
            remove(os.path.join('{}'.format(dir), 'chromedriver_{}.zip'.format(os_version)))
            os.chmod(os.path.join('{}'.format(dir), 'chromedriver'), 0o777)
            os.chmod(os.path.join('{}'.format(dir), 'chromedriver', filename), 0o777)
        return os.path.join('{}'.format(dir), 'chromedriver', filename)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
