
def rectangle_area( a, b):
    return a * b
print(rectangle_area(17 , 14 ))

""" запись этой функции при помощи лямбда"""

print((lambda a , b : a * b)( 17 , 14))

""" еще пример"""

def maximum( a, b):
    if a > b:
        return a
    else:
        return b
print(maximum( 25,17))

"""" ламбда выражение"""

print((lambda a, b : a if a > b else b)( 25 , 17 ))