from selenium.webdriver.support.ui import WebDriverWait
import requests
import config
import json

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
    with open('url_list.txt', 'r') as url_list:
        rest=config.rest_values()
        print(rest)
        for url in url_list:
            if(len(url)<5):
                continue;
            driver.get(url)
            driver.save_screenshot('job_details.png')
            try:
                WebDriverWait(driver, 15).until(lambda driver: driver.find_elements_by_xpath("//a[contains(@class, 'bidButton')]"))
            except:
                print "Skipped URL: "+url
                driver.save_screenshot(url+'.png')
                continue
            title = driver.find_elements_by_xpath("//h1[@class='project_name largest bold margin-b5 span12']")[0].text
            description = [i.text for i in driver.find_elements_by_xpath("//h2[@class='project-brief-subheading bold margin-b5']/following-sibling::p")][0]
            skills = [i.text for i in driver.find_elements_by_xpath("//a[@class='skills-required']")][0]
            price = driver.find_elements_by_xpath("//div[contains(@class, 'project-budget')]")[0].text
            #tab.append({'title': title, 'description': description, 'url': url.strip(), 'skills': skills})
            job_rest(title, description, skills, url, price, rest['endpoint']+'/leads/')
        return tab

def job_write_file(title, description, skills, url, price, jobs_file=False):
    if(jobs_file == False):
        jobs_file = open('jobs_file.txt', 'w')
    s = price.encode('utf-8').strip()+', '+title.encode('utf-8').strip()+', '+''.join(description).encode('utf-8').strip()+', '+''.join(skills).encode('utf-8').strip()+', '+url.encode('utf-8').strip()+'\n'
    jobs_file.write(s)
    if(jobs_file == False):
        jobs_file.close()

def job_rest(title, description, skills, url, price, endpoint):
    payload = {
        'title': title,
        'description': description,
        'skills': skills,
        'url': url,
        'price': price
    }
    r = requests.post(endpoint, data=payload).text
    print(r)
    r = json.loads(r)
    if(len(r['title']) <= 0):
        raise AssertionError('No success response from REST endpoint. Stopped harvesting under belief results are not recorded')
