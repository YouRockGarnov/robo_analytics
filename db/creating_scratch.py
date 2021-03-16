from peewee import PostgresqlDatabase, Database, Proxy, SqliteDatabase
from db.mymodels import *
from db.mymodels import db_proxy
from tools.log import logger, logged
from flask import g

@logged
def init_db():
    '''
    Создает подключение к базе данных, ибо после каждого запроса бд закрывается

    :return:
    '''
    from peewee import PostgresqlDatabase, Database, Proxy, SqliteDatabase
    import os
    if ('DYNO' in os.environ):
        logger.info("'DYNO' in os.environ")

        import urllib.parse as urlparse, os
        urlparse.uses_netloc.append('postgres')
        url = urlparse.urlparse(os.environ["DATABASE_URL"])
        db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname,
                                port=url.port)

        db_proxy.initialize(db)
    else:
        db = SqliteDatabase('sender.sqlite')
        db_proxy.initialize(db)

    db_proxy.close()
    g.db = db_proxy

@logged
def create_or_connect_to_db():
    '''
    Создает базу данных и заполняет таблицу с мессенджерами

    :return:
    '''
    init_db()

    db_proxy.create_tables([Account, Subscription, Messenger, AccessToken, BetaUser, ManagerWaitFor, ManagerToDependent])

    from db.constants import Messenger as messenger_enum
    Messenger.get_or_create(name=messenger_enum.VK.name)[0]
    Messenger.get_or_create(name=messenger_enum.Telegram.name)[0]
    Messenger.get_or_create(name=messenger_enum.WhatsApp.name)[0]

    db_proxy.close()
    return 'DB is created!'


@logged
def reset_db():
    '''
    Удаляет базу данных (и все таблицы, записи и проч.) и создает новую

    :return:
    '''
    init_db()
    db_proxy.drop_tables([Account, Subscription, Messenger, AccessToken, BetaUser])
    create_or_connect_to_db()

    return 'DB is reseted!'

if __name__ == '__main__':
    create_or_connect_to_db()
