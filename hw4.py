    # задача 4.1
n = int(input('введит натуральное число '))
a = int(input('введит натуральное число '))
b = int(input('введит натуральное число '))
i = 0
x = 0
for x in range (n,0,-1):
    p = 0
    for i in range ((a+1),b):
        c = b - a - 1
    if (not (i == x)) and (x % 2 >0):
    p = p +1
    if p == c:
    print(x)
    
    
    
    
    # задача 4.2 
    com = 0 
    while not (com == ('конец')):
    com = input('введите команду >>>')
    if com == ('лого'):
        logo = input('сторка')
        print (math.log(len(logo)))
    if com == ('триго'):
        grad = float(input('введите градусы '))
        rad = math.radians(grad)
        print (math.sin(rad),math.cos(rad),math.tan(rad),math.cos(rad)/math.sin(rad),sep = '\n')
        
        
        
        
        
         # задача 4.3
          import random
a = random.randint(0, 1000)
b = random.randint(0, 1000)
x = 0

n = int(input('введите число '))
i = 0
for i in range (min(a,b),max(a,b)):
    if i == n :
        x = 1
    else :
        x = x
if x == 1:
    print ('Lucky!')
else :
  
  
  
     # задача 4.4
        import math
import random
i = 0
com = 0

while not(com ==('N')):
    a = int(input('введите натуральное число'))
    b = int(input('введите натуральное число'))
    ran = random.randrange(a, b)
    for i in range (1,ran):
        print(math.log(i,10))
    com = input('Желаете продолжить? Y/N >>>')
    
    
    
    
      # задача 4.5
    import math
n = int(input('введите чило '))
for n in range (1,n):
    if (n % 5)>0:
        print ('Длина окружности с радиусом ',n,':',n * 2 * math.pi)
        print ('Площадь круга с радиусом ',n,':',n**2 * math.pi)
        print ('')
