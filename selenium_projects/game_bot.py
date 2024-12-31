import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

money_str = driver.find_element(By.ID, value= 'money')
money = int(money_str.text.replace(",", ""))
#print(money)

# power_up = driver.find_element(By.CSS_SELECTOR, value=r"#buyAlchemy\ lab > b")
# print(power_up.text)
#
power_ups = [r"#buyTime\ machine > b", "#buyPortal > b", r"#buyAlchemy\ lab > b",
             "#buyShipment > b", "#buyMine > b", "#buyFactory > b",
             "#buyGrandma > b", "#buyCursor > b"]


power_up_cost_list = []
for power in power_ups:
    power_up = driver.find_element(By.CSS_SELECTOR, value=power)
    power_up_cost = int(power_up.text.split("-")[1].strip().replace(",", ""))
    power_up_cost_list.append(power_up_cost)
#print(power_up_cost_list)

power_up_mapping = dict(zip(power_ups, power_up_cost_list))
#print(power_up_mapping)

def look_for_power_up(n):
    x = 1
    global money
    while x < 40:
        time.sleep(n*x)
        for key,value in power_up_mapping.items():
            if money > value:
                try:
                    affordable_power_up = driver.find_element(By.CSS_SELECTOR, value=key)
                    affordable_power_up.click()
                    money -= value
                except:
                    print("Error clicking power-up")
                time.sleep(n)


# Create a new thread for the power-up loop
power_up_thread = threading.Thread(target=look_for_power_up, args=(10,))
power_up_thread.daemon = True  # Set as daemon so it exits when main thread exits

# Start the power-up thread
power_up_thread.start()

# Start the game loop
start_time = time.time()
while time.time() - start_time < 300:  # 300 seconds = 5 minutes
    cookie = driver.find_element(By.ID, value='cookie')
    cookie.click()
    money_str = driver.find_element(By.ID, value= 'money')
    money = int(money_str.text.replace(",", ""))







