# Написать программу, которая преобразует все буквы (русские) в введенной пользователем строке в числа,
# соответствующие позиции этих букв в алфавите.
# Пример:
# Ввод: "а%бв42гд!"
# Вывод: "1%234245!"

# m = m + i == m += i

rus_alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
             'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
s = input()
print(s)
m = ""
for i in s:
    if i in rus_alpha:
        m += str(rus_alpha.index(i) + 1)
    else:
        m += i
    print(m)
