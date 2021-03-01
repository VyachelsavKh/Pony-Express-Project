import request_authorisation
import pytest

'''
Тест-кейс №1. Вход существующего пользователя в систему
1) Ввести правильный логин и пароль - 
    бот зашёл в систему
'''

def test_1():
    request_authorisation.authorisation()
