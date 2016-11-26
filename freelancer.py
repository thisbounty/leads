#!/usr/bin/python3

from selenium import webdriver
import freelancer_xpaths
import freelancer_login
import freelancer_projects

# Login
driver = webdriver.Firefox()
freelancer_login.user_login(driver, freelancer_xpaths.login())

# go to search results page for projects with my skills
freelancer_projects.my_skills(driver)

# Parse urls from search result and save to file for later bid
res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results(driver))    # TODO: steel don't understand why this way
print(res)


# TODO: and scrape url, title, description, skills
# TODO: then the values that come up in a form when you click place a bid time and amount

