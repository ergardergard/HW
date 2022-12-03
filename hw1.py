# Задча 1:

k = int(input('кол. шаурмы: '))
n = int(input('кол. студентов'))
if (k //n)> 0 :
    print ('кол.целой шаурмы:',k//n)
    a = k//n
    print ('кол.в холодильнике :',k-(a*n))
else :
    print ('кол.в холодильнике :',k)
    
# задча 2:
num = int(input('трехзачное число'))
a = num // 100
b = num // 10 % 10
c = num % 10
print (a,b,c)
print (a,c,b)
print (b,a,c)
print (b,c,a)
print (c,a,b)
print (c,b,a)


# задча 3:
a = int(input('введите время работы'))
b = int(input('введите время работы'))
c = int(input('введите время работы'))
rab = a + b + c
thas = rab // 60
minut = rab - thas * 60
print(thas+10,':',minut)



# задча 4:
Pasw = input('введите пароль : ')
PaswChek = input('Повторите пароль :')
if Pasw == PaswChek:
    print('Пароль принят!')
else:
    print('Пароль не принят! Введённые пароли не совпадают!')
    
    
    
# задча 5:
first = int(input('введите первое число :'))
sec = int(input('введите второе число :'))
if first > sec :
    print (first,'наибольшее число')
    print (sec,'наименьшее число')
elif first < sec :
    print (sec,'наибольшее число')
    print (first,'наименьшее число')
elif first == sec :
    print ('числа равны ')
    
    
 # задча 6:
age = int(input('введите возраст'))
if age >= 18:
    print ('доступ разрешон')
else :
    print ('доступ запрещен')
    
    
     # задча 7:
num = int(input('трехзачное число'))
a = num // 100
b = num // 10 % 10
c = num % 10
if  a > b:
if a > c:
     print(a)
elif b > c:
    print(b)
else :
    print(c)
