# class arav:
#     def hell(self,name):
#         print(f'jagerna arav {name}')
#         print(f'self{self}')
# ob1 = arav()
# ob1.hell('gg')
# ob2 = arav()
# ob2.hell( "us ")
# arav.hell("op")
class arav:
    def __init__(self,name,color):
        print('hii from ja')
        self.name = name
        self.color = color
        
    def show(self):
        print(self.name,self.color)
ob1 = arav('dog','white')
ob2 = arav('cat','blck')
ob1.show()
ob2.show()

