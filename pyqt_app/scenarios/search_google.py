# author: Oleg Sushchenko <fmorte@ya.ru>

from helpers.main_helper import get
from pages import google


def search(pbar, log):
    """Search with google"""
    pbar.emit(10)
    get()

    pbar.emit(30)
    google.search('Funny cats')
    log.emit('Finished')


def search_with_query(pbar, log, search_query):
    """Search with google"""
    pbar.emit(10)
    get()

    pbar.emit(30)
    google.search(search_query)
    log.emit('Finished')
