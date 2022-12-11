# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 12334
# print(value)

# s = 'hello world'

# print(s)
# print(a,b,s)
# print(a,'-',b,'-',s)
# print('{} - {} - {}'.format(a,b,s))
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3', 1, 2, 4.5, True]
# print(list)

# ist = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# строки
# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print(a, '+' , b, '=', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# натуральные числа
# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+' , b, '=', a+b)

# вещественные числа
# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+' , b, '=', a+b)

# Арифетические операции

# a = 123
# b = 321
# c=a+b
# print(c)

# a = 123
# b = -321
# c=a+b
# print(c)

# a = 12
# b = 5
# c=a/b
# print(c)
# c=a//b
# print(c)

# # возвидение в степень

# a = 2
# b = 8
# c=a**b
# print(c)

# # округление

# a = 1.3
# b = 3
# c= round(a*b,5)
# # где 5 число знаков после запятой
# print(c)

# логические операции

# a = 1 < 4
# print(a)
# b = 1 > 4
# print(b)
# c = 1 < 4 and 5 > 2
# print(c)
# d = 1 == 2
# print(d)
# e = 1 != 2
# print(e)
# f = 1 < 3 < 6 < 10
# print(f)

# a = 'qwe'
# b = 'qwe'
# print(a == b)
# c = [1,2]
# d = [1,2]
# print(c == d)

# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)

# is_odd = f[0] % 2 == 0
# # так пишут в python - is_odd = nit f[0] % 2
# print(is_odd)

# Логические операторы elif else if

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это МАША!')
# elif username == 'Марина':
#     print('Я так ждал Васб Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Логические операторы while

# original = 1234
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(inverted)

# Логические операторы for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'range(1, 10, 2)':
#     print(i)

# Работа со строками

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# # 39

# text = 'съешь ещё этих мягких французских булок'
# print('ещё' in (text))
# # True

# text = 'съешь ещё этих мягких французских булок'
# print(text.isdigit())
# # False являются ли все символы в строке числами

# text = 'съешь ещё этих мягких французских булок'
# print(text.islower())
# # True являются ли все символы в строке символами нижнего регистра

# text = 'съешь ещё этих мягких французских булок'
# print(text.replace('ещё','ЕЩЁ'))
# # Заменить символ в строке

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in (text))
# print(text.isdigit())
# print(text.islower())
# print(text.replace('ещё','ЕЩЁ'))

# for c in text:
#     print(c)

# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# # print(text[len(text)]) IndexError
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10

# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#  print(e) # red green blue

# for e in colors:
#  print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый многократно

# def function_name(x):
# body line 1

def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType