""" разница между множествами"""
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers2 = {2, 6 , 54, 42 , 3}# содержатся в numbers но не содержатся в numbers2
numbers3 = numbers - numbers2
print(numbers3)

""" или так к примеру - содержатся в numbers2 и не содержатся в nombers"""
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers2 = {2, 6 , 54, 42 , 3}
numbers3 = numbers2 - numbers
print(numbers3)

""" метод copy - скопировать элементы из одного множества в другое"""
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers2 = {2, 6 , 54, 42 , 3}
numbers3 = numbers2.copy()
print(numbers3)

""" метод len - возвращение длины количества элементов множества"""
print(len(numbers3)) # это количество элементов после последней операции - когда copy делали
"""frozenset - замороженное множество - на нем метод add не работает"""