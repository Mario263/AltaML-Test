from .cat import Cat 
from .dog import Dog
from .data import Data 


cat = Cat() 
cat_name = cat.getName()

dog = Dog()
dog_name = dog.getName()

if cat_name is None:
    print("Name is currently ")
else:
    print("Name is currently {0}".format(cat_name))
    
if dog_name is None:
    print("Name is currently ")
else:
    print("Name is currently {0}".format(dog_name))


cat.setName("Garfield")
cat_name = cat.getName()
print("Name has been changed to {0}".format(cat_name))


dog.setName("Kia")
dog_name = dog.getName()
print("Name has been changed to {0}".format(dog_name))


data = Data("database")
data.insert("Cat", cat)
data.insert("Dog", dog)

cat.speak("meow")
dog.speak("bark")