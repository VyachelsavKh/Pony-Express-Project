import log_output
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def quit(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_exit_button = element_menu_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/div[2]/div/button[2]')))
    except:
        log_output.Print('Не нашёл кнопку выхода')
        return 'ERROR'

    element_exit_button.click()

    log_output.Print('Вышел из системы')

    try:
        element_login = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))

        element_password = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        log_output.Print('Не вернулся на главную страницу')
        return 'ERROR'

    log_output.Print('Вернулся на главную страницу')
    return 'SUCCESS'


def menu_button(driver):
    if driver == 'ERROR':
        return

    try:
        element_menu_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    except:
        log_output.Print('Не нашёл кнопку меню')
        return 'ERROR'

    element_menu_button.click()

    log_output.Print('Нажал кнопку меню')

    return 'SUCCESS'


if __name__ == '__main__':
    print('Файл содержит функции нажатия на кнопки на гланой странице')
