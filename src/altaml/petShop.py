from .cat import Cat
from .dog import Dog
from .data import Data

def saveTest():
    cat = Cat("Garfield")
    dog = Dog("Kia")
    
    data = Data("database")
    data.insert("Cat", cat)
    data.insert("Dog", dog)

    
def savePetShop():
    data = Data("database")
    data.beginTran()
    
    try:
        cats = [Cat(),Cat(), Cat()]
        for i in cats:
            data.insert("Cat", i)
        
        dogs = [Dog(), Dog(), Dog()]
        for i in dogs:
            data.insert("Dog", i)
            
        data.commit()
        
    except Exception:
        data.rollback()
        raise

    
def logStats():
    print("saveTest: 2 pets processed 1 Cat and 1 Dog")
    print("savePetShop: 6 pets processed 3 Cats and 3 Dogs")
    print("Total pets processed: 8")

saveTest()
savePetShop()
logStats()