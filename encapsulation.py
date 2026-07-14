class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def __age_verification(self, age):
        return True if age >= 18 else False
    

c1 = Person('Peter', 19)
c1.__age = 5
print(f'Age is still {c1.get_age()}')

c1.set_age(5)
print(f'Age is now {c1.get_age()}')

print(c1._Person__age) # NOT RECOMMENDED AS THIS DEFEATS THE PURPOSE OF HAVING ENCAPSULATION