# author: Oleg Sushchenko <fmorte@ya.ru>

from pages import google
from helpers.main_helper import get


def search():
    """Search with google"""
    get()

    google.search('Funny cats')


def search_with_query(search_query):
    """Search with google"""
    get()

    google.search(search_query)
