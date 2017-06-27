import selenium

from pages import google
from helpers.main_helper import get


def search(pbar, log):
    """Search with google"""
    try:
        pbar.emit(10)
        get()

        pbar.emit(30)
        google.search('Funny cats')

    except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.WebDriverException) as e:
        log.emit('Message: {}.\nPlease, try again or contact to developer'.format(e))


def search_with_query(pbar, log, search_query):
    """Search with google"""
    try:
        pbar.emit(10)
        get()

        pbar.emit(30)
        google.search(search_query)

    except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.WebDriverException) as e:
        log.emit('Message: {}.\nPlease, try again or contact to developer'.format(e))
