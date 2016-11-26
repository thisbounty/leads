from selenium.webdriver.support.ui import WebDriverWait


def my_skills(driver):
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//h3[@class='dashboard-section-heading']"))
    driver.get('https://www.freelancer.com/jobs/myskills/1/')


def parse_search(driver, search_results):    # res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results())
    data = [line.strip() for line in open('url_list.txt', 'r')]
    search_results.extend(data)
    search_results = set(search_results)

    with open('url_list.txt', 'w') as url_list:
        url_list.write('\n'.join(search_results)+'\n')
        #url_list.write("%s\n" % search_results)

    return search_results
