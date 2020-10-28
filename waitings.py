import paths
import time


def searching():
    time.sleep(paths.search_time)


def transitioning():
    time.sleep(paths.transition_time)


def visual_checking():
    time.sleep(paths.visual_check_time)

if __name__ == '__main__':
    print('Файл содержит функции ожидания')