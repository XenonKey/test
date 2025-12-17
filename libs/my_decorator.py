import time
from functools import wraps


def timing(func):
    """Узнаем время выполнения функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(end_time - start_time)
        return result

    return wrapper


