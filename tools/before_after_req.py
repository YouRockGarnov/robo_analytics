# from flask import g
# from db.creating_scratch import init_db, db_proxy
# from tools.log import logged
# from globals import app
#
# @logged
# def before_request():
#     with app.app_context():  # без этого вроде нельзя использовать g
#         if 'db' not in g:
#             init_db()
#             g.db = db_proxy
#
#         g.db.connect(True)
#
# @logged
# def after_request():
#     with app.app_context():  # без этого вроде нельзя использовать g
#         g.db.close()