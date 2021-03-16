from flask import g, Flask, request
import json
from tools.log import logged
from db.creating_scratch import init_db, db_proxy
import db.creating_scratch as creating_scratch
from db.mymodels import Message, Event, Subscription, Account

app = Flask(__name__) # главное приложение

@app.route('/', methods=['GET'])
def describe():
    return 'Это бот для создания аналитики для RoboManager'

@app.before_request
@logged
def before_request():
    '''
    Перед запросом нужно сделать у бд connect
    :return:
    '''

    if 'db' not in g:
        init_db()
        g.db = db_proxy

    g.db.connect(True)

@app.after_request
@logged
def after_request(response):
    '''
    После закрыть бд, а то мало ли
    :param response:
    :return:
    '''
    g.db.close()
    return response

@app.route('/put_event', methods=['POST'])
def put_event():
    data = json.loads(request.data)
    account = Subscription.get(messenger_user_id=data['user_id'])
    Event.create(account=account, type=data['type'], datetime=data['datetime'])

@app.route('/put_message', methods=['POST'])
def put_message():
    data = json.loads(request.data)
    account = Subscription.get(messenger_user_id=data['user_id'])

    Message.create(account=account, datetime=data['datetime'], text=data['text'], direction=data['direction'])

if __name__ == "__main__":
    creating_scratch.create_or_connect_to_db()
    app.run(debug=True, threaded=True) # запускает приложение
