'''#10 naturaal number
for i in range(1,11):
   print(i)'''

'''#sum of number
num = int(input('Enter the number :'))
sum = 0
n = num +1
for i in range(1,n):
    sum +=i
print(sum)

Num = int(input('Enter the number for multiplication : '))
for i in range (1,11):
   print(f'{Num}*{i}={Num*i}')

#reverse
name = "astro"
print(name[ : :-1])

#rectange
len = int(input('Enter the length : '))
bread = int( input('Enter the breadth :'))
if bread == len :
    print(f'given dimension are of square ')
else:
    print(f'given dimension are of rectangle ')

#greatest
a = int(input(' enter first number : '))
b = int(input(' enter second number : '))
if a   > b :
    print(f'{a} is greater ')
else:
     print(f'{b} is greater ')'''

#oldest age among 3
age1 = int(input('Enter the age of 1st person :'))
age2 = int(input('Enter the age of 2nd person :'))
age3 = int(input('Enter the age of 3rd person :'))

if age1 > age2 and age1 > age3 :
    print('1st person is oldest')
elif age2 > age1 and age2 > age3 :
    print('2nd person is oldest')
elif age3 > age1 and age3 > age2 :
    print('3rd person is oldest')
else:
    print('all have equal age')

age = [age1,age2,age3]
low = 999
high = 0
for i in age :
    if i < low :
        low = i 
    if i > high :
        high = i 
print(f"high is {high}")
print(f'low is {low}')