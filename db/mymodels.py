from peewee import Model
from peewee import IntegerField, BigIntegerField
from peewee import ForeignKeyField
from peewee import TextField
from peewee import TextField
from peewee import PostgresqlDatabase, Proxy
from peewee import DateTimeField
from datetime import datetime

db_proxy = Proxy()

def see_elem_in_all_tables():
    query = Account.select()

    print('Accounts:')
    for acc in query:
        print(acc.id, acc.login, acc.password)
    print()

    query = Subscription.select()

    print('Subscriptions:')
    for sub in query:
        print(sub.id, sub.account, sub.subscr_type, sub.messenger_user_id)
    print()

    print('Messengers:')
    query = Messenger.select()
    for messenger in query:
        print(messenger.id, messenger.name)

    print('ManagerToDependent:')
    query = ManagerToDependent.select()
    for mtod in query:
        print(mtod.manager.id)
        print(mtod.dependent.id)

class DBModel(Model):
    class Meta:
        database = db_proxy

class Account(Model):
    login = TextField()
    password = TextField()

    class Meta:
        database = db_proxy

class Messenger(Model):
    name = TextField()
    # cost = IntegerField()

    class Meta:
        database = db_proxy

class Subscription(Model):
    account = Foreig    nKeyField(Account, to_field='id', null=True)
    messenger = ForeignKeyField(Messenger, to_field='id')
    messenger_user_id = BigIntegerField()
    messenger_username = TextField()

    class Meta:
        database = db_proxy

class ManagerToDependent(DBModel):
    manager = ForeignKeyField(Account, to_field='id')
    dependent = ForeignKeyField(Account, to_field='id')

class Message(DBModel):
    account = ForeignKeyField(Account, backref='id')
    datetime = DateTimeField()
    text = TextField()
    direction = TextField() # from, to

class Event(DBModel):
    account = ForeignKeyField(Account, backref='id')
    type = TextField()
    datetime = DateTimeField()
