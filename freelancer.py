#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import freelancer_xpaths
import freelancer_login
import freelancer_projects

# Login
driver = webdriver.Firefox()
freelancer_login.user_login(driver, freelancer_xpaths.login())

# go to search results page for projects with my skills
freelancer_projects.my_skills(driver)

# Parse urls from search result and save to file for later bid
# res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results())    # TODO: don't understand why this way
# freelancer_xpaths.search_results()
print(driver.title)
print(driver.current_url)
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(@href, 'https://www.freelancer.com/projects/php/')]"))
res1 = driver.find_element_by_xpath("//a[contains(@href, 'https://www.freelancer.com/projects/php/')]")
for i in res1.text:
    print(str(i))

# urls = res[0]
#
# with open('urls', 'a') as outfile:
#     for url in urls:
#         outfile.write("%s\n" % url)
# driver.quit()


def user_login():
    driver = webdriver.Firefox()
    driver.get('https://www.freelancer.com/login')

    emailFieldID = "//input[@id='username']"
    passFieldID = "//input[@id='passwd']"
    loginButtoXpath = '//button[@id="login_btn"]'

    WebDriverWait(driver, 10)
    emailFieldElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
    passFieldElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(passFieldID))
    loginButtonElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(loginButtoXpath))

    emailFieldElement.clear()
    emailFieldElement.send_keys(username)
    passFieldElement.clear()
    passFieldElement.send_keys(password)
    loginButtonElement.click()



# TODO: and scrape url, title, description, skils
# TODO: then the values that come up in a form when you click place a bid time and amount

