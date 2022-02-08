# .join()-cборка строки из списка с разделителем
# vowels = ("a", "e", "i", "o", "u")
# vowels_str = ",".join(vowels)
# print("Строка гласных:", vowels_str)
# .strip()- Удаление пробельных символов в начале и в конце строки


# string = ' xoxo love xoxo '
# print(string.strip())
# print(string.strip(' xoe'))
# print(string.strip('stx'))
# string = 'android is awesome'
# print(string.strip('an'))
# string = ' xoxo love xoxo '


# .rstrip()-Удаление пробельных символов в конце строки
# print(string.rstrip())
# print(string.rstrip(' xoe'))
# print(string.rstrip('stx'))
# string = 'android is awesome'
# print(string.rstrip('me'))


# .lstrip()- Удаление пробельных символов в начале строки
# string =' xoxo love xoxo '
# print(string.lstrip())
# print(string.lstrip(' xo'))
# print(string.lstrip('stx'))
# string = 'android is awesome'
# print(string.lstrip('ao'))


# .find()-Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# str1 = "это пример строки....wow!!!"
# str2 = "пример";
# print (str1.find(str2))
# print (str1.find(str2, 4))
# print (str1.find(str2, 10))


# .startswith()-возвращает True, если строка начинается с указанного префикса (строки). Если нет, возвращается False.
# text = "Python is easy to learn."
# result = text.startswith('is easy')
# print(result)
# result = text.startswith('Python is ')
# print(result)
# result = text.startswith('Python is easy to learn.')
# print(result)


# .endswith()-возвращает True, если строка заканчивается с указанного префикса (строки). Если нет, возвращается False.
# text = "Python is easy to learn."
# result = text.endswith('is easy')
# print(result)
# result = text.endswith('to learn.')
# print(result)
# result = text.endswith('Python is easy to learn.')
# print(result)


# .rfind()-Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
# quote = 'Do small things with great love'
# print(quote.rfind('things', 10))
# print(quote.rfind('t', 2))
# print(quote.rfind('o small ', 10, -1))
# print(quote.rfind('th', 6, 20))


# .isalpha()- проверяет состоит и строка из букв
# print('ladno'.isalpha())
