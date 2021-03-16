
'''Если LOCAL_MODE включен, то бот не будет отсылать сообщения пользователям и взаимодействовать с ними.

Создано для того, чтобы дебажить на локалке.
НИКОГДА НЕ ЗАГРУЖАЙТЕ НА СЕРВЕР С LOCAL_MODE = True

Если включен DEV_MODE, то все сообщения будут отсылаться с dev-версии бота - https://vk.com/public171438021
'''

DEV_MODE = True
LOCAL_MODE = False

def get_flag_DEV_MODE():
    global DEV_MODE
    return DEV_MODE

def set_flag_DEV_MODE(bool):
    global DEV_MODE
    DEV_MODE = bool

def get_flag_LOCAL_MODE():
    global LOCAL_MODE
    return LOCAL_MODE

def set_flag_LOCAL_MODE(bool):
    global LOCAL_MODE
    LOCAL_MODE = bool
