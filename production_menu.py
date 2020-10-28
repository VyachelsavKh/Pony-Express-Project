import main_page
import paths
import log_output
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def production_button(driver):
    result = main_page.menu_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_manufacture_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
    except:
        log_output.Print('Не нашёл кнопку Производство')
        return 'ERROR'

    element_manufacture_button.click()

    log_output.Print("Нажал кнопку Производство")
    return 'SUCCESS'

def event_registration_button(driver):
    result = production_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_event_registration_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span")))
    except:
        log_output.Print('Не нашёл кнопку Регистрация событий')
        return 'ERROR'

    element_event_registration_button.click()

    log_output.Print("Нажал кнопку Регистрация событий")
    return 'SUCCESS'