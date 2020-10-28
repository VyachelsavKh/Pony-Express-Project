import paths
import waitings
import log_output
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver_init():
    driver = 'ERROR'

    if paths.browser == 'Chrome':
        driver = webdriver.Chrome(paths.driver_path)
    if paths.browser == 'Firefox':
        driver = webdriver.Firefox(executable_path = paths.driver_path)

    if driver == 'ERROR':
        return 'ERROR'

    driver.get(paths.pegas_url)

    try:
        title = WebDriverWait(driver, paths.search_time).until(EC.title_is(paths.pegas_title))
    except:
        log_output.Print('Не смог открыть сайт')
        waitings.visual_checking()
        driver.close()
        return 'ERROR'

    log_output.Print('Открыл сайт')

    return driver


def login(input_login=paths.correct_enter_login,
          input_password=paths.correct_enter_password):
    driver = driver_init()

    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_login = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[1]')))
        element_password = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/input[2]')))
    except:
        log_output.Print('Не найдены поля для ввода')
        waitings.visual_checking()
        driver.close()
        return 'ERROR'

    element_login.send_keys(input_login)
    element_password.send_keys(input_password)

    log_output.Print('Ввёл логин и пароль')

    try:
        element_enter_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/form/button')))
    except:
        log_output.Print('Не найдена кнопка входа')
        waitings.visual_checking()
        driver.close()
        return 'ERROR'

    element_enter_button.click()

    log_output.Print('Нажал кнопку войти')

    return driver


def check_enty(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_menu_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
    except:
        log_output.Print('Не зашёл в систему')
        return 'Wrong identifiers'

    log_output.Print('Вошёл в систему')
    return 'Correct identifiers'


def check_non_entry(driver):
    if driver == 'ERROR':
        return 'ERROR'

    elem_wrong_login_password = WebDriverWait(driver, paths.search_time).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/form/p')))

    if elem_wrong_login_password.text == 'Неверный логин или пароль':
        log_output.Print('Не зашёл в систему')
        return 'Wrong identifiers'
    else:
        log_output.Print('Вошёл в систему')
        return 'Correct identifiers'


if __name__ == "__main__":
    print("Файл содержит функцию авторизации на сайте и проверку успешности авторизации")

    driver = login()

    check_enty(driver)
    #check_non_entry(driver)

    waitings.visual_checking()
    driver.close()
