import login
import editing_user_groups
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_5():
    login.myPrint("Тест 5")

    driver = editing_user_groups.editing_user_groups(login.paths.login, login.paths.password)
    
    if driver == 'Error':
        return 'Eror'
    
    login.myPrint('Тест 5 пройден')
    
    #time.sleep(5)
    driver.close()