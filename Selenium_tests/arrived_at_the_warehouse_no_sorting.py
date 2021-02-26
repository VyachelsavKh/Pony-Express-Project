import event_registration
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure

def check_menu(driver):
    event_registration.continue_without_courier_button(driver)

    with allure.step('Проверка меню'):
        try:
            element_menu_name_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[1]/h1")))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл название меню'

        if element_menu_name_button.text != '71. Прибыл на склад (без сортировки)':
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Попал не в то меню'

def enter_object_number(driver, number):
    with allure.step('Ввод номера объекта'):
        try:
            element_object_number = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не найдено поле ввода номера объекта'

        element_object_number.send_keys(number)
        element_object_number.send_keys(Keys.RETURN)

def check_error(driver):
    with allure.step('Проверка ошибки'):
        try:
            element_error_message = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/span')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не найдено поле ошибки'

        return element_error_message.text

def check_element_11_1111_1111(driver):
    with allure.step('Проверка наличия накладной'):
        try:
            element_11_1111_1111 = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/p')))
        except:
            return 'ERROR'

        return element_11_1111_1111.text

def delete_element_11_1111_1111(driver):
    with allure.step('Удаление накладной'):
        try:
            element_choose_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/p")))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопки выбора накладной'

        element_choose_button.click()

        try:
            element_delete_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[4]/div[2]/div/div/div/div/div[1]/div[1]/button[1]/span[2]')))
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            assert 0, 'Не нашёл кнопки удаления'

        element_delete_button.click()