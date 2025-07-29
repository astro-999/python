#__ variable name  = private
#_variable name = protected
public = "This is a public variable."
class MyClass:
    def __init__(self,name):
        self.__name = name
    def set_name(self,name):#set function
        self.__name = name
if __name__ == '__main__':
    obj = MyClass('arav')
    print(obj._MyClass__name) #accessing outside the class
    obj.set_name("Arav") # using set function 
    print(obj._MyClass__name)
    obj.set_name('Bukkie')
    print(obj._MyClass__name)
    public = 'hi'
    print(public)