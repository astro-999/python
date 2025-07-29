class animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Its %s" % (self.name)
dog = animal('pogo')
print(dog)
print(dog.name)
# class animal:
#     def __init__(self, name):
#         self.name = name
#         # self.__species = 'mammal'  # private attribute
# dog = animal('pogo')

# print(dog.name)
# dog.name ='rocky'
# print(dog.name)
# def showdetails(dog):
#     """Print the details of an animal object"""
#     print(f'name of dog :{dog.name}')
# showdetails(dog)