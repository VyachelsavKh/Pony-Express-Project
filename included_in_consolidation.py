import log_output
import event_registration
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def choose_destination_button(driver):
    if driver == 'ERROR':
        return 'ERROR'

    result = event_registration.included_in_consolidation_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_choose_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button')))
    except:
        log_output.Print('Не нашёл кнопку Выбрать')
        return 'ERROR'

    element_choose_button.click()

    log_output.Print('Нажал кнопку Выбрать')

def input_dote_name(driver, name):
    if driver == 'ERROR':
        return 'ERROR'

    result = choose_destination_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_search_field = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="search-input"]')))
    except:
        log_output.Print('Не нашёл поле поиска')
        return 'ERROR'

    element_search_field.send_keys(name)

    return 'SUCCESS'


def choose_the_first_group(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_first_group_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/label/span')))
    except:
        log_output.Print('Не нашёл кнопку выделения 1 точки назначения')
        return 'ERROR'

    element_first_group_button.click()

    log_output.Print('Выделил 1 точку назначения')

    try:
        element_add_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]/span')))
    except:
        log_output.Print('Не нашёл кнопку Добавить')
        return 'ERROR'

    element_add_button.click()

    log_output.Print('Нажал кнопку Добавить')

    return 'SUCCESS'

def continue_button(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_continue_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button')))
    except:
        log_output.Print('Не нашёл кнопку Далее')
        return 'ERROR'

    element_continue_button.click()

    log_output.Print('Нажал кнопку Далее')

    return 'SUCCESS'


def check_menu(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_menu_name_field = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[1]/h1')))
    except:
        log_output.Print('Не нашёл идентификатор меню')
        return 'ERROR'

    if element_menu_name_field.text == '79. Включен в консолидацию':
        log_output.Print('Попал в меню 79. Включен в консолидацию')
        return 'SUCCESS'
    else:
        log_output.Print('Попал в другое меню')
        return 'ERROR'


def enter_object_number(driver, name):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_object_number = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))
    except:
        log_output.Print('Не найдено поле ввода номера объекта')
        return 'ERROR'

    element_object_number.send_keys(name)
    element_object_number.send_keys(Keys.RETURN)

    log_output.Print('Ввёл название объекта: ' + name)
    return 'SUCCESS'


def check_colour(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_object_number = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div')))
    except:
        log_output.Print('Не найдено поле ввода номера объекта')
        return 'ERROR'

    return element_object_number.get_attribute('style')

def full_screen_button(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_full_screen_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[1]/div/button/span[2]')))
    except:
        log_output.Print('Не нашёл кнопку Полноэкранного режима')
        return 'ERROR'

    element_full_screen_button.click()

    log_output.Print('Нажал кнопку Полноэкранный режим')

    return 'SUCCESS'


def enter_object_name_full_screen(driver, name):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_object_number = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/form/input')))
    except:
        log_output.Print('Не найдено поле ввода номера объекта')
        return 'ERROR'

    element_object_number.send_keys(name)
    element_object_number.send_keys(Keys.RETURN)

    log_output.Print('Ввёл название объекта: ' + name)
    return 'SUCCESS'


def check_colour_full_screen(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_object_number = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div')))
    except:
        log_output.Print('Не найдено поле ввода номера объекта')
        return 'ERROR'

    return element_object_number.get_attribute('style')