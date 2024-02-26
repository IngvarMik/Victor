"""обьявление класса"""
class House():
    """описание дома - класс это чертеж микрорайона а дома внем, по чертежу построенные - обьекты"""
    def __init__(self , street , number ): # street number -- улица и номер - описание класса для обьекта
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0
    """строить дом"""
    def build(self):
        print ("дом на улице  " + self.street + "  под номером  " + str(self.number) + "  построен")

    """ работа с возрастом дома"""
    def age_of_house(self,year):
        self.age += year
    
        

"""создание обьектов - создание двух обьектов на основе одного класса """
House1 = House( "Московская " , 20) 
House2 = House( " Кленовая" , 21 )

"""выводим-мы хотим знать на какой улице House1. с помощью аргумента street. то есть обращение House1.street"""
print(House1.street)
print(House2.street)
"""то же самое насчет номера- House1.number"""
print(House1.number)
print(House2.number)

"""обращаемся к build то есть хотим узнать в каком состоянии House1 - обращаемся к def build!"""
House1.build()
House2.build()

print(House1.age) # распечака атрибута заданного в начале - age = 0
House1.age_of_house(5) # задали атрибут - 5 лет
print(House1.age) # распечатали теперь

class ProspectHouse(House): #создали дочерний класс  на основе класса House
    def __init__(self , prospect , number):
        super().__init__(self , number)#перенос из родительского класса свойств - super связывает
        self.prospect = prospect # с помощью super мы уже описанные свойства родительского класса пееренесли 

"""теперь создаем обьекты"""
PrHouse = ProspectHouse ( " Кацманавтов" , 37)
print(PrHouse.prospect)
print(PrHouse.number)
        
