from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


event_schedule = driver.find_elements(By.CSS_SELECTOR, value= '#content > div > section > '
                                                              'div.list-widgets.row > div.medium-widget.event-widget.last > '
                                                              'div > ul > li > time')
event_date = [event.text for event in event_schedule]
print(event_date)

event_description = driver.find_elements(By.CSS_SELECTOR, value= '#content > div > section > '
                                                                 'div.list-widgets.row > div.medium-widget.event-widget.last > '
                                                                 'div > ul > li > a')
event_name = [event.text for event in event_description]
print(event_name)

event_details = {index: {'event_date': l1, 'event_name': l2} for index, (l1, l2) in enumerate(zip(event_date, event_name))}

print(event_details)

driver.quit()
