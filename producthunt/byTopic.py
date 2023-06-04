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

url = 'https://www.producthunt.com/topics/artificial-intelligence'
driver.get(url)

# Search Box - need the exact element where you type in the text
# search_box = driver.find_element(By.XPATH, "//input[@name='q']")
# search_box.click()
# sleep(3)
# search_box1 = driver.find_element(By.XPATH, "//input[@class='styles_input__ZOT6E']")
# search_box1.send_keys('curated')
# search_box1.send_keys(Keys.ENTER)
sleep(3)

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

# Initialize lists
product_names_list = []
product_descriptions_list = []
product_links_list = []
num_of_votes_list = []
num_of_followers_list = []
product_categories_list=[]

# fetch product names
product_names = driver.find_elements(By.XPATH, "//div[@data-test='product-item-name']")
for product_name in product_names:
    product_names_list.append(product_name.text)

# Fetch product descriptions
product_descriptions = driver.find_elements(By.XPATH, "//div[contains(@class, 'mb-mobile-0') and contains(@class, 'color-lighter-grey') and contains(@class, 'fontSize-mobile-12') and contains(@class, 'fontWeight-400') and contains(@class, 'noOfLines-2')]")
for product_description in product_descriptions:
    product_descriptions_list.append(product_description.text)

# Fetch product links
elements = driver.find_elements(By.XPATH, "//a[@class='styles_review__CAwcJ']")
for element in elements:
    href_with_reviews = element.get_attribute('href')
    # Remove '/reviews' from the end of the URL
    if href_with_reviews.endswith('/reviews'):
        product_link = href_with_reviews[:-len('/reviews')]
    else:
        product_link = href_with_reviews
    product_links_list.append(product_link)

# Fetch number of reviews
votes = driver.find_elements(By.XPATH, "//div[@class='ml-1 color-lighter-grey fontSize-12 fontWeight-400 noOfLines-undefined']")
for vote in votes :
    num_of_votes_list.append(vote.text)

# Fetch number of follwers
followers = driver.find_elements(By.XPATH, "//div[@class='color-lighter-grey fontSize-12 fontWeight-400 noOfLines-undefined styles_followersCount__3cUpz']")
for follower in followers:
    num_of_followers_list.append(follower.text)

# Fetch product categories
categories = driver.find_elements(By.XPATH, "//div[@class='mr-3 color-lighter-grey fontSize-12 fontWeight-400 noOfLines-undefined']")
for category in categories:
    product_categories_list.append(category.text)

with open('ai_projects.pkl', 'wb') as f:
    pickle.dump((product_names_list, product_descriptions_list, product_links_list,num_of_votes_list,num_of_followers_list,product_categories_list), f)

