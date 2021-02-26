import event_registration
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

def choose_destination_button(driver):
    event_registration.included_in_consolidation_button(driver)

    with allure.step('Нажатие кнопки выбрать'):
        try:
            element_choose_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопку Выбрать'

        element_choose_button.click()

def input_dote_name(driver, name):
    choose_destination_button(driver)

    time.sleep(1)

    with allure.step('Ввод номера точки назначения'):
        try:
            element_search_field = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="search-input"]')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл поле поиска'

        element_search_field.send_keys(name)

def choose_the_first_group(driver):
    with allure.step('Выделение 1 точки назначения'):
        try:
            element_first_group_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/p/label/span')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопку выделения 1 точки назначения'

        element_first_group_button.click()

    with allure.step('Нажатие кнопки добавить'):
        try:
            element_add_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/button[1]')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопку Добавить'

        element_add_button.click()

def continue_button(driver):
    with allure.step('Нажатие кнопки далее'):
        try:
            element_continue_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопку Далее'

        element_continue_button.click()

def check_menu(driver):
    try:
        element_menu_name_field = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[1]/h1')))
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        assert 0, 'Не нашёл идентификатор меню'

    if element_menu_name_field.text != '79. Включен в консолидацию':
        assert 0, 'Попал в другое меню'

def enter_object_number(driver, name):
    with allure.step('Ввод номера объекта'):
        try:
            element_object_number = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не найдено поле ввода номера объекта'

        element_object_number.send_keys(name)
        element_object_number.send_keys(Keys.RETURN)

def check_colour(driver):
    with allure.step('Проверка цвета рамки'):
        try:
            element_object_number = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не найдено поле ввода номера объекта'

        return element_object_number.get_attribute('style')

def full_screen_button(driver):
    with allure.step('Переход в полноэкранный режим'):
        try:
            element_full_screen_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[1]/div/button/span[2]')))
        except:
            assert 0, 'Не нашёл кнопку Полноэкранного режима'

        element_full_screen_button.click()

def enter_object_name_full_screen(driver, name):
    with allure.step('Ввод номера объекта'):
        try:
            element_object_number = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/form/input')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не найдено поле ввода номера объекта'

        element_object_number.send_keys(name)
        element_object_number.send_keys(Keys.RETURN)

def check_colour_full_screen(driver):
    with allure.step('Проверка цвета рамки'):
        try:
            element_object_number = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div')))
        except:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.close()
                assert 0, 'Не найдено поле ввода номера объекта'

        return element_object_number.get_attribute('style')