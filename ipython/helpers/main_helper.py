# author: Oleg Sushchenko <fmorte@ya.ru>

from selenium.webdriver.common.keys import Keys

from helpers.js_helper import get_domain
from helpers.waiting_helper import wait, wait_clickable
from init import Setup

config = Setup().config
driver = Setup().driver


def find(xpath):
    """Find the element on page and return object of element"""
    wait(xpath)
    wait_clickable(xpath)
    return driver.find_element_by_xpath(xpath)


def send(xpath, text):
    """Send text to field"""
    element = focus_to_element(find(xpath))
    element.clear()
    element.send_keys(text)
    return element


def push_enter_key(element):
    """Push the Enter key"""
    element.send_keys(Keys.RETURN)


def get(url='', domain=None):
    """Go to url"""
    if not domain:
        domain = get_domain()
    driver.get('{}{}'.format(domain, url))
    return driver.current_url


def url():
    """Get current url"""
    return driver.current_url


def is_displayed(xpath):
    """Check element is visible"""
    driver.implicitly_wait(1)
    element = driver.find_elements_by_xpath(xpath)
    driver.implicitly_wait(config['common']['implicitly_wait'])

    return element


def focus_to_element(element):
    """crutch for focus to element"""
    element.send_keys(Keys.NULL)
    return element
