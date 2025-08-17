# reverse tuple
"""t1 = ( 0,'arav', 20, 9, 7, 6)
print(t1[::-1])
import sys
#tuple to string 
str1 = ''
for i in t1 :
    if isinstance (i,str):
        str1+= i
    else:
        str1+=str(i)
print(str1)
str3=''.join(str(t1))
print(str3)
print(type(str3))"""
t2 = (1,'arav','shrestha','kind','hi')
# '''print(len(t2))
# print(t2[(len(t2)-2)])
# print( t2[: :-1] )'''
'''if 'arav' in t2 :
    print('found')
else :
    print('not found')'''
list1 =[(20,5,14),(21,4,45),(35,67,23)]
lst =[]
for i in list1 :
    te1 = list(i)
    te1.remove(te1[-1])
    lst.append(tuple(te1))
print(lst)