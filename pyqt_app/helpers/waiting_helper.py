import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from init import Setup


def wait(xpath, time=10):
    """Awaiting 10 sec till element become clickable"""
    wait = WebDriverWait(Setup().driver, time)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


def wait_ajax():
    """Awaiting ajax"""
    while Setup().driver.execute_script("return jQuery.active") != 0:
        time.sleep(0.5)


def wait_clickable(xpath):
    """Wait for clickable"""
    wait = WebDriverWait(Setup().driver, 10)
    if EC.visibility_of((By.XPATH, xpath)):
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
