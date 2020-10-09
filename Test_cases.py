import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pony_driver_init(driver_path):
	pegas_url = 'http://pegasus-edu.pegasus.ponyex.local/'
	
	driver = webdriver.Chrome(driver_path)
	driver.get(pegas_url)
	
	try:
		title = WebDriverWait(driver, 10).until(EC.title_is('Пегас'))
	except:
		print('Не смог открыть сайт')
		driver.close()
		return 'ERROR'
	
	print('Открыл сайт')
	
	return driver
	
def pony_login(driver_path, login, password):
	driver = pony_driver_init(driver_path)
	
	if driver == 'ERROR':
		return
		
	try:
		element_login = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
		
		element_password = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
			
	except:
		print('Не найдены поля для ввода')
		driver.close()
		return 'ERROR'
		
	element_login.send_keys(login)
	element_password.send_keys(password)
	
	print('Ввёл логин и пароль')
	
	try:
		element_enter_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/button')))
	except:		
		print('Не найдена кнопка входа')
		driver.close()
		return 'ERROR'
		
	
	element_enter_button.click()
	
	print('Нажал кнопку войти')
	
	return driver
	
def case_1(driver_path):
	login = 'ext.mgu_education'
	password = 'rg#P5hZm4F'
	
	driver = pony_login(driver_path, login, password)

	try:
		element_menu_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
	except:
		print('Не зашёл в систему')
		driver.close()
		return 'ERROR'

	print('Вошёл в систему')
	print('Тест 1 пройден')

	#time.sleep(10)
	driver.close()

def case_2(driver_path):
	login = 'ext.mgu_education'
	password = 'rg#P5hZm4F'
	
	driver = pony_login(driver_path, login, password)
	
	try:
		element_menu_button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
	except:
		print('Не зашёл в систему')
		driver.close()
		return 'ERROR'

	print('Вошёл в систему')
	
	try:
		element_exit_button = element_menu_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
	except:
		print('Не нашёл кнопку выхода')
		driver.close()
		return 'ERROR'
	
	element_exit_button.click()
	
	print('Вышел из системы')
	
	try:
		element_login = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
		
		element_password = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
			
	except:
		print('Не найдены поля для ввода')
		driver.close()
		return 'ERROR'
		
	print('Вернулся на главную страницу')
	print('Тест 2 пройден')
	
	#time.sleep(10)
	driver.close()

def case_3(driver_path):
	login = 'wronglogin'
	password = 'wrongpassword'
	
	driver = pony_login(driver_path, login, password)
	
	elem_wrong_password = element_login = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))
	
	if elem_wrong_password.text == 'Неверный логин или пароль':
		print('Неверный логин или пароль')
		print('Тест 3 пройден')
	else:
		print('Произошло чудо, пароль и логин верны')
		driver.close()
		return 'ERROR'
	
	#time.sleep(10)
	driver.close()

if __name__ == "__main__":
	driver_path = r'./chromedriver.exe'
	
	#case_1(driver_path)
	#case_2(driver_path)
	#case_3(driver_path)
	
	
	
	
	
	
	
	
	
	