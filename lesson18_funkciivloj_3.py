"""вложенная функция"""
def degree(x): # функция 
    y = 2 # локальная переменная
    def degree_two(): # вложенная функция
        return y ** x # возврат y  в степени x
    return degree_two() # возврат функции 
print(degree(4)) # печать результата при degree x = 4

"""инкапсуляция - защита функции"""
def message(number):
    def print_message():
        return ' Число ' + str(number)
    return print_message()
print(message(78))
print(print_message()) # уже ругается - он не видит print_message - так как спрятан print_message внутри def print_message
