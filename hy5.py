# Задача 5.1
n = int(input('кол строк '))
str2 = ('')
for n in range (0,n):
    str1 = input('введите строку')
    def first1(str1):
        return str1.title()[:1]
    str2 = (str2 + first1(str1))
print(str2)




# Задача 5.2
str1 = input('введите строку ')
print(len(str1))
def first1(str1):
    return str1[:1]
print(first1(str1))
n = len(str1)
i = n
p = 0
str2 = ''
str3 = ''
str4 = ''
def firstL(str1):
    return str1[n-1:n]
print(firstL(str1))
for n in range (0,n):
    p = i -n
    def firstO(str1):
        return str1[p-1:p]
    str2 = str2 + (firstO(str1))
print(str2)
for n in range(0,n+2):
    if n % 2 == 0:
        def firstH(str1):
            return str1[n-1:n]
        str3 = str3 +firstH(str1)
    else:
        def firstH(str1):
            return str1[n-1:n]
        str4 = str4 +firstH(str1)
print(str3)
print(str4)




# Задача 5.3
str1 = input('введите строку ')
s = len(str1)
p = 0
i = 0
let = ''
if str1.isdigit() == 1:
    for s in range (1,s+1):
        def ans(str1):
            return str1[s-1:s]
        print(ans(str1) + '0')
elif str1.isalpha():
    for let in (str1):
        if let == 'q':
            i = 1 + i
    print(i)
elif str1.isalnum() == 0:
    for let in str1:
        p = p + 1
        if let.isalnum() == 0:
            print(p-1)
            
            
            
            
  # Задача 5.4      
  stop = ''
while not(stop == ('stop')):
    str1 = input('введите строку ')
    if str1.isdigit():
        print('цифровая строка ')
    elif str1.isalpha():
        print('Буквенная строка')
    elif str1.isalnum():
        print('Смешаная сторка ')
    stop = input('Продолжим???')
