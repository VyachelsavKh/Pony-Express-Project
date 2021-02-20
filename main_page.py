import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def quit(driver):
    with allure.step('Нажатие кнопки выхода'):
        try:
            element_exit_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку выхода'

        element_exit_button.click()

    with allure.step('Проверка выхода из системы'):
        try:
            WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))

            WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
        except:
            driver.close()
            assert 0, 'Не вернулся на главную страницу'

def menu_button(driver):
    with allure.step('Нажатие кнопки меню'):
        try:
            element_menu_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку меню'

        element_menu_button.click()