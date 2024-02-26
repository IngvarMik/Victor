import re
s = "whfwk4rh+34  =+ 54098423 dknnn332;k"
result = re.search (r"\W", s) # вывод ни буквы ни цифры ни нижнего подчеркивания
print ( result)

result = re.search (r"\bdknn", s) # символ b - и после него указываю ну скажем 4 буквы начала искомого слова
print ( result)

result = re.search (r"\Bdknn", s) # а это - середина слова но у нас начало dknn а слева проьел поэтому none
print ( result)

result = re.search (r"\d+", s) # первая цифра которая встречается в строке
print ( result)