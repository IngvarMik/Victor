import re
s = "8282568-+  kahfKHHD;:Kw'ocvc344"
result = re.search (r"\D", s) # вывод любого символа сразу после цифры - ответ match пропускает цифры 
"""и выводит первый символ сразу после цифры"""
print ( result)

result = re.search (r"\s", s) # это любой пробельный символ, т е сразу первыл пробел
print ( result)

result = re.search (r"\S", s) # любой непробельный символ - в нашем случае 8
print ( result)

result = re.search (r"\w", s) # любая первая буква, цифра или нижнее подчеркивание
print ( result)