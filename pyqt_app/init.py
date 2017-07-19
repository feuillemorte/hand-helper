import platform

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
        try:
            with open('configs/config.yml', 'r') as ymlfile:
                config = yaml.load(ymlfile)
        except FileNotFoundError:
            with open('configs/config_default.yml', 'r') as ymlfile:
                config = yaml.load(ymlfile)

        if platform.system().lower() == 'linux':
            config['chromedriver_path'] = config['common']['chromedriver_linux']
        elif platform.system().lower() == 'darwin':
            config['chromedriver_path'] = config['common']['chromedriver_mac']
        elif platform.system().lower() == 'windows':
            config['chromedriver_path'] = config['common']['chromedriver_win']

        return config
