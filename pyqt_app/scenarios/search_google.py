# author: Oleg Sushchenko <fmorte@ya.ru>

from helpers.main_helper import get
from pages import google


def search(pbar):
    """Search with google"""
    pbar.emit(10)
    get()

    pbar.emit(30)
    google.search('Funny cats')


def search_with_query(pbar, search_query):
    """Search with google"""
    pbar.emit(10)
    get()

    pbar.emit(30)
    google.search(search_query)
