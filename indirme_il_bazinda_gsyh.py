#### Drivers required ####
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
import time
import os
import shutil
import subprocess

print('Modules imported.')
# Setting Webdriver
DRIVER_PATH = r'C:\Users\User\Desktop\chromedriver.exe'  # BILGISAYARDA chromedriver'ın bulunduğu yer
options = Options() 
options.headless = False
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
### Opens driver
driver.get("https://biruni.tuik.gov.tr/medas/")
## Chooses the dataset
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div/div/div/select'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div/div/div/select/option[10]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[4]'))).click()
time.sleep(0.5)
## Choosing required dataset
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[2]/table/tbody/tr/td/table/tbody/tr/td[1]/div/div[3]/table/tbody[1]/tr[1]/td[2]/div'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[2]/table/tbody/tr/td/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr/td/table/tbody/tr[1]/td/div/div/table/tbody[1]/tr[3]/td[1]/div/span[2]'))).click()
## Clicking TAMAM
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[2]/table/tbody/tr/td/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td/table/tbody/tr/td[5]/div/button[1]'))).click()
## Choosing Sub-set
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div[3]/div[4]/table/tbody[1]/tr[1]/td/div'))).click()
time.sleep(0.5)
## Choosing Sub-set
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div/div[2]/div[2]/div[3]/div[4]/table/tbody[1]/tr/td/div'))).click()
time.sleep(0.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/div/div[3]/div[2]/div[3]/div[4]/table/tbody[1]/tr[3]/td/div/span[2]'))).click()
## Adding GÖSTERGE
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[6]/div[1]/div/div/div/table/tbody/tr/td/table/tbody/tr/td[1]/a/span'))).click()
## Clickking İLERİ
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/div[9]/button'))).click()
## Adding all the years
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr/td/table/tbody/tr/td[1]/div/div[1]/table/tbody/tr/th[1]/div/span'))).click()
#Clicking İLERİ
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/button[2]'))).click()
## Choosing all the provinces
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div[1]/div/div[1]/div/div/div/select'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div[1]/div/div[1]/div/div/div/select/option[4]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[4]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div[1]/div/div[2]/table/tbody/tr/td/table/tbody/tr/td[1]/div/div[1]/table/tbody/tr/th[1]/div/span'))).click()
## Clicking RAPOR OLUŞTUR
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/div[2]/button[2]'))).click()
## Downloading
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[3]/div[2]/div[4]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div/div[2]/a'))).click()
# Wait for two second
time.sleep(2)
## Copying and deleting the file
source =r'C:\Users\User\Downloads\pivot.csv'
destination = r'C:\Users\User\Desktop\TEPAV\TEPAV-DATABASE\il_bazinda_gsyh\il_bazinda_gsyh.csv'
shutil.copyfile(source, destination)
os.remove(source)
driver.quit()