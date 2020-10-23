import login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def editing_user_groups(mylogin, password):
    driver = login.pony_login(mylogin, password)

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
        element_service_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(7) .bp3-text-overflow-ellipsis")))
    except:
        login.myPrint('Не нашёл кнопку Сервис')
        driver.close()
        return 'ERROR'

    element_service_button.click()
    
    login.myPrint("Нажал кнопку Сервис")
    
    try:
        element_permissions_management_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-popover-content:nth-child(1) .bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
    except:
        login.myPrint('Не нашёл кнопку Управление разрешениями')
        driver.close()
        return 'ERROR'
    
    element_permissions_management_button.click()
        
    login.myPrint("Нажал кнопку Управление разрешениями")
    
    try:
        element_group_of_users_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(1) > .bp3-menu-item > .bp3-text-overflow-ellipsis")))
    except:
        login.myPrint('Не нашёл кнопку Группы пользователей')
        driver.close()
        return 'ERROR'
    
    element_group_of_users_button.click()
    
    login.myPrint("Нажал кнопку Группы пользователей")
    
    try:
        element_editing_user_groups = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div/h1")))
    except:
        login.myPrint('Не нашёл идентификатор меню')
        driver.close()
        return 'ERROR'
    
    if element_editing_user_groups.text != 'Редактирование групп пользователей':
        login.myPrint("Попал в другое меню")
        driver.close()
        return 'ERROR'
    else:
        login.myPrint("Попал в меню Редактирование групп пользователей")
        
    return driver