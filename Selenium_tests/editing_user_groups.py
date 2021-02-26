import service_menu
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def create_group(driver):
    service_menu.editing_user_groups_button(driver)

    with allure.step('Нажатие кнопки создать меню'):
        try:
            element_create_new_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div/div/div/div[1]/div[1]/button[1]')))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Создать новую'

        element_create_new_button.click()

    with allure.step('Ввод названия группы'):
        try:
            element_groop_name = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input")))
        except:
            driver.close()
            assert 0, 'Не нашёл поля для ввода названия группы'

        date = datetime.datetime.now()
        name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop')

        element_groop_name.send_keys(name)

    with allure.step('Сохранение группы'):
        try:
            element_save_groop_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]/span")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Сохранить'

        element_save_groop_button.click()

    return name


def check_for_a_single_group_with_a_similar_name(driver, name):
    with allure.step('Поиск группы'):
        try:
            element_find_groop_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="search-input"]')))
        except:
            driver.close()
            assert 0, 'Не нашёл строки поиска группы'

        element_find_groop_element.send_keys(name)

        try:
            element_my_groop = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/section/section[2]/section/section/div/div/div/div[2]/div[2]/div/div[2]/p')))
        except:
            return 'ERROR'

        if element_my_groop.text != name:
            return 'ERROR'

        return 'SUCCESS'

def delete_first_groop(driver):
    with allure.step('Удаление группы'):
        try:
            element_put_a_tick_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span")))
        except:
            driver.close()
            assert 0, 'Не нашёл поля для выделения группы'

        element_put_a_tick_button.click()

        try:
            element_delete_groop_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Удалить группу'

        element_delete_groop_button.click()

        try:
            element_delete_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Удалить'

        element_delete_button.click()