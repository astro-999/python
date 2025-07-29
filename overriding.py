# class Animal:
#     def eat(self):
#         print('meat')
# class Dog(Animal):
#     def eat(self):
#         super().eat() #super().overriding function
#         print("hii")
# obj = Dog()
# obj.eat()

'''_summary_'''

# class Person:
#     def __init__(self,name):
#         self._name=name
#     def show(self):
#         print(self._name)
# class Hari(Person):
#     def show1(self):
#         print('child class')
# h = Hari('ram')
# h.show()
# # print(h.show())  #Parent Class
# h.show1()         #Child Class

class College:
    def __init__(self,name ,address ,phone):
        self._collegeName='acme'
        self._address = 'sitapaila'
        self._contactNo=phone
    def display(self):
        print ("College Name : ",self._collegeName,"\nAddress :",self._address)
        
class Computer(College):
    def __init__(self, name , address , phone ,sem,total_sub):
        self.sem = sem
        self.total_sub = total_sub
        super().__init__(name ,address ,phone)
    def display(self):
        print ("College Name : ",self._collegeName,"\nAddress :",self._address)
        print(f'{self._contactNo}\n{self.sem }\n{self.total_sub}' )

obj = Computer('acme55','ktm',9841,4,6)
obj.display()
print(hasattr(obj,"_collegeName"))
print(getattr(obj,"_collegeName"))
setattr(obj,'total_sub',10)
delattr(obj,"_contactNo")
print(obj._contactNo)