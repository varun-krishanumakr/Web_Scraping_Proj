from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time
import pyautogui


chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--load-extension=")


# duo_2FA_link = "https://chromewebstore.google.com/detail/auto-2fa/bnfooenhhgcnhdkdjelgmmkpaemlnoek?pli=1"
# # driver = webdriver.Chrome(options = chrome_options)
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = service, options = chrome_options)
# #download the extension and add this device to it
# driver.get(duo_2FA_link)
# time.sleep(2)
# actions = ActionChains(driver)
# add_to_chrome_button = driver.find_element(By.XPATH, '//button[span[contains(text(), "Add to Chrome")]]')

# add_to_chrome_button.click()
# time.sleep(2)
# pyautogui.press('tab', presses = 1)
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(3)
# #now that the extension is downloaded, add this device to it to bypass duo
# duo_device_link = "https://identity.uw.edu/2fa/"
# driver.get(duo_device_link)

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://myplan.uw.edu/audit/#/degree")

# this part finds the "login with UW net ID" button and clicks it
login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "login-netid"))  # Waits for the button to be clickable
     )
login_button.click()

# #on the ensuing page this part enters the login info (for me specifically) and hits enter
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "weblogin_netid"))
)
driver.find_element(By.ID, "weblogin_netid").send_keys("varkrish")
driver.find_element(By.ID, "weblogin_password").send_keys("$00pMonke2246")
driver.find_element(By.ID, "weblogin_password").send_keys(Keys.RETURN)
time.sleep(10)

# #this part is the 2FA request (try and see if you can handle with API)
print("Complete 2FA in the browser...")
not_my_device = WebDriverWait(driver, 30).until(
     EC.presence_of_element_located((By.ID, "dont-trust-browser-button"))
 )
not_my_device.click()

WebDriverWait(driver, 20).until(
    EC.url_contains("https://myplan.uw.edu/audit/#/degree")
)

html = driver.page_source

dars_soup = BeautifulSoup(html, "html.parser")
#now you should be able to do what you want with it

driver.get("https://myplan.uw.edu/plan/#/")
academic_plan_soup = BeautifulSoup(html, "html.parser")

planned_courses = {}
course_urls = {}
#print(soup.prettify())
#go through all of the planned courses and add them and their planned quarters to the planned_courses dictionary
#also add those courses and their respective urls to hte course_urls dictionary

driver.quit()