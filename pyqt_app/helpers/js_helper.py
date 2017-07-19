from init import Setup


def get_domain():
    """Get protocol from config and domain and return url
    """
    return Setup().driver.execute_script('return location.protocol') + '//' + Setup().driver.execute_script('return location.hostname') + '/'
