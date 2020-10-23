import paths
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def myPrint(string):
    if paths.print_to_output_to_file:
        print(string)
        with open(paths.output_file_name, 'a') as output_file:
            output_file.write(string + '\n')
    else:
        print(string)

def pony_driver_init():
    driver = webdriver.Chrome(paths.driver_path)
    driver.get(paths.pegas_url)

    try:
        title = WebDriverWait(driver, 5).until(EC.title_is('Пегас'))
    except:
        myPrint('Не смог открыть сайт')
        driver.close()
        return 'ERROR'

    myPrint('Открыл сайт')

    return driver
	
def pony_login(login, password):
	driver = pony_driver_init()
	
	if driver == 'ERROR':
		return
		
	try:
		element_login = WebDriverWait(driver, 5).until(
			EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
		
		element_password = WebDriverWait(driver, 5).until(
			EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
			
	except:
		myPrint('Не найдены поля для ввода')
		driver.close()
		return 'ERROR'
		
	element_login.send_keys(login)
	element_password.send_keys(password)
	
	myPrint('Ввёл логин и пароль')
	
	try:
		element_enter_button = WebDriverWait(driver, 5).until(
			EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/form/button')))
	except:		
		myPrint('Не найдена кнопка входа')
		driver.close()
		return 'ERROR'
		
	
	element_enter_button.click()
	
	myPrint('Нажал кнопку войти')
	
	return driver
    