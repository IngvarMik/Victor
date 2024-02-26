"""измерение времени работы функции"""

import time
def my_decor(func):
    def my_wr():
        start_time = time.time()# начальное время
        func()
        print(time.time() - start_time) # конечное время
    return my_wr
@my_decor
def sp():
    spisok = [ i ** 2 for i in range(100) if i % 2 == 0 ] # это цикл -генерация списка четных чисел от 0 до 100
    print(spisok)

sp()