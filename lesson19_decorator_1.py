"""декоратор"""
def my_decor(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
def my_func():
    print("тут основная функция")
my = my_decor(my_func)# то есть переменная my = my_decor а в ней вызвали my_func
my()# ну и вызвал my .. получиается start  тут основная функция end ... 

"""второй способ декорирования """
def my_decor(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
@my_decor # просто водим собачку с my_decor - результат аналогичен - my_decor -имя декоратора
def my_func():
    print("тут основная функция")
my_func()