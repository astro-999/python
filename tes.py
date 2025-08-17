l1 = [1,2,3,4]
# l2 =[5,6,7]
# for i,j in zip(l1,l2) :
#     print(i*j)
# name = ['aarav']
# name1 = ["jagga"]
# for i,j in zip(name,name1):
#     print(i+j)
l2 = []

# for i,j in zip(l1,l1) :
#     print(i*j ,end = ' ')
#     # l2.append(i*j)
# print(l2)

list1 = [1,2,3,3,5,6]
# set(list1)
print(set(list1))

def reverse1(n):
    return n[:-1]

l1 = [(2,1),(7, 5),(1, 4)]
l2 = sorted(l1, key = reverse1)
print(l2)