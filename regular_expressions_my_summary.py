import re
# Изучаем универсальный язык регулярных выражений
# ссылки:
# 1) статья https://tproger.ru/translations/regular-expression-python/
# 2) туториал на Ютубе https://www.youtube.com/watch?v=1SWGdyVwN3E&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=1
# 3) отладчик рег выражений https://regex101.com/
# ----------------------------- спецсимволы -----------------------------
# ● .	    Один любой символ, кроме новой строки \n.
# ● ?	    0 или 1 вхождение шаблона слева
# ● +	    1 и более вхождений шаблона слева
# ● *	    0 и более вхождений шаблона слева
# ● \w	    Любая цифра или буква (\W — все, кроме буквы или цифры)
# ● \d	    Любая цифра [0-9] (\D — все, кроме цифры)
# ● \s	    Любой пробельный символ (\S — любой непробельный символ)
# ● \b	    Граница слова
# ● [..]    Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# ● \	    Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ● ^ и $	Начало и конец строки соответственно
# ● {n,m}	От n до m вхождений ({,m} — от 0 до m)
# ● a|b	    Соответствует a или b
# ● ()	    Группирует выражение и возвращает найденный текст
# ● \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно


# ---------------------------------- Флаги ----------------------------------
# ● re.A, re.ASCIIASCII - диапазон символов вместо Юникода
# ● re.U, re.UNICODE - Использование диапазонов Юникода. Работает по умолчанию, можно не назначать
# ● re.I, re.IGNORECASE - Игнорировать регистр символов
# ● re.M, re.MULTILINE - Разбивать текст на строки при обработке. Нужен, в основном, для функций re.match и re.search
# ● re.S, re.DOTALL - По умолчанию символ точки означает любой символ, кроме символа новой строки \n.
# Если назначить этот флаг, ограничение снимается


# ---------------------------------- Методы ----------------------------------
# ||||||||||||||||||||||| re.match(pattern, string) ||||||||||||||||||||||||||
# Этот метод ищет по заданному шаблону в начале строки. Например, если мы вызовем
# метод match() на строке «AV Analytics AV» с шаблоном «AV», то он завершится
# успешно. Однако если мы будем искать «Analytics», то результат
# будет отрицательный. Давайте посмотрим на его работу:
result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result)
#  мы получаем <re.Match object; span=(0, 2), match='AV'> где
# <re.Match object> - это название питоновского объекта
# <span=(0, 2)> - это границы того паттерна, который мы ищем, в данном случае он находится с 0 до 2 символа не включ.
#  <match='AV'> - само соответствие
# Искомая подстрока найдена. Чтобы вывести ее содержимое, используем
# метод group(). (Мы используем «r» перед строкой шаблона, чтобы показать,
# что это «сырая» строка в Python).
result2 = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result2.group(0))  # можно и без 0 просто написать print(result2.group())

# Теперь попробуем найти «Analytics» в данной строке. Поскольку строка начинается
# на «AV», метод вернет None:
result3 = re.match(r'Analytics', 'AV Analytics Vidhya AV')
# print(result3)


# ||||||||||||||||||||||| re.search(pattern, string) |||||||||||||||||||||||
# Этот метод похож на match(), но он ищет не только в начале строки. В отличие
# от предыдущего, search() вернет объект, если мы попытаемся найти «Analytics».
# Метод search() ищет по всей строке, но возвращает только первое найденное совпадение.
result4 = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# Внимание! Тут для вывода конкретной инфо тоже нужен метод group()
# print(result4)  # получаем тоже <re.Match object; span=(3, 12), match='Analytics'>
# print(result4.group(0))  # можно и без 0 просто написать print(result2.group())


# ||||||||||||||||||||||| re.findall(pattern, string) |||||||||||||||||||||||
# Этот метод возвращает список всех найденных совпадений. У метода findall() нет
# ограничений на поиск в начале или конце строки. Если мы будем искать «AV»
# в нашей строке, он вернет все вхождения «AV». Для поиска рекомендуется
# использовать именно findall(), так как он может работать и как re.search(), и как re.match().
result5 = re.findall(r'AV', 'AV Analytics Vidhya AV')
# print(result5)


# ||||||||||||||||||||||| re.split(pattern, string, [maxsplit=0]) |||||||||||||||||||||||
# Этот метод разделяет строку по заданному шаблону.
#  В примере мы разделим слово «Analytics» по букве «y».
result6 = re.split(r'y', 'Analytics')
# print(result6)

# Метод split() принимает также аргумент maxsplit со значением по умолчанию, равным 0. В данном
# случае он разделит строку столько раз, сколько возможно, но если указать этот аргумент, то
# разделение будет произведено не более указанного количества раз.
result7 = re.split(r'i', 'Analytics Vidhya')
# Мы установим параметр maxsplit равным 1, и в результате строка будет разделена на две
# части вместо трех.
result8 = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
# print(result7)
# print(result8)


# ||||||||||||||||||||||| re.sub(pattern, repl, string) |||||||||||||||||||||||
# Этот метод ищет шаблон в строке и заменяет его на указанную подстроку.
# Если шаблон не найден, строка остается неизменной.
result9 = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
# print(result9)


# ||||||||||||||||||||||| re.compile(pattern, repl, string) |||||||||||||||||||||||
# Мы можем собрать регулярное выражение в отдельный объект, который может
# быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.
pattern_ = re.compile('AV')
result_ = pattern_.findall('AV Analytics Vidhya AV')
result_2 = pattern_.findall('AV is largest analytics community of India')
# print(result_)
# print(result_2)
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# Примеры использования регулярных выражений

# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 1: Вернуть первое слово из строки
# Сначала попробуем вытащить каждый символ (используя .)
_result = re.findall(r'../../../netology_http_10', 'AV is largest Analytics community of India')
# print(_result)

# Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.
_result2 = re.findall(r'\w', 'AV is largest Analytics community of India')
# print(_result2)

# Теперь попробуем достать каждое слово (используя * или +)
_result3 = re.findall(r'\w*', 'AV is largest Analytics community of India')
# print(_result3)

# И снова в результат попали пробелы, так как * означает «ноль или более
# символов». Для того, чтобы их убрать, используем +:
_result4 = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print(_result4)

# Теперь вытащим первое слово, используя ^:
_result5 = re.findall(r'^\w+', 'AV is largest Analytics community of India')
# print(_result5)

# Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
_result6 = re.findall(r'\w+$', 'AV is largest Analytics community of India')
# print(_result6)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 2: Вернуть первые два символа каждого слова
# Вариант 1: используя \w, вытащить два последовательных
# символа, кроме пробельных, из каждого слова:
__result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
# print(__result)

# Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):
__result2 = re.findall(r'\b\w.', 'AV is largest Analytics community of India')
# print(__result2)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 3: вернуть список доменов из списка адресов электронной почты
# Давайте снова рассмотрим решение пошагово. Сначала вернем все символы после «@»:
__result3 = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, '
                                'test.first@analyticsvidhya.com, first.test@rest.biz')
# print(__result3)

# Как видим, части «.com», «.in» и т. д. не попали в результат. Изменим наш код:
__result4 = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, '
                                    'test.first@analyticsvidhya.com, first.test@rest.biz')
# print(__result4)

# Второй вариант — вытащить только домен верхнего уровня, используя группировку — ( ):
__result5 = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, '
                                      'test.first@analyticsvidhya.com, first.test@rest.biz')
# print(__result5)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 4: Извлечь дату из строки
# Используем \d для извлечения цифр.
__result6 = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print(__result6)

# Для извлечения только года нам опять помогут скобки:
__result7 = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print(__result7)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 5: Извлечь все слова, начинающиеся на гласную
# Для начала вернем все слова:
__result8 = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print(__result8)

# А теперь — только те, которые начинаются на определенные буквы (используя []):
__result9 = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print(__result9)

# Выше мы видим обрезанные слова «argest» и «ommunity». Для того, чтобы убрать
# их, используем \b для обозначения границы слова:
result__ = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print(result__)

# Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:
result__2 = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print(result__2)

# В результат попали слова, «начинающиеся» с пробела. Уберем их, включив пробел
# в диапазон в квадратных скобках:
result__3 = re.findall(r'\b[^aeiouAEIOU ]\w+', 'AV is largest Analytics community of India')
# print(result__3)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 6: Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)
# У нас есть список телефонных номеров, и нам нужно проверить их, используя регулярные выражения:
lst = ['9999999999', '999999-999', '99999x9999']
# # print(re.match(r'[8-9]{1}[0-9]{9}', lst[0]))  # <re.Match object; span=(0, 10), match='9999999999'>
# for i in lst:
#     if re.match(r'[8-9]{1}[0-9]{9}', i) and len(i) == 10:
#         print(f'{i} - yes')
#     else:
#         print(f'{i} - no')


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 7: Разбить строку по нескольким разделителям
# Возможное решение:
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
_my_result = re.split(r'[;,\s]', line)
# print(_my_result)

# Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:
line2 = 'asdf fjdk;afed,fjek,asdf,foo'
_my_result2 = re.sub(r'[;,\s]', ' ', line2)
# print(_my_result2)


# ` ` ` ` ` ` ` ` ` ` ` `
# Задача 8: Извлечь информацию из html-файла
# Допустим, нам надо извлечь информацию из html-файла, заключенную между
# <td> и </td>, кроме первого столбца с номером. Также будем считать,
# что html-код содержится в строке.
# Пример содержимого html-файла:
test_str = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
# Решение:
_my_result3 = re.findall(r'\d([A-Z][a-z]+)([A-Z][a-z]+)', test_str)
# print(_my_result3)

# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# Занятия с https://www.youtube.com/watch?v=1SWGdyVwN3E&list=PLA0M1Bcd0w8w8gtWzf9YkfAxFCgDb09pA&index=1
# Регулярные выражения #1: литералы и символьный класс

# начальный пример
text = 'Карта map и объект bitmap - это разные вещи'
match = re.findall('map', text)  # пришем что искать, где искать
# print(match)


# теперь мы хотим найти только отдельное слово "map", а не "map" в нутри чего-либо
text2 = 'Карта map и объект bitmap - это разные вещи'
match2 = re.findall('\\bmap\\b', text2)  # пришем что искать, где искать
# Но есть и более простой вариант с одинарными слэшами, если перед строкой мы поставим букву 'r'
match_2 = re.findall(r'\bmap\b', text2)
# print(match2)
# print(match_2)


# Чтобы эти спецсимволы в тексте распознавались не как спецсимволы, а как символы текста, используем \
text3 = 'еда, беда, победа'
match3 = re.findall(r'\(еда\)', text3)  # пришем что искать, где искать
text4 = '(еда), беда, победа'
match4 = re.findall(r'\(еда\)', text4)
# print(match3)  # и видим, что в тексте нигде нет круглых скобок
# print(match4)  # а здесь мы их уже, наоборот, находим


# спецсимволы также в тексте буду таспознаны как бычный текст, есть мы это запишим так
text_ = 'Карта map и, -4 56 объек?*.т'
match_ = re.findall(r'[?*.]', text_)
# print(match_)


# переберем различные варианты написания
text5 = 'Еда, беду, победа'
match5 = re.findall(r'[еЕ]д[ау]', text5)
# print(match5)


# цифры
# в усл. задано, что нужно искать только там, где 2 символа подряд, поэтому получаем ['56']
text6 = 'Карта map и 4 56 объект'
match6 = re.findall(r'[0123456789][0123456789]', text6)
# print(match6)

# в тексте нет двух цифр подряд, поэтому получаем []
text7 = 'Карта map и 5 5 объект'
match7 = re.findall(r'[0123456789][0123456789]', text7)
# print(match7)

# выведет все цифры по одиночке ['2', '3', '4', '5', '5', '6', '4', '5', '6', '7', '6', '4']
text8 = 'Карта map и      234 556  456   764  объект'
match8 = re.findall(r'[0123456789]', text8)
# print(match8)

# выведет по 2 первых цифры из каждого цифросочетания
text9 = 'Карта map и      234 556  456   764  объект'
match9 = re.findall(r'[0123456789][0123456789]', text9)
# print(match9)

# можно заменить [0123456789][0123456789] на [0-9][0-9]
text10 = 'Карта map и      234 556  456   764  объект'
match10 = re.findall(r'[0-9][0-9]', text10)
# print(match10)

text11 = 'Карта map и 56 объект'
match11 = re.findall(r'[0-9][0-9]', text11)
# print(match11)  # находим 2 цифры подряд ['56']

# если нужно будет написать -
text12 = 'Карта map и, -4 56 объект'
match12 = re.findall(r'[-0-9][0-9]', text12)
# print(match12)

# инвертируем
text13 = 'Карта map и, -4 56 объект'
match13 = re.findall(r'[^0-9]', text13)
# print(match13)


# получаем все маленькие буквы
text14 = 'Карта map и, -4 56 объект'
match14 = re.findall(r'[а-я]', text14)
# print(match14)


# получаем и маленькие, и большие буквы
text15 = 'Карта map и, -4 56 объект'
match15 = re.findall(r'[а-яА-Яa-z0-4]', text15)
# print(match15)


# получаем все цифры
text16 = 'Карта map и, -4 56 объект'
match16 = re.findall(r'\d', text16)
# print(match16)


# получаем все, кроме \n
text17 = 'Карта map и, -4 56 объект'
match17 = re.findall(r'../../../netology_http_10', text17)
# print(match17)


# получаем все, кроме символы букв и цифр
text18 = 'Карта map и, -4 56 объект'
match18 = re.findall(r'\w', text18)
# print(match18)


# пример использования флага re.ASCII для вывода только латинских букв и цифр
text19 = 'Карта map и, -4 56 объект'
match19 = re.findall(r'\w', text19, re.ASCII)
# print(match19)
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# ___________________________________________________________________________
# Регулярные выражения #2: квантификаторы {m,n}, +, * , ?
# {m,n} m - минимальное, n - максимальное число совпадений с выражением
# пример жадного мажорного квантификатора
_text = 'Google, Gooogle, Goooooogle'
_match = re.findall(r'o{2,5}', _text)
# print(_match)  # квантификатор по умолчанию находит самые длинные последовательности


# # пример минорного квантификатора
# _text2 = 'Google, Gooogle, Goooooogle'
# _match2 = re.findall(r'o{2,5}?', _text2)
# print(_match2)


# краткие формы записи квантификаторов
# для всех этих форм можно использовать и минорный режим
# ● {m} - повторение выражения ровно m раз (эквивалент {m,m})
# ● {m,} - повторение от m и более раз
# ● {,n} - повторение не более n раз


_text3 = 'Google, Gooogle, Goooooogle'
_match3 = re.findall(r'Go{2,}gle', _text3)
# print(_match3)  # ['Google', 'Gooogle', 'Goooooogle']


_text4 = 'Google, Gooogle, Goooooogle'
_match4 = re.findall(r'Go{,4}gle', _text4)
# print(_match4)  # ['Google', 'Gooogle']


phone = '89123456789'
_match5 = re.findall(r'8\d{10}', phone)
# print(_match5)  #


# если уберем 1 цифру, то так работать уже не будет, так как мы запрашиваем именно 10 цифр
phone6 = '8912345678'
_match6 = re.findall(r'8\d{10}', phone6)
# print(_match6)  # []


# в программировании эти 2 квантификатора ({0,} и {1,}) встречаются довольно часто
# так что им придумали сокращенное написание: * это {0,}, + это {1,}
# также есть квантификатор ? - от 0 до 1 (аналог {0,1}
# все они могут использоваться и в минорном режиме: ??, *?, +?


# мы хотим выделить оба слова
_text7 = 'стеклянный, стекляный'
_match7 = re.findall(r'стеклянн?ый', _text7)  # в данном случае конструкция н? говорит,
# что вторая буква "н" у нас необязательна, она может быть от 0 до 1
# print(_match7)


# пропарсим данный текст
_text8 = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001'
_match8 = re.findall(r'\w+\s*=\s*[^;]+', _text8)
# \w+ символов слова должно быть от 1 и до сколько есть
# \s*=\s* должен стоять знак равно, но перед ним и после него могут быть пробелы
# [^;]+ затем мы выделяем все слова кроме ';', то есть мы используем символьный класс с
# инвертацией. И все это будем перебирать от единицы и более
# print(_match8)


# также здесь мы можем провести и более тонкую работу, к примеру, вывести запись кортежами (ключ - значение)
_text9 = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001'
_match9 = re.findall(r'(\w+)\s*=\s*([^;]+)', _text9)
# print(_match9)


# рассмотрим пример использования минорного квантификатора на примера парсинга html-документа
__text = "<p>Картина <img src='bg.jpg'> в тексте</p>"
__match = re.findall(r'<img.*?>', __text)
# в данном случае .* означает, что нужно после img взять все символы пока у нас не встетится >
# и если бы мы использовали мажорный квантификатор, то у нас бы вывелось <img src='bg.jpg'> в тексте</p>
# мы даже можем создать мажорный аналог этому шаблону
__match1 = re.findall(r'<img[^>]*>', __text)
# [^>] этим мы говорим, чтобы он перебирал все символы кроме > до того момента, пока не встретится первая >
# print(__match)
# print(__match1)


