from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/Users/Jope/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

# data = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# all_portals = driver.find_element_by_link_text('All portals')
# all_portals.click()

# search = driver.find_element_by_name('search')
# search.send_keys('cruton', Keys.RETURN)

driver.find_element_by_name('fName').send_keys('beeop')
driver.find_element_by_name('lName').send_keys('eebop')
driver.find_element_by_name('email').send_keys('peemail@eop.bop')
#driver.find_element_by_tag_name('button').click()
# alternatively, for the above
driver.find_element_by_css_selector('form button').click()
time.sleep(3)

driver.close()