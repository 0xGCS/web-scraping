# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

PATH = '/Users/gregshaheen2/Downloads/chromedriver_mac64'
s = Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get("https://twitter.com/login")

subject = "@0x_cope"

# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("gcs199209")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('3rdjdQkMM.a-2a3v')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
account = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]")
account.click()

sleep(3)
followers = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a")
followers.click()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Initialize List

accounts = driver.find_elements(By.XPATH, '//div[@data-testid="UserCell"]')

account_names_list = []
account_handles_list = []
account_descriptions_list = []

account_names = driver.find_elements(By.XPATH, ".//div[@class='css-901oao r-1awozwy r-18jsvk2 r-6koalj r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0']")
for account_name in account_names:
    account_names_list.append(account_name.text)

account_handles = driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wbh5a2']")
for account_handle in account_handles:
    account_handles_list.append(account_handle.text)

account_descriptions = driver.find_elements(By.XPATH, "//div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-1h8ys4a r-1jeg54m r-qvutc0']")
for account_description in account_descriptions:
    try:
        account_descriptions_list.append(account_description.text)
    except Exception as e:
        print(f"Exception when extracting description: {e}")
        account_descriptions_list.append("")

print("Account names:", account_names_list)
print("Account handles:", account_handles_list)
print("Account descriptions:", account_descriptions_list)

with open('account_data.pkl', 'wb') as f:
    pickle.dump((account_names_list, account_handles_list, account_descriptions_list), f)