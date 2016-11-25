from bs4 import BeautifulSoup
import requests


def login():
    return {
        'username': '//input[@id="username"]',
        'password': '//input[@id="passwd"]',
        'login_button': '//button[@id="login_btn"]'
    }

# TODO why?
def search_results():   # res = freelancer_projects.parse_search(driver, freelancer_xpaths.search_results())
    html = requests.get('https://www.freelancer.com/jobs/myskills/1/')
    print(html)
    soup = BeautifulSoup(html.content, "html.parser")
    print(soup.find_all('span class="ProjectTable-titleIcon is-ProjectTable-titleIcon-project"'))
    return True






'''

<span class="ProjectTable-titleIcon is-ProjectTable-titleIcon-project">
<a href="https://www.freelancer.com/projects/php/WHM-Cpanel-dns-setting-domain/">WHM / Cpanel and dns setting to domain name with team viewer </a>

<p class="ProjectTable-description">I need someone who can set up my VP hosting on whm/cpanel and the dns . You need to do my project with team viewer. https://www.1and1.com/vps-hosting </p>

<span class="ProjectTable-skills">
<a class="hiddenlink" href="https://www.freelancer.com/jobs/php/">PHP</a>
,
<a class="hiddenlink" href="https://www.freelancer.com/jobs/Linux/">Linux</a>
,
<a class="hiddenlink" href="https://www.freelancer.com/jobs/html/">HTML</a>
,
<a class="hiddenlink" href="https://www.freelancer.com/jobs/web-hosting/">Web Hosting</a>
,
<a class="hiddenlink" href="https://www.freelancer.com/jobs/whmcs/">WHMCS</a>

'''
