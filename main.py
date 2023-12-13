from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time

# Create Chromeoptions instance
options = webdriver.ChromeOptions()

# Adding argument to disable the AutomationControlled flag
options.add_argument("--disable-blink-features=AutomationControlled")

# Exclude the collection of enable-automation switches
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
options.add_experimental_option("useAutomationExtension", False)

# Setting the driver path and requesting a page
driver = webdriver.Chrome(options=options)

# Changing the property of the navigator value for webdriver to undefined
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Initializing a list with two Useragents
useragentarray = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
]

for i in range(len(useragentarray)):
    # Setting user agent iteratively as Chrome 108 and 107
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]})
    print(driver.execute_script("return navigator.userAgent;"))
    driver.get("https://www.httpbin.org/headers")

driver.get("https://www.google.com")

# Wait 3.5 on the webpage before trying anything
time.sleep(5)

search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
search_bar.click()

time.sleep(4.5)

search_bar.send_keys("beans")
search_bar.send_keys(Keys.RETURN)  # Simulate hitting the Enter key

# Wait 4.5 seconds before scrolling down 700px
time.sleep(8.2)
driver.execute_script('window.scrollTo(0, 700)')

# Wait for user input (hit Enter to close the browser)
input("Press Enter to close the browser...")

# Close the browser when done
driver.quit()
