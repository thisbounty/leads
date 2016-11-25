import config


def user_login(driver, xpaths):
    conf = config.values()
    driver.get('https://freelancer.com/login')
    driver.set_window_size(1124, 850)

    driver.find_element_by_xpath(xpaths['username']).send_keys(conf['username'])
    driver.find_element_by_xpath(xpaths['password']).send_keys(conf['password'])
    driver.find_element_by_xpath(xpaths['login_button']).click()
