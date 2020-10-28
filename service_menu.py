import main_page
import paths
import log_output
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def service_button(driver):
    result = main_page.menu_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_service_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-submenu:nth-child(7) .bp3-text-overflow-ellipsis")))
    except:
        log_output.Print('Не нашёл кнопку Сервис')
        return 'ERROR'

    element_service_button.click()

    log_output.Print("Нажал кнопку Сервис")
    return 'SUCCESS'

def permissions_management_button(driver):
    result = service_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_permissions_management_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".bp3-popover-content:nth-child(1) .bp3-submenu:nth-child(1) .bp3-text-overflow-ellipsis")))
    except:
        log_output.Print('Не нашёл кнопку Управление разрешениями')
        return 'ERROR'

    element_permissions_management_button.click()

    log_output.Print("Нажал кнопку Управление разрешениями")
    return 'SUCCESS'

def editing_user_groups_button(driver):
    result = permissions_management_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_group_of_users_button = WebDriverWait(driver, paths.search_time).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li:nth-child(1) > .bp3-menu-item > .bp3-text-overflow-ellipsis")))
    except:
        log_output.Print('Не нашёл кнопку Группы пользователей')
        return 'ERROR'

    element_group_of_users_button.click()

    log_output.Print("Нажал кнопку Группы пользователей")

    try:
        element_editing_user_groups = WebDriverWait(driver, paths.search_time).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/section[2]/section/div/h1")))
    except:
        log_output.Print('Не нашёл идентификатор меню')
        return 'ERROR'

    if element_editing_user_groups.text != 'Редактирование групп пользователей':
        log_output.Print("Попал в другое меню")
        return 'ERROR'
    else:
        log_output.Print("Попал в меню Редактирование групп пользователей")
        return 'SUCCESS'