#Задание 7.1
import random
n=int(input('Введите колличество случайных чисел >>>'))
for i in range (n):
    k = random.randint(1000,10000)
    myfile = open('HW7_1.txt','a+')
    myfile.write(str(k)+'\n')
    myfile.close()
myfile = open("HW7_1.txt", "r")
file_contents = myfile.read()
myfile.close()
print(file_contents)



#Задание 7.2
import HW7_2math
a = float(input('Введите начало аргумента x >>>'))
b = float(input('Введите конец аргумента x >>>'))
h = float(input('Введите шаг >>>'))
while (a<=b):
    y=a*math.log(1+math.sin(math.radians(a))/a)/(a+math.sin(math.radians(a)))
    a+=h
    with open('HW7_2.txt', encoding='utf-8', mode='a+') as myfile:
        myfile.write('При x, равном '+str(a-h)+': y ='+str(y) + '\n')
with open('HW7_2.txt', encoding='utf-8', mode='r') as myfile:
    file_contents = myfile.read()
print(file_contents)




#Задание 7.3
text = ''
while (0==0):
    text = input('Введите слово >>>')
    if text.upper() == 'И ТД':
        break
    else:
        with open('HW7_3.txt', encoding='utf-8', mode='a+') as myfile:
            myfile.write(text+'\n')
with open('HW7_3.txt', encoding='utf-8', mode='r') as myfile:
    file_contents = myfile.read().splitlines()
print(file_contents)
print('I receive', random.choice(file_contents),'\nYou receive', random.choice(file_contents))
