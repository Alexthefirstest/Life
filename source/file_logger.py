import logging
from functools import wraps


def __init_file_logger():
    fh = logging.FileHandler('logs.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

    file_logger = logging.getLogger('info logger')
    file_logger.setLevel(logging.INFO)
    file_logger.addHandler(fh)

    file_logger.info('logger start')

    return file_logger


__file_logger = __init_file_logger()


def logg_exception_and_print_message(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as ex:
            message = str(ex)
            __file_logger.warning(message)
            print(message)

    return inner
