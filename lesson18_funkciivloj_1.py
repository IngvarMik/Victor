import builtins
print(dir(builtins))

"""глобальные функции"""
y = 2
def degree(x):
    return  y ** x
print(degree(4))