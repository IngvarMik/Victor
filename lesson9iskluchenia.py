""" исключения """
try: # все это затевается чтобы исключить возможность деления на ноль
    a = int(input(" a: "))
    b = int(input(" b: "))
    print(a/b)
except ZeroDivisionError: # признак деления на ноль(ZeroDivisionError)
    print(" на ноль делить нельзя")
