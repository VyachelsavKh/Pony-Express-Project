import login
import editing_user_groups
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_8():
    login.myPrint("Тест 8")

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

    element_menu_button.click()
    
    login.myPrint("Нажал кнопку Меню")
    
    try:
        element_manufacture_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
    except:
        login.myPrint('Не нашёл кнопку Производство')
        driver.close()
        return 'ERROR'

    element_manufacture_button.click()
    
    login.myPrint("Нажал кнопку Производство")
    
    try:
        element_event_registration_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span")))
    except:
        login.myPrint('Не нашёл кнопку Регистрация событий')
        driver.close()
        return 'ERROR'
    
    element_event_registration_button.click()
    
    login.myPrint("Нажал кнопку Регистрация событий")
    
    try:
        element_no_sorting_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a")))
    except:
        login.myPrint('Не нашёл кнопку Прибыл на склад(Без сортировки)')
        driver.close()
        return 'ERROR'
    
    element_no_sorting_button.click()
    
    login.myPrint("Нажал кнопку Прибыл на склад(Без сортировки)")
    
    time.sleep(2)
    
    driver.switch_to_window(driver.window_handles[1])
    
    try:
        element_without_courier_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]/span")))
    except:
        login.myPrint('Не нашёл кнопку Без курьера')
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'ERROR'
    
    element_without_courier_button.click()
    
    login.myPrint('Нажал кнопку Без курьера')
    
    try:
        element_menu_name_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1")))
    except:
        login.myPrint('Не нашёл название меню')
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'ERROR'
    
    if element_menu_name_button.text != '71. Прибыл на склад (без сортировки)':
        login.myPrint('Попал не в то меню')
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.close()
        return 'ERROR'
    
    login.myPrint('Попал в меню 71. Прибыл на склад (без сортировки)')
    
    login.myPrint("Тест 8 пройден")
    
    time.sleep(5)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.close()