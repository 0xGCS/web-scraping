import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

PATH = '/path/to/your/driver'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

url = 'https://fbref.com/en/comps/10/gca/Championship-Stats'
driver.get(url)

sleep(3)

# #expand the table
# expand_button = driver.find_element(By.ID,"stats_standard_control")
# expand_button.click()

# sleep(3)

player_name_list = []
nationality_list = []
position_list = []
player_club_list = []
#league_list = []
age_list = []
sca_list = []
sca90_list = []
gca_list = []
gca90_list = []



#fetch the second table DONE
table2 = driver.find_element(By.ID, 'stats_gca')

#fetch player names DONE
player_names = table2.find_elements(By.XPATH, ".//td[@data-stat='player']")
for player_name in player_names:
    player_name_list.append(player_name.text)

#fetch player nationality DONE
nationalities = table2.find_elements(By.XPATH, ".//td[@data-stat='nationality']")
for nationality in nationalities:
    nationality_list.append(nationality.text)

#fetch player position DONE
positions = table2.find_elements(By.XPATH, ".//td[@data-stat='position']")
for position in positions:
    position_list.append(position.text)

#fetch player clubs DONE
clubs = table2.find_elements(By.XPATH, ".//td[@data-stat='team']")
for club in clubs:
    player_club_list.append(club.text)

# #fetch player league 
# leagues = table2.find_elements(By.XPATH, ".//td[@data-stat='comp_level']") 
# for league in leagues:
#    league_list.append(league.text) 

#fetch player age DONE
ages = table2.find_elements(By.XPATH, ".//td[@data-stat='age']")
for age in ages:
    age_list.append(age.text)

#fetch shot creating actions DONE
scas = table2.find_elements(By.XPATH, ".//td[@data-stat='sca']")
for sca in scas:
    sca_list.append(sca.text)

#fetch shot creating actions per 90 DONE
shots = table2.find_elements(By.XPATH, ".//td[@data-stat='sca_per90']")
for shot in shots:
    sca90_list.append(shot.text)

#fetch goal creating actions DONE
gcas = table2.find_elements(By.XPATH, ".//td[@data-stat='gca']")
for gca in gcas:
    gca_list.append(gca.text)

#fetch goal creating actions DONE
xs = table2.find_elements(By.XPATH, ".//td[@data-stat='gca_per90']")
for x in xs:
    gca90_list.append(x.text)


with open('championshipgca.pkl', 'wb') as f:
    pickle.dump((player_name_list, nationality_list, position_list, player_club_list, age_list, sca_list, sca90_list, gca_list, gca90_list), f)
