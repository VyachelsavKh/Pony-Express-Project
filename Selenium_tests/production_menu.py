import main_page
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def production_button(driver):
    main_page.menu_button(driver)

    with allure.step('Нажатие кнопки Производство'):
        try:
            element_manufacture_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Производство'

        element_manufacture_button.click()

def event_registration_button(driver):
    production_button(driver)

    with allure.step('Нажатие кнопки Регистрация событий'):
        try:
            element_event_registration_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Регистрация событий'

        element_event_registration_button.click()