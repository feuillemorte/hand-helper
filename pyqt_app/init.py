# author: Oleg Sushchenko <fmorte@ya.ru>

import platform
import stat
import urllib.request
import zipfile
from os import chmod, remove
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
        self.config = self.get_config()
        self.driver = None

    def start_browser(self):
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
        if isfile('configs/config.yml'):
            with open('configs/config.yml', 'r') as ymlfile:
                config = yaml.load(ymlfile)
        else:
            with open('configs/config_default.yml', 'r') as ymlfile:
                config = yaml.load(ymlfile)
        config['chromedriver_path'] = self.get_chromedriver_path()

        return config

    def get_chromedriver_path(self):
        if not isfile('./chromedriver/chromedriver'):
            os_name = platform.system().lower()
            version = requests.request('GET', 'http://chromedriver.storage.googleapis.com/LATEST_RELEASE').json()
            if os_name == 'linux':
                os_version = 'linux64'
            elif os_name == 'darwin':
                os_version = 'mac64'
            elif os_name == 'windows':
                os_version = 'win32'
            urllib.request.urlretrieve(
                f'http://chromedriver.storage.googleapis.com/{version}/chromedriver_{os_version}.zip',
                f'chromedriver_{os_version}.zip')
            zip_ref = zipfile.ZipFile(f'chromedriver_{os_version}.zip', 'r')
            zip_ref.extractall('chromedriver')
            zip_ref.close()
            remove(f'chromedriver_{os_version}.zip')
            chmod('./chromedriver/chromedriver', stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)
        return './chromedriver/chromedriver'
