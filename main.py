from selenium import webdriver
import time

chrome_driver_path = '/Users/Jope/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')

####### METHOD ONE #######

# data = driver.find_element_by_xpath(xpath='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
#
# scrappy = data.text.split('\n')
#
# for entry in range(0, len(scrappy), 2):
#     key = scrappy[entry]
#     value = scrappy[entry + 1]
#     addition = {key:value}
#
# scrappy_list = [{scrappy[i]: scrappy[i + 1]} for i in range(0, len(scrappy), 2)]
# print(scrappy_list)

####### METHOD TWO #######

time_data = driver.find_elements_by_css_selector('.event-widget time')
name_data = driver.find_elements_by_css_selector('.event-widget li a')
events = {}

for i in range(len(time_data)):
    events[i] = {'time': time_data[i].text, 'name': name_data[i].text}

print(events)

driver.quit()
