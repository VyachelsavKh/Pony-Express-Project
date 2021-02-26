import paths
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def driver_init():
    driver = 'ERROR'

    with allure.step('Подключение драйвера браузера'):
        if paths.browser == 'Chrome':
            driver = webdriver.Chrome(paths.driver_path)
        if paths.browser == 'Firefox':
            driver = webdriver.Firefox(executable_path = paths.driver_path)

        assert driver != 'ERROR', 'Не смог найти драйвер для работы с браузером'

    with allure.step('Открытие сайта'):
        driver.get(paths.pegas_url)

        try:
            WebDriverWait(driver, paths.search_time).until(EC.title_is(paths.pegas_title))
        except:
            driver.close()
            assert 0, 'Не смог открыть сайт'

        return driver


def login(input_login=paths.correct_enter_login,
          input_password=paths.correct_enter_password):

    driver = driver_init()

    with allure.step('Ввод логина и пароля'):
        try:
            element_login = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
            element_password = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
        except:
            driver.close()
            assert 0, 'Не найдены поля для ввода'

        element_login.send_keys(input_login)
        element_password.send_keys(input_password)

    with allure.step('Нажатие кнопки войти'):
        try:
            element_enter_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/form/button')))
        except:
            driver.close()
            assert 0, ('Не найдена кнопка входа')

        element_enter_button.click()

        return driver

def check_enty(driver):
    with allure.step('Проверка входа в систему'):
        try:
            WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
        except:
            driver.close()
            assert 0, 'Не смог войти в систему'

def check_non_entry(driver):
    with allure.step('Проверка входа в систему'):
        elem_wrong_login_password = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))

        if elem_wrong_login_password.text != 'Неверный логин или пароль':
            driver.close()
            assert 0, 'Смог войти в систему'