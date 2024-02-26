"""обьединение множеств"""
""" union """
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers2 = {2, 6 , 54, 42 , 3}
numbers3 = numbers.union(numbers2)
print ( numbers3)# и заметь - не содержит дубликаты элементов
""" или такая форма записи - numbers3 = numbers | numbers2"""

""" пересечение множеств метод intersection """
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers2 = {2, 6 , 54, 42 , 3}
numbers3 = numbers.intersection(numbers2)
print(numbers3) # то есть он внес те элементы, которые имеются как в numbers  так и в numbers2
""" или вместо intersection - numbers3 = numbers & numbers2"""