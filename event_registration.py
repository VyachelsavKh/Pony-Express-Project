import log_output
import production_menu
import waitings
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def arrived_at_the_warehouse_without_sorting_button(driver):
    result = production_menu.event_registration_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_no_sorting_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a")))
    except:
        log_output.Print('Не нашёл кнопку Прибыл на склад(Без сортировки)')
        return 'ERROR'

    element_no_sorting_button.click()

    log_output.Print("Нажал кнопку Прибыл на склад(Без сортировки)")

    waitings.transitioning()

    driver.switch_to_window(driver.window_handles[1])

    try:
        element_without_courier_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]/span")))
    except:
        log_output.Print('Попал в другое меню')
        return 'ERROR'

    log_output.Print('Попал в меню Ввод данных о блоке')

    return 'SUCCESS'

def continue_without_courier_button(driver):
    result = arrived_at_the_warehouse_without_sorting_button(driver)

    waitings.transitioning()

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_without_courier_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]/span")))
    except:
        log_output.Print('Не нашёл кнопку Без курьера')
        return 'ERROR'

    element_without_courier_button.click()

    log_output.Print('Нажал кнопку Без курьера')