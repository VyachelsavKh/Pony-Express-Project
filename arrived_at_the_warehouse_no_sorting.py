import log_output
import event_registration
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def check_menu(driver):
    result = event_registration.continue_without_courier_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_menu_name_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1")))
    except:
        log_output.Print('Не нашёл название меню')
        return 'ERROR'

    if element_menu_name_button.text != '71. Прибыл на склад (без сортировки)':
        log_output.Print('Попал не в то меню')
        return 'ERROR'

    log_output.Print('Попал в меню 71. Прибыл на склад (без сортировки)')
    return 'SUCCESS'

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
