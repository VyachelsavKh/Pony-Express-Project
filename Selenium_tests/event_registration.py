import production_menu
import time
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def arrived_at_the_warehouse_without_sorting_button(driver):
    production_menu.event_registration_button(driver)

    with allure.step('Нажатие кнопки 71. Прибыл на склад(Без сортировки)'):
        try:
            element_no_sorting_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a")))
        except:
            assert 0, 'Не нашёл кнопку 71. Прибыл на склад(Без сортировки)'

        element_no_sorting_button.click()

    time.sleep(paths.transition_time)

    driver.switch_to.window(driver.window_handles[1])

    with allure.step('Проверка меню'):
        try:
            WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/button[2]")))
        except:
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            driver.close()
            assert 0, 'Попал в другое меню'

def continue_without_courier_button(driver):
    arrived_at_the_warehouse_without_sorting_button(driver)

    with allure.step('Нажатие кнопки продолжить без курьера'):
        try:
            element_without_courier_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/button[2]")))
        except:
            assert 0, 'Не нашёл кнопку Без курьера'

        element_without_courier_button.click()

def included_in_consolidation_button(driver):
    production_menu.event_registration_button(driver)

    with allure.step('Нажатие кнопки 79. Включен в консолидацию'):
        try:
            element_included_in_consolidation_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку 79. Включен в консолидацию'

        element_included_in_consolidation_button.click()

    time.sleep(paths.transition_time)

    driver.switch_to.window(driver.window_handles[1])

    with allure.step('Проверка меню'):
        try:
            element_menu_ident = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/p")))
        except:
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            driver.close()
            assert 0,'Не нашёл индентификатора меню'

        if element_menu_ident.text != 'Выберите точку назначения':
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            driver.close()
            assert 0, 'Попал в другое меню'