# Пользователь вводит n год(а)/лет
# Пример 1:
# Ввод: 2
# Вывод: 2 года
# Пример 2:
# Ввод : 21
# вывод : 21 год
# print(input()[-1])
# print(int(input()) % 10)
x = int(input())
if x % 10 == 1 and x % 100 != 11:
    print(x, "год")
elif x % 10 in {2, 3, 4} and  not (12 <= x % 100 <= 14):
    print(x, 'года')
else:
    print(x, 'лет')

