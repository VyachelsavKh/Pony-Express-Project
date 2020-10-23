import login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_3():
    login.myPrint("Тест 3")

    wrong_login = 'wrong_login'
    wrong_password = 'wrong_password'
    
    driver = login.pony_login(wrong_login, wrong_password)
	
    if driver == 'ERROR':
        return
    
    elem_wrong_password = element_login = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))
	
    if elem_wrong_password.text == 'Неверный логин или пароль':
        login.myPrint('Неверный логин или пароль')
        login.myPrint('Тест 3 пройден')
    else:
        login.myPrint('Произошло чудо, пароль и логин верны')
        driver.close()
        return 'ERROR'
	
    #time.sleep(5)
    driver.close()