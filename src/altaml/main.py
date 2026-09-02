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
cat.setName("Katherine")

cat_name = cat.getName()
print("Name has been changed to {0}".format(cat_name))
print(cat.getNames())
print(cat.getAverageNameLength())


dog.setName("Kia")
dog.setName("Oscar")

dog_name = dog.getName()
print("Name has been changed to {0}".format(dog_name))
print(dog.getNames())
print(dog.getAverageNameLength())

data = Data("database")
data.insert("Cat", cat)
data.insert("Dog", dog)

cat_age = cat.getAge()
dog_age = dog.getAge()

print("Age of cat before {0}".format(cat_age))
print("Age of dog before {0}".format(dog_age))

for _ in range(5):
    cat.speak()

cat_age = cat.getAge()


for _ in range(5):
    dog.speak()
    
dog_age = dog.getAge()

print("Age of cat after {0}".format(cat_age))
print("Age of dog after {0}".format(dog_age))
