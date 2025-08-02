# # from s import su
# # a= input('enter the number')
# # b= input('enter another ')
# # c = su(a,b)
# # print(c)

# age = 3
# try:>back
#     if age<16:
#         raise Exception("you canot drive")
#     print("code for >16 age")
# except Exception as e:
#     print(e)
def add(a,b):
    try:
        print(a+b)
        dis()
    except Exception as e:
        print(e)
def multiply(a,b):
    try:
        print(a*b)
        dis()
    except Exception as e:
        print("error in multiplication",e)
def dis():
    try:
        a= int(input('enter the number'))
        b= int(input('enter another '))
        c =int(input('\n1. for sum \n2.for multiply :'))
        if c==1:
            add(a,b)
        elif c==2:
            multiply(a,b)
        else:
            exit
    except Exception as h:
        print("\nwrong choice ",h)
dis()
