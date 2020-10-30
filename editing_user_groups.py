import service_menu
import log_output
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_group(driver):
    if driver == 'ERROR':
        return 'ERROR'

    result = service_menu.editing_user_groups_button(driver)

    if result == 'ERROR':
        return 'ERROR'

    try:
        element_create_new_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]")))
    except:
        log_output.Print('Не нашёл кнопку Создать новую')
        return 'ERROR'

    element_create_new_button.click()

    log_output.Print("Нажал кнопку Создать новую")

    try:
        element_groop_name = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input")))
    except:
        log_output.Print('Не нашёл поля для ввода названия группы')
        return 'ERROR'

    date = datetime.datetime.now()
    name = date.strftime('%Y.%d.%m,%H.%M.%S.test_groop')

    element_groop_name.send_keys(name)

    log_output.Print("Ввёл название группы: " + name)

    try:
        element_save_groop_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]/span")))
    except:
        log_output.Print('Не нашёл кнопку Сохранить')
        return 'ERROR'

    element_save_groop_button.click()

    log_output.Print("Нажал кнопку сохранить")
    return name


def check_for_a_single_group_with_a_similar_name(driver, name):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_find_groop_element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[2]/div/div/div/input")))
    except:
        log_output.Print('Не нашёл строки поиска группы')
        return 'ERROR'

    element_find_groop_element.send_keys(name)

    log_output.Print('Ввёл название группы в поле поиска')

    try:
        element_my_groop = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]")))
    except:
        log_output.Print('Не нашёл созданную группу')
        return 'ERROR'

    if element_my_groop.text != name:
        log_output.Print("Нашёл группу с похожим именем")
        return 'ERROR'

    log_output.Print("Нашёл созданную группу")
    return 'SUCCESS'

def delete_first_groop(driver):
    if driver == 'ERROR':
        return 'ERROR'

    try:
        element_put_a_tick_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/section/section[2]/section/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span")))
    except:
        log_output.Print('Не нашёл поля для выделения группы')
        return 'ERROR'

    element_put_a_tick_button.click()

    log_output.Print('Выделил группу')

    try:
        element_delete_groop_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[4]")))
    except:
        log_output.Print('Не нашёл кнопку Удалить группу')
        return 'ERROR'

    element_delete_groop_button.click()

    log_output.Print('Нажал кнопку Удалить группу')

    try:
        element_delete_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/a[1]")))
    except:
        log_output.Print('Не нашёл кнопку Удалить')
        return 'ERROR'

    element_delete_button.click()

    log_output.Print('Нажал кнопку Удалить')
    return 'SUCCESS'
