from selenium.webdriver.support.ui import WebDriverWait


def my_skills(driver):
    print('my skills')
    driver.save_screenshot('screen.png')
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//h3[@class='dashboard-section-heading']"))
    driver.get('https://www.freelancer.com/jobs/myskills/1/')


def parse_search(driver, search_results):    # res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results())
    print('parse results')
    data = [line.strip() for line in open('url_list.txt', 'r')]
    search_results.extend(data)
    search_results = set(search_results)

    with open('url_list.txt', 'w') as url_list:
        url_list.write('\n'.join(search_results)+'\n')
        #url_list.write("%s\n" % search_results)

    return search_results


def job_details(driver):
    print('job details')
    tab = []
    jobs_file = open('jobs_file.txt', 'w')
    with open('url_list.txt', 'r') as url_list:
        for url in url_list:
            driver.get(url)
            driver.save_screenshot('job_details.png')
            try:
                WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath("//a[contains(@class, 'bidButton')]"))
            except:
                print "Skipped URL: "+url
                driver.save_screenshot(url+'.png')
                continue
            title = driver.find_elements_by_xpath("//h1[@class='project_name largest bold margin-b5 span12']")[0].text
            description = [i.text for i in driver.find_elements_by_xpath("//h2[@class='project-brief-subheading bold margin-b5']/following-sibling::p")]
            skills = [i.text for i in driver.find_elements_by_xpath("//a[@class='skills-required']")]
            #tab.append({'title': title, 'description': description, 'url': url.strip(), 'skills': skills})
            s = title+', '+''.join(description)+', '+''.join(skills)+', '+url+'\n'
            jobs_file.write(s)

        jobs_file.close()
        return tab

def job_write_file(title, description, skills, url, jobs_file=False):
    if(jobs_file == False):
        jobs_file = open('jobs_file.txt', 'w')
    s = title+', '+''.join(description)+', '+''.join(skills)+', '+url+'\n'
    jobs_file.write(s)
    if(jobs_file == False):
        jobs_file.close()
