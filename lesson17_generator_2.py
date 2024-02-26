""" в одну строку все опять"""

print (sum ([ i ** 3 for i in range ( 1 , 36 ) if i % 5 == 0])) # в одну строку все слил

""""""
s = []
for i in range(1 , 21 ):
    for j in range ( 1 , 51 ):
        s.append (( i , j ))
print (s)

s1 = [(i , j ) for i in range (1,21) for i in range(1 , 51)]
print ( s1)