class num:
    def __init__(self,a, b):
        self.a=a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
try:
    num1 = int(input('Enter the first number : '))
    num2  = int(input('Enter the second number : '))
    oper = input('Enter the opertaion : ')
    ob1 =num(num1, num2)
    if oper == "+":
        ob1.add()
    elif oper == "-":
        ob1.sub()
    elif oper == '*':
        ob1.mul()
    elif oper == '/':
        ob1.div()
    else:
        raise ValueError("Invalid operator")
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)