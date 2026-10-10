import logging


logging.basicConfig(
    filename="Error.log",
    level=logging.ERROR,
    format="%(message)s"
)


def xatolik_yozuvchi_dekorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as xato:
            logging.error(f"Xatolik : {func.__name__} da : {xato}")
            raise
    return wrapper


@xatolik_yozuvchi_dekorator
def bolish(a, b):
    return a / b


try:
    print(bolish(40, 0))
except Exception:
    pass


joriy_user = {"Login": False}


def login_talab(func):
    def wrapper(*args, **kwargs):
        if joriy_user["Login"] == False:
            print("Avval tizimga kiring!")
            return
        return func(*args, **kwargs)
    return wrapper


@login_talab
def user():
    print("Accountingiz ochildi!")


user()






















