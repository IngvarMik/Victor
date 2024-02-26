""" kwarg для именованных аргументов"""
def brand ( **brands): # тут уже ставятся ** и название тож любое - обозначение этих функций - это звездочки
    print ( brands) # 
brand( a = "Apple" , s = " Samsung")

""" или так """
def brand ( **brands): # печать столбцом - при помощи items
    for x , y in brands.items():
        print( x , ':'  , y)
    
brand( a = "Apple" , s = " Samsung") 