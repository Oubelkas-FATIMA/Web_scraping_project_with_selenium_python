#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


# creating a file where data will be stored
with open('job_scraping_multipe_pages.csv', 'w') as file:
    file.write("Job_title; Location; Salary; Contract_type; Job_description \n")
    
    

driver=webdriver.Chrome(executable_path='C:\\Users\\oubelkas fatima\\Documents\\chromeDriverSelenium\\chromedriver.exe')

# here is the site i will be using to scrape my data
driver.get('https://www.jobsite.co.uk/')



# adding a chrome options
chrome_options = webdriver.ChromeOptions()

    
# !!! blocking browser notifications !!!
prefs = {"profile.default_content_setting_values.notifications" : 2} 
chrome_options.add_experimental_option("prefs", prefs)

# maximizing windows
driver.maximize_window()
time.sleep(1)


# this handle notifocation of cockies we will just accept if it appears
cookie= driver.find_element_by_xpath("//div[@id='ccmgt_explicit_accept']")
try:
    cookie.click()
except:
    pass 


# entering necessarly infos to go on with scraping
job_title=driver.find_element_by_id('keywords')
job_title.click()
job_title.send_keys('Software Engineer')
time.sleep(1)

location=driver.find_element_by_id('location')
location.click()
location.send_keys('Manchester')
time.sleep(1)

dropdown=driver.find_element_by_id('Radius')
radius=Select(dropdown)
radius.select_by_visible_text('30 miles')
time.sleep(1)

search=driver.find_element_by_xpath('//input[@value="Search"]')
search.click()
time.sleep(2)

for k in range(3):
    titles=driver.find_elements_by_xpath('//div[@class="sc-fzooss kBgtGS"]/a/h2') 
    location=driver.find_elements_by_xpath('//li[@class="job-item-location"]/span')
    salary=driver.find_elements_by_xpath('//d1[@class="sc-fzoJMP jpodhy"]/span')
    contract_type=driver.find_elements_by_xpath('//li[@class="job-type"]/span')
    job_details=driver.find_elements_by_xpath('//div[@class="sc-fzoYkl kSkZOQ"]/a/span')

    with open('job_scraping_multipe_pages.csv', 'a') as file:
        for i in range(len(titles)):
            file.write(titles[i].text + ";" + location[i].text + ";" + salary[i].text + ";" + contract_type[i].text + ";"+
                      job_details[i].text + "\n")

        next=driver.find_element_by_xpath('//a[@class="PaginationArrowLink-sc-imp866-0 crGtvH"]/span')
        next.click()
    file.close()
driver.close()