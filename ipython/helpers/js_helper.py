# author: Oleg Sushchenko <fmorte@ya.ru>

from init import Setup

driver = Setup().driver


def get_domain():
    """Get protocol from config and domain and return url
    """
    return driver.execute_script('return location.protocol') + '//' + driver.execute_script('return location.hostname') + '/'
