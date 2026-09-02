import random

class Dog:

    def __init__(self, name = None):
        self.name = name
        self.age = random.randint(5,10)
        self.favoriteFood = None
        self.history_name=[]
        self.speak_count = 0
        
        if name is not None:
            self.history_name.append(self.name)
        
    def getName(self):
        return self.name    
    
    def getAge(self):
        return self.age
    
    def getFavoriteFood(self):
        return self.favoriteFood
    
    def getNames(self):
        return list(self.history_name)
        
    def getAverageNameLength(self):
        if len(self.history_name) == 0:
            return 0.0
        
        total_len = 0
        for i in (self.history_name):
            current_name = i
            total_len += len(current_name)
            
        return total_len/len(self.history_name)
    
    def setName(self, newName):
        if newName is not None:
            self.history_name.append(newName)
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood
        
    def speak(self,sound = None):
        self.speak_count=self.speak_count+1
        if self.speak_count%5==0:
            self.age+=1
            
        if sound is None :
            print("bark")
        else:
            print(sound)
            
    
        
