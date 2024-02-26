import re

s = "qfoh3iybb qjb__  d3340580q2HDKW fpgjg134edw5"
result = re.search(r"[djgjw]", s) # вывел первую же попавшуюся букву из списка в апострофах - j
print(result)

result = re.search(r"[4-8]", s) # выдал поиск первой цифры в диапазоне от 4 до 8 - у нас 4
print(result)

result = re.search(r"[^4-8]", s) #выводит первую букву символ попадающуюся вне диапазона 4-8
print(result)

result = re.search(r"D|f", s) # вывод либо D либо f - что пападется первым - у нас f
print(result)