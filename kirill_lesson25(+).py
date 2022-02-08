# Написать программу, которая выводит,
# какие элементы и сколько раз встретились в введённой пользователем строке.
# Пример:
# Ввод: "рьппвьь"
# Вывод: {"р": 1, "ь": 3, "п": 2, "в": 1}

# ctrl + / == comment

# Ladno = {}
# for i in input():
#     if i in Ladno:
#         Ladno[i] += 1
#     else:
#         Ladno[i] = 1
# print(Ladno)

# print(sorted(list("йцукенгшщзхъфывапролджэячсмитьбю")))
s = {}
for i in "йцукенгшщзхъфывапролджэячсмитьбю":
    s[i] = 0
print(s)

for i in "рьппвьь":
    s[i] += 1

for elem in s:
    if s[elem]:
        print(elem, s[elem])
