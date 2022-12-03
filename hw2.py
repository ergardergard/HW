    # Задча 1:
num = int(input('введите число: '))
if (10 < num < 22) or (30 < num < 40):
    print ('Точка в множестве')
else :
    print('Точка вне множества')
    
    # Задча 2:
    num1 = int(input('введите число: '))
num2 = int(input('введите число: '))
if (( -5 < num1 <= 0)or (2 < num1 <= 7)) and (( -5 < num2 <= 0)or (2 < num2 <= 7)):
    print ('да')
else :
    print('нет')


    # Задча 3: 
    rast = int(input('введите растояние : '))
vrem = int(input('введите время : '))
if (rast // vrem) < 30 :
    print('медленно')
elif (rast // vrem) < 60 :
    print('средне')
elif (rast // vrem) > 90 :
    print('быстро')
    
    
    # Задча 4: 
    num = int(input('введите трехзанчное число :'))
n = num // 100
u = (num // 10 ) % 10
m = num % 10
if max(n,u,m) - min(n,u,m) == n+u+m-min(n,u,m)-max(n,u,m):
    print ('интересное число ')
else :



   # Задча 5:
    nik = str(input('введите ник-нейм :'))   
    if 3 < len(nik) < 15:
    print ('ник-нейм принят')
elif len(nik) < 3 :
    print ('Ник-нейм должен состоять минимум из 3 символов!')
else:
    print('Ник-нейм может состоять максимум из 15 символов!')   
    
    
      # Задча 6:
    x = float(input('введите x'))
    y = float(input('введите y'))
    if x == 0 or y == 0:
    print ('x и y > 0')
else :
    if x > 0 and y > 0:
        print ('точка в первой четверти ')
        strok1 = str(input('введите первую сторчку'))
        strok2 = str(input('введите вторую строчку'))
        if len(strok1) > len(strok2):
            print (strok2)
        elif len(strok1) == len(strok2):
            print ('сторки равны')
        else :
            print(strok1)
    if x < 0 and y > 0:
        print ('вторая четверть ')
        f = (2 * abs(x) - y)
        f = f / (y**2)
        print(f)
    if x < 0 and y < 0:
        print('третья четверть')
        strok = (input('введите строку'))
        print('(',int(len(strok)*x),',',len(strok)*y,')')
    if x > 0 and y < 0:
        print ('четверая четверть')
        if abs(x) > abs(y):
            print('Координата x – наибольшая по модулю')
        elif abs(x) < abs(y):
            print('Координата x – наибольшая по модулю')
        else:
            print('Координаты равны по модулю')
            
            
           # Задча 7: 
            strok = str(input('введите строку'))
if 'кот' in strok:
    print('Мы погладили кота')
else :
    print('кота нет =(')
