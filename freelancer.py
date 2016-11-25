from selenium import webdriver

import freelancer_xpaths
import freelancer_login
import freelancer_projects

#Login
driver = webdriver.PhantomJS()
freelancer_login.user_login(driver, freelancer_xpaths.login())
#go to search results page for projects with my skills
freelancer_projects.my_skills(driver);
#Parse urls from search result and save to file for later bid
res=freelancer_projects.parse_search(driver, freelancer_xpaths.search_results());
urls=res[0]
with open('urls', 'a') as outfile:
    for url in urls:
        outfile.write("%s\n" % url)
driver.quit()
