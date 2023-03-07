import selenium 
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
from time import sleep

path = "/Users/danie/Downloads/chromedriver.exe "
service = Service(executable_path=path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)
 
#cookies = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _42y0 _9o-t _4jy3 _4jy1 selected _51sy"]'))).click()

email=driver.find_element(By.ID,'email')
email.send_keys("xxx@email.com")
password=driver.find_element(By.ID, 'pass')
password.send_keys("xxxxxxx")
sleep(1)

login=driver.find_element(By.NAME, 'login')
login.click()
sleep(2)


groups_links_list = [
    "https://www.facebook.com/groups/3698647250201218","https://www.facebook.com/groups/cryptoadvertisingonfacebook","https://www.facebook.com/groups/711727893611883","https://www.facebook.com/groups/makemoneyonline07","https://web.facebook.com/groups/558417114958911","https://web.facebook.com/groups/theworkfromhome","https://web.facebook.com/groups/3405854396179998","https://web.facebook.com/groups/forexbinaryoptionstrading","https://web.facebook.com/groups/bestforextradingsignals","https://web.facebook.com/groups/1330696460624402","https://web.facebook.com/groups/OnlineBusinessMentoringandtools","https://web.facebook.com/groups/iqoptionbd4","https://web.facebook.com/groups/878395403495245","https://web.facebook.com/groups/841527152564944","https://web.facebook.com/groups/778419636129897","https://web.facebook.com/groups/560110697725128","https://web.facebook.com/groups/507079372708836","https://web.facebook.com/groups/Investmentbitcoins","https://web.facebook.com/groups/273476911572378","https://web.facebook.com/groups/bitcoinuse","https://web.facebook.com/groups/220464723584265","https://web.facebook.com/groups/181001415920632","https://web.facebook.com/groups/makemoneyonlinefree4yu","https://web.facebook.com/groups/nicee12maan"
]

for group in groups_links_list:
    driver.get(group)
    sleep(4)
    #driver.execute_script("window.scrollTo(0, 200)")
    postbox = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
    postbox.click()
    sleep(2)
    
    element = driver.switch_to.active_element
    element.send_keys("Message")
    sleep(2)

    postbutton = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
    sleep(1)
    postbutton.click()
    sleep(10)