# задча 3.1:
x = int(input('введите число'))
a = 0
for a in range (1,11):
    print(x,'*',a,'=',x*a)




# задча 3.2:
 x = int(input('задайте количество чисел'))
summ = 0
for a in range (1,(x+1)):
    y = float(input('введите число'))
    summ = y + summ
print('сумма чисел равна:',summ)



# задча 3.3:
x  = input('введте стороку ')
while not(x == ("PRINT")):
    print('id'+ x)
    x  = input('введите строку')
    
    
    
    # задча 3.4:
    x = float(input('введите два числа:'))
y = float(input())
while not(y == 0):
    print(x+y,x-y,x*y,x/y,sep = '\n')
    x = float(input('введите два числа:'))
    y = float(input())
else :
    print('на ноль делить нельзя')
        
        
        
        
       
