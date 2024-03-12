#Class- its a blueprint of an object (An Instance of a class)

#How to craete  a class
 #PlayerCharacter is the name of the Class
class PlayerCharacter:  
    
    #Class Object Attribute
    membership = True
    
    #Constructor method, called anytime we instantiate    
    def __init__(self,name='anonymous',age='0'):#Constructor method, called anytime we instantiate
        if (age>18):
            self.name=name #attributes 
            self.age=age
           
    def shout(self):
        print(f'My name is {self.name}')
        
    @classmethod
    def adding_things(cls,num1,num2):
        return num1+num2
        
#creating an instance( calling a class to craeate an object)        
player1=PlayerCharacter("Cindy",20)  


 #accessing the attribute using dot notation
print(player1.adding_things(2,3))  
   
           
         
 
 
  
 
 
 
 
 
 
 