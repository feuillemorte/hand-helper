from helpers.main_helper import find, send, push_enter_key
from locators.pages import google_locators


def search(query):
    send(google_locators.search_line, query)

    push_enter_key(find(google_locators.search_line))
