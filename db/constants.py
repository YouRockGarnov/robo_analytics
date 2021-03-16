from enum import Enum

# если будете менять имена тут, то загляните в репозиторий todoist-swither, там они захардкожены
# так надо, см. services.TodoistService.get_auth_url - там будет state, куда это пихается
class Messenger(Enum):
    VK = 1
    Telegram = 2
    WhatsApp = 3

class Service(Enum): # todo сервисы тоже имеют имя в своих классах. как бы с этими путаницы не возникло
    Todoist = 1
    Trello = 2
