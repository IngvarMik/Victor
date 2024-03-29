"""создание словаря -- пары ключ-значение"""
dict = {"яблоко": "красное","банан": "желтый" , "лимон": "желтый",}# ключ яблоко , значение - красное
""" ключ это то , что стоит слева от двоеточия , значение - стоит справа от двоеточия"""
print(dict)

"""метод keys - это если надо вывести только ключи"""
for k in dict.keys(): #  переменная k в цикле с указанием метода через точку - keys
    print (k) # принт k

""" метод values - это если надо вывести значения"""
for k in dict.values(): #  переменная k в цикле с указанием метода через точку - values
    print (k)

""" метод items - если надо вывести и ключ и значения"""
for k in dict.items(): #  переменная k в цикле с указанием метода через точку - items
    print (k)

""" вывод например нужного значения ключа"""
print(dict["банан"]) # форма записи вывода необходимого значения выбранного ключа

"""изменение значения """
dict["банан"] = "зеленый"
print(dict)

""" удаление элемента словаря - оператор del"""
del(dict["банан"])
print (dict)