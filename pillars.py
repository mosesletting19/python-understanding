#Enscapulation
class PlayerCharacter:
    def __init__(self, name, age):
       #private variable
        self._name = name
        self._age = age
        
        
    def speak(self):
        print(f"My name is {self._name} and i am {self._age} years old")
        
player1 = PlayerCharacter("Moses Letting", 23)
player1.speak() 
player1.speak='BOOO'

#Abstraction- hiding information and giving what is just necessary
print((1,2,3,1).count(1))   #We don't need to know how the tuple works in order to use this method
                            #The user doesn't care about how it works underneath
"""
In Python, we can achieve encapsulation by using a technique called "Name Mangling". This technique involves prefixing an attribute with double unders
In Python, we can create an abstraction by creating a new class that inherits from another class (or multiple classes), but does not hav
"""
print(player1.speak)


#inheritance

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
    def __init__(self, name,power):
        self.name=name
        self.power=power
        
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
     def __init__(self, name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
     def attack(self):
        print(f'Attacking with Arrows:aroows left- {self.num_arrows}')

wizard1=Wizard('Merlin',50)


wizard1.attack()

#Polymorphism 
archer1=Archer("Arthur",30) 


for char in [wizard1, archer1]:
    char.attack()
    