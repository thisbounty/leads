from selenium.webdriver.support.wait import WebDriverWait


def login():
    return {
        'username': '//input[@id="username"]',
        'password': '//input[@id="passwd"]',
        'login_button': '//button[@id="login_btn"]'
    }


def search_results(driver):

    # it is just near after what we are looking for:
    WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_class_name("ProjectTable-description"))
    z = driver.find_elements_by_xpath("//a[contains(@href, 'https://www.freelancer.com/projects/')]")

    return [i.get_property('href') for i in z]
