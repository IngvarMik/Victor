"""замыкание"""
def message(x):
    def print_message(y):
        return x , y
    return print_message

d = message(4) # судя по ответу - 4 сохранилась , а не удалилась ,как это было бы в обычной ситуации
print(d)

"""эксперимент """
def message(x):
    def print_message(y):
        return x , y
    return print_message

d = message(4) # как видно тз результата он 4 запомнил и еще дал 8
print(d(8)) # как итог - это запоминание нашего целого числа четыре 
print(d(22)) # опять - видим что он 4 все равно  запомнил а 8 сменил на 22
"""все это называется сохранением состояния"""