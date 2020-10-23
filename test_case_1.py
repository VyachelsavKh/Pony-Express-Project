import login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_1():
    login.myPrint("Тест 1")

    driver = login.pony_login(login.paths.login, login.paths.password)

    if driver == 'ERROR':
        return
    
    try:
        element_menu_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    except:
        login.myPrint('Не зашёл в систему')
        driver.close()
        return 'ERROR'

    login.myPrint('Вошёл в систему')
    login.myPrint('Тест 1 пройден')

    #time.sleep(5)
    driver.close()