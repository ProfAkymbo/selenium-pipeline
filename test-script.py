#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

# Set up the Chrome browser and options
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-default-apps")
options.add_argument("--disable-infobars")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Set up the Chrome driver
service = Service(r'C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Loop through the tests
for i in range(100):
    # Open the URL
    driver.get("https://www.lambdatest.com/")

    # Wait for the page to load
    time.sleep(2)

    # Click on each header navigation item
    headers = driver.find_elements(By.XPATH, "//header//nav//a")
    for header in headers:
        header.click()
        time.sleep(5)

    # Get the network logs generated on the browser
    logs = driver.execute_script("return window.performance.getEntries();")

    # Save the logs to a file
    with open(f"network_logs_{i}.json", "w") as f:
        json.dump(logs, f)

import os
print(os.getcwd())

# Close the browser
driver.quit()
