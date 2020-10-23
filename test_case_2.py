import login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_2():
    login.myPrint("Тест 2")

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
	
    try:
        element_exit_button = element_menu_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
    except:
        login.myPrint('Не нашёл кнопку выхода')
        driver.close()
        return 'ERROR'
	
    element_exit_button.click()
	
    login.myPrint('Вышел из системы')
	
    try:
        element_login = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))

        element_password = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
			
    except:
        login.myPrint('Не найдены поля для ввода')
        driver.close()
        return 'ERROR'
		
    login.myPrint('Вернулся на главную страницу')
    login.myPrint('Тест 2 пройден')
	
    #time.sleep(5)
    driver.close()