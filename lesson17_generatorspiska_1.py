""" создание списков генерация"""
s = [] # создаем спсок
for i in range( 1 , 36 ): # условие создания списка от 1 до 21
    if i % 5 == 0: # если i - элемент списка кратен 5 
        s.append(i) # то с помощью append  заносим в список
print(s) # печать списка

""" использование ГЕНЕРАТОРА списка - та же самая программа"""
s1 = [ i for i in range ( 1 , 36 ) if i % 5 == 0] # та же самая прг но в одну строку
print ( s1)

""" возведение в куб каждого числа списка"""
s1 = [ i ** 3 for i in range ( 1 , 36 ) if i % 5 == 0] # ** - возведение в степень - в данном случае куб
print ( s1)
""" сумма всех кубов """
s1 = [ i ** 3 for i in range ( 1 , 36 ) if i % 5 == 0] # 
print (sum (s1)) # сумма кубов
