
import logging

# create logger with 'spam_application'
# logger = logging.getLogger('TodoistVK')
# logger.setLevel(logging.DEBUG)
# # create file handler which logs even debug messages
# fh = logging.FileHandler('bot.log')
# fh.setLevel(logging.DEBUG)
# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# # create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# # add the handlers to the logger
# logger.addHandler(fh)
# logger.addHandler(ch)

from tools.mods import get_flag_LOCAL_MODE

class Logger:
    def info(self, mess):
        print('INFO - {0}'.format(mess))

    def warn(self, mess):
        print('WARN - {0}'.format(mess))

    # show_exc_info == True -> выведет не только сообщение, но и само исключение, которое возникло
    def error(self, mess, show_exc_info=False):
        print('ERROR - {0}'.format(mess))

        if (show_exc_info):
            import sys, traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print(''.join('!! ' + line for line in lines))  # Log it or whatever here

logger = Logger()

def logged(func): # если у метода есть ещё какой-то декоратор - @logged должен быть внизу
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info('Enter to function {0} with args {1} and kwargs {2}'.format(repr(func.__name__), args, kwargs))
            result = func(*args, **kwargs)
            logger.info('Exit from function {0}'.format(repr(func.__name__)))
        except Exception as e:
            if get_flag_LOCAL_MODE():
                raise e
            else:
                logger.error("Fatal error in main loop, args: " + args.__repr__(), show_exc_info=True)
            result = None


        return result

    return wrapper
