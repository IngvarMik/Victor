"""усложненная декоратор"""
@decorator1
@decorator2
def f()
    
a = decorator1(decorator2(f)) # вот так работает -- сначала декоратор1 потом декоратор2 а потом функция
