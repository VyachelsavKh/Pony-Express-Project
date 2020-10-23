import login
import editing_user_groups
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def case_6():
    login.myPrint("Тест 6")

    driver = editing_user_groups.editing_user_groups(login.paths.login, login.paths.password)
    
    if driver == 'Error':
        return 'Eror'
        
    try:
        element_create_new_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
    except:
        login.myPrint('Не нашёл кнопку Создать новую')
        driver.close()
        return 'ERROR'    
    
    element_create_new_button.click()
    
    login.myPrint("Нажал кнопку Создать новую")
    
    try:
        element_groop_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input")))
    except:
        login.myPrint('Не нашёл поля для ввода названия группы')
        driver.close()
        return 'ERROR'    
    
    date = datetime.datetime.now()
    name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop')
    
    element_groop_name.send_keys(name)
    
    login.myPrint("Ввёл название группы: " + name)
    
    try:
        element_save_groop_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]/span")))
    except:
        login.myPrint('Не нашёл кнопку Сохранить')
        driver.close()
        return 'ERROR'   
    
    element_save_groop_button.click()
    
    login.myPrint("Нажал кнопку сохранить")
    
    try:
        element_find_groop_element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
    except:
        login.myPrint('Не нашёл строки поиска группы')
        driver.close()
        return 'ERROR'   
    
    element_find_groop_element.send_keys(name)
    
    login.myPrint('Ввёл название группы в поле поиска')
    
    try:
        element_my_groop = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]")))
    except:
        login.myPrint('Не нашёл созданную группу')
        driver.close()
        return 'ERROR'   
    
    if element_my_groop.text != name:
        login.myPrint("Нашёл группу с похожим именем")
        driver.close()
        return 'ERROR'   
    
    login.myPrint("Нашёл созданную группу")
    
    try:
        element_put_a_tick_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span")))
    except:
        login.myPrint('Не нашёл поля для выделения группы')
        driver.close()
        return 'ERROR'
    
    element_put_a_tick_button.click()
        
    login.myPrint('Выделил группу')
        
    try:
        element_delete_groop_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]")))
    except:
        login.myPrint('Не нашёл кнопку Удалить группу')
        driver.close()
        return 'ERROR'
        
    element_delete_groop_button.click()
        
    login.myPrint('Нажал кнопку Удалить группу')
    
    try:
        element_delete_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]")))
    except:
        login.myPrint('Не нашёл кнопку Удалить')
        driver.close()
        return 'ERROR'
    
    element_delete_button.click()
    
    login.myPrint('Нажал кнопку Удалить')
    
    #time.sleep(5)
    driver.close()