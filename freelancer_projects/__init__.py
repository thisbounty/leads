from selenium.webdriver.support.ui import WebDriverWait


def my_skills(driver):
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath('//link[contains(@href, "https://cdn3.f-cdn.com/css")]'))
    driver.get('https://www.freelancer.com/jobs/myskills/1/')


def parse_search(driver, search_results):    # res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results())

    pass

