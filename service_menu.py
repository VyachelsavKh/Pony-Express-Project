import main_page
import paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

def service_button(driver):
    main_page.menu_button(driver)

    with allure.step('Нажатие кнопки сервис'):
        try:
            element_service_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(7) .bp3-text-overflow-ellipsis")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Сервис'

        element_service_button.click()

def permissions_management_button(driver):
    service_button(driver)

    with allure.step('Нажатие кнопки Управление разрешениями'):
        try:
            element_permissions_management_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-popover-content:nth-child(1) .bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Управление разрешениями'

        element_permissions_management_button.click()

def editing_user_groups_button(driver):
    permissions_management_button(driver)

    with allure.step('Нажатие кнопки Группы пользователей'):
        try:
            element_group_of_users_button = WebDriverWait(driver, paths.search_time).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "li:nth-child(1) > .bp3-menu-item > .bp3-text-overflow-ellipsis")))
        except:
            driver.close()
            assert 0, 'Не нашёл кнопку Группы пользователей'

        element_group_of_users_button.click()

    with allure.step('Определение меню'):
        try:
            element_editing_user_groups = WebDriverWait(driver, paths.search_time).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div/h1")))
        except:
            driver.close()
            assert 0, 'Не нашёл идентификатор меню'

        if element_editing_user_groups.text != 'Редактирование групп пользователей':
            driver.close()
            assert 0, "Попал в другое меню"