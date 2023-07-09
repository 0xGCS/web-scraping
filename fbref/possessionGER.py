import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import openpyxl


PATH = '{enter_path_of_chrome_driver}' #need to fill this in
s = Service(PATH)
driver = webdriver.Chrome(service=s)

url = 'https://fbref.com/en/comps/20/possession/Bundesliga-Stats' #change URL here for different competitions
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
age_list = []
touches_list = []
defpen_list = []
def3rd_list = []
mid3rd_list = []
att3rd_list = []
attpen_list = []
live_list = []
takeons_list = []
takeonswon_list = []
takeonswonpct_list = []
takeonstackled_list = []
takeonstackledpct_list = []
carries_list = []
carries_distance_list = []
carries_progressive_distance_list = []
progressive_carries_list = []
carries_into_final_third_list = []
carries_into_penalty_area_list = []
miscontrols_list = []
dispossessed_list = []


#fetch the player table
table2 = driver.find_element(By.ID, 'stats_possession')

#fetch player names
zs = table2.find_elements(By.XPATH, ".//td[@data-stat='player']")
for z in zs:
    player_name_list.append(z.text)

#fetch player nationality
xs = table2.find_elements(By.XPATH, ".//td[@data-stat='nationality']")
for x in xs:
    nationality_list.append(x.text)

#fetch player position
ys = table2.find_elements(By.XPATH, ".//td[@data-stat='position']")
for y in ys:
    position_list.append(y.text)

#fetch player clubs
ws = table2.find_elements(By.XPATH, ".//td[@data-stat='team']")
for w in ws:
    player_club_list.append(w.text)


#fetch player age
us = table2.find_elements(By.XPATH, ".//td[@data-stat='age']")
for u in us:
    age_list.append(u.text)

#total touches
aas = table2.find_elements(By.XPATH, ".//td[@data-stat='touches']")
for aa in aas:
    touches_list.append(aa.text)

#Def Pen -- Touches 
bs = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_def_pen_area']")
for b in bs:
    defpen_list.append(b.text)

#Def 3rd -- Touches (total) 
cs = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_def_3rd']")
for c in cs:
    def3rd_list.append(c.text)

#Mid 3rd -- Touches 
ds = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_mid_3rd']")
for d in ds:
    mid3rd_list.append(d.text)

#Att 3rd -- Touches 
es = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_att_3rd']")
for e in es:
    att3rd_list.append(e.text)

#Att Pen -- Touches
fs = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_att_pen_area']")
for f in fs:
    attpen_list.append(f.text)

#Live -- Touches 
gs = table2.find_elements(By.XPATH, ".//td[@data-stat='touches_live_ball']")
for g in gs:
    live_list.append(g.text)

#Att -- Take-Ons Attempted
hs = table2.find_elements(By.XPATH, ".//td[@data-stat='take_ons']")
for h in hs:
    takeons_list.append(h.text)

#Succ -- Successful Take-Ons
iis = table2.find_elements(By.XPATH, ".//td[@data-stat='take_ons_won']")
for ii in iis:
    takeonswon_list.append(ii.text)

#Succ% -- Successful Take-On %
js = table2.find_elements(By.XPATH, ".//td[@data-stat='take_ons_won_pct']")
for j in js:
    takeonswonpct_list.append(j.text)

#Tkld -- Times Tackled During Take-On
ks = table2.find_elements(By.XPATH, ".//td[@data-stat='take_ons_tackled']")
for k in ks:
    takeonstackled_list.append(k.text)

#Tkld% -- Tackled During Take-On Percentage
ls = table2.find_elements(By.XPATH, ".//td[@data-stat='take_ons_tackled_pct']")
for l in ls:
    takeonstackledpct_list.append(l.text)

#Carries
ms = table2.find_elements(By.XPATH, ".//td[@data-stat='carries']")
for m in ms:
    carries_list.append(m.text)

#TotDist -- Total Carrying Distance
ns = table2.find_elements(By.XPATH, ".//td[@data-stat='carries_distance']")
for n in ns:
    carries_distance_list.append(n.text)

#PrgDist -- Progressive Carrying Distance
os = table2.find_elements(By.XPATH, ".//td[@data-stat='carries_progressive_distance']")
for o in os:
    carries_progressive_distance_list.append(o.text)

#PrgC -- Progressive Carries
ps = table2.find_elements(By.XPATH, ".//td[@data-stat='progressive_carries']")
for p in ps:
    progressive_carries_list.append(p.text)

#1/3 -- Carries into Final Third
qs = table2.find_elements(By.XPATH, ".//td[@data-stat='carries_into_final_third']")
for q in qs:
    carries_into_final_third_list.append(q.text)
    
#CPA -- Carries into Penalty Area
rs = table2.find_elements(By.XPATH, ".//td[@data-stat='carries_into_penalty_area']")
for r in rs:
    carries_into_penalty_area_list.append(r.text)
    
#Mis -- Miscontrols
ss = table2.find_elements(By.XPATH, ".//td[@data-stat='miscontrols']")
for s in ss:
    miscontrols_list.append(s.text)

#Dis -- Dispossessed
ts = table2.find_elements(By.XPATH, ".//td[@data-stat='dispossessed']")
for t in ts:
    dispossessed_list.append(t.text)

df = pd.DataFrame(zip(player_name_list, nationality_list, position_list, player_club_list, age_list, touches_list, defpen_list, def3rd_list, mid3rd_list, att3rd_list, attpen_list, live_list, takeons_list, takeonswon_list, takeonswonpct_list, takeonstackled_list, takeonstackledpct_list, carries_list, carries_distance_list, carries_progressive_distance_list, progressive_carries_list, carries_into_final_third_list, carries_into_penalty_area_list, miscontrols_list, dispossessed_list),columns =['name', 'nationality', 'position', 'club', 'age', 'touches', 'defpen', 'def3rd', 'mid3rd','att3rd','attpen', 'live', 'takeons', 'takeonswon', 'takeonswon%', 'takeonstackled', 'takeonstackled%', 'carries', 'carries_distance','prgDist','PrgC','Cfinal3rd','CPA','miscontrols','dispossed'])
df.to_excel('bundesliga.xlsx', index=False)
