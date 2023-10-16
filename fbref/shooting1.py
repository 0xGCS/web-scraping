import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

PATH = ''/path/to/your/driver''
s = Service(PATH)
driver = webdriver.Chrome(service=s)

url = 'https://fbref.com/en/comps/10/shooting/Championship-Stats'
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
nineties_list = []
shots_list = []
sot_list = []
sotpercent_list = []
shotper90_list = []
sotper90_list = []
goalpershot_list = []
goalpersot_list = []


#fetch the second table DONE
table2 = driver.find_element(By.ID, 'stats_shooting')

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

#fetch 90 min played DONE
fullmatch = table2.find_elements(By.XPATH, ".//td[@data-stat='minutes_90s']")
for y in fullmatch:
    nineties_list.append(y.text)

#fetch shots total DONE
shots = table2.find_elements(By.XPATH, ".//td[@data-stat='shots']")
for shot in shots:
    shots_list.append(shot.text)

#fetch shots on target DONE
sots = table2.find_elements(By.XPATH, ".//td[@data-stat='shots_on_target']")
for sot in sots:
    sot_list.append(sot.text)

#fetch shots on target % DONE
xs = table2.find_elements(By.XPATH, ".//td[@data-stat='shots_on_target_pct']")
for x in xs:
    sotpercent_list.append(x.text)

#fetch shots per 90 DONE
spns = table2.find_elements(By.XPATH, ".//td[@data-stat='shots_per90']")
for spn in spns:
    shotper90_list.append(spn.text)

#fetch sot per 90 DONE
sotpns = table2.find_elements(By.XPATH, ".//td[@data-stat='shots_on_target_per90']")
for sotpn in sotpns:
    sotper90_list.append(sotpn.text)

#fetch goals per shotDONE
gpss = table2.find_elements(By.XPATH, ".//td[@data-stat='goals_per_shot']")
for gps in gpss:
    goalpershot_list.append(gps.text)

#fetch goals per sot
gpsots = table2.find_elements(By.XPATH, ".//td[@data-stat='goals_per_shot_on_target']")
for gpsot in gpsots:
    goalpersot_list.append(gpsot.text)


with open('championshipshooting.pkl', 'wb') as f:
    pickle.dump((player_name_list, nationality_list, position_list, player_club_list, age_list, nineties_list, shots_list, sot_list, sotpercent_list, shotper90_list, sotper90_list, goalpershot_list, goalpersot_list), f)
