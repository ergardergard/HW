# Задача 6.1
import random
import array
n = int(input('Задайте размер списка:'))
i = int(input('Задайте начало диапазона:'))
c = int(input('Задайте онец диапазона:'))
mylist = []
for n in range (0,n):
    o = random.randrange(i,c)
    mylist.append(o)
print(mylist)
print(len(mylist))
print(max(mylist))
print(min(mylist))
print(sorted (mylist))
mylist.sort(reverse = True)
print(mylist)





# Задача 6.2
import random
import array
mylist = []
list1 = []
q =0
n = int(input('Задайте размер списка:'))
for n in range (0,n):
    o = random.randrange(0,2)
    mylist.append(o)
print(mylist)
col = mylist.count(0)
print(col)
col1 = mylist.count(1)
print(col1)
for n in range (0,n):
    if 0 in mylist :
        q = mylist.index(0)
        mylist.pop(q)
        mylist.insert(q, 1)
        list1.append(q)
print(list1)




# Задача 6.3
import random
import array
mylist = []
n = int(input('Задайте размер списка:'))
s = int (input('удалить из списка'))
for n in range (0,n):
    o = random.randrange(0,10)
    mylist.append(o)
print(mylist)
for n in range (0,n):
    if s in mylist :
        mylist.remove(s)
print(mylist)
