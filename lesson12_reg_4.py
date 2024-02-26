""" квантификаторы"""
import re

s = "lqwhd3678567fekhrKHWBn64673   ::3efm__wekfGR55E64EWs"
result = re.search(r"\d{3}", s )# три раза ищем цифры идущие подряд - у нас 646
print(result)

result = re.search(r"\d{1,3}", s )# вообще непонятная фигня насчет от1 до 3
print(result)

result = re.search(r"\d{4,}", s )# вывод не менее чем 4 подряд идущие цифры
print(result)

result = re.search(r"\d{,4}", s )# вывод не более 4 повторений цифр а чего то не работает
print(result)