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

url = 'https://fbref.com/en/comps/10/stats/Championship-Stats'
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
games_list = []
starts_list = []
minutes_list = []
gls_list = []
ast_list = []
xg_list = []
xag_list = []
prgc_list = []
prgp_list = []
prgr_list = []
glsper90_list = []
astper90_list = []
xgper90_list = []
xagper90_list = []


#fetch the second table
table2 = driver.find_element(By.ID, 'stats_standard')

#fetch player names
player_names = table2.find_elements(By.XPATH, ".//td[@data-stat='player']")
for player_name in player_names:
    player_name_list.append(player_name.text)

#fetch player nationality
nationalities = table2.find_elements(By.XPATH, ".//td[@data-stat='nationality']")
for nationality in nationalities:
    nationality_list.append(nationality.text)

#fetch player position
positions = table2.find_elements(By.XPATH, ".//td[@data-stat='position']")
for position in positions:
    position_list.append(position.text)

#fetch player clubs
clubs = table2.find_elements(By.XPATH, ".//td[@data-stat='team']")
for club in clubs:
    player_club_list.append(club.text)

# #fetch player league 
# leagues = table2.find_elements(By.XPATH, ".//td[@data-stat='comp_level']") 
# for league in leagues:
#    league_list.append(league.text) 

#fetch player age
ages = table2.find_elements(By.XPATH, ".//td[@data-stat='age']")
for age in ages:
    age_list.append(age.text)

#fetch goals
games = table2.find_elements(By.XPATH, ".//td[@data-stat='games']")
for game in games:
    games_list.append(game.text)

#fetch starts
starts = table2.find_elements(By.XPATH, ".//td[@data-stat='games_starts']")
for start in starts:
    starts_list.append(start.text)

#fetch minutes
minutes = table2.find_elements(By.XPATH, ".//td[@data-stat='minutes']")
for minute in minutes:
    minutes_list.append(minute.text)

#fetch goals
goals = table2.find_elements(By.XPATH, ".//td[@data-stat='goals']")
for goal in goals:
    gls_list.append(goal.text)

#fetch assists
assists = table2.find_elements(By.XPATH, ".//td[@data-stat='assists']")
for assist in assists:
    ast_list.append(assist.text)

#fetch xg
xg = table2.find_elements(By.XPATH, ".//td[@data-stat='xg']")
for x in xg:
    xg_list.append(x.text)

#fetch xag
xag = table2.find_elements(By.XPATH, ".//td[@data-stat='xg_assist']")
for xa in xag:
    xag_list.append(xa.text)

#fetch prgc
prgc = table2.find_elements(By.XPATH, ".//td[@data-stat='progressive_carries']")
for prg in prgc:
    prgc_list.append(prg.text)

#fetch prgp
prgp = table2.find_elements(By.XPATH, ".//td[@data-stat='progressive_passes']")
for q in prgp:
    prgp_list.append(q.text)

#fetch prgr
prgr = table2.find_elements(By.XPATH, ".//td[@data-stat='progressive_passes_received']")
for w in prgr:
    prgr_list.append(w.text)

#fetch goals per 90min
goals_per90 = table2.find_elements(By.XPATH, ".//td[@data-stat='goals_per90']")
for e in goals_per90:
    glsper90_list.append(e.text)

#fetch assist per 90min
ast_per90 = table2.find_elements(By.XPATH, ".//td[@data-stat='assists_per90']")
for r in ast_per90:
    astper90_list.append(r.text)

#fetch xg per 90min
xgper90 = table2.find_elements(By.XPATH, ".//td[@data-stat='xg_per90']")
for t in xgper90:
    xgper90_list.append(t.text)

#fetch xag per 90min
xagper90 = table2.find_elements(By.XPATH, ".//td[@data-stat='xg_assist_per90']")
for y in xagper90:
    xagper90_list.append(y.text)

with open('championship.pkl', 'wb') as f:
    pickle.dump((player_name_list,nationality_list,position_list,player_club_list,age_list,games_list,starts_list,minutes_list,gls_list,ast_list,xg_list,xag_list, prgc_list, prgp_list, prgr_list, glsper90_list, astper90_list, xgper90_list, xagper90_list), f)
