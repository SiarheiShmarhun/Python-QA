# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
url = 'www.my_site.com#about'
print(url.replace('#','/'))


# Напишите программу, которая добавляет ‘ing’ к словам.
word = 'test'
print(word + 'ing')


# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
full_name = 'Ivanou Ivan'
name_parts = full_name.split()
print(name_parts[1] + ' ' + name_parts[0])


# Напишите программу которая удаляет пробел в начале, в конце строки.
text = '   hello world   '
print(text.strip())


# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
name = 'siArHeI'
print(name.capitalize())


# Перевести строку в список "Robin Singh" => ["Robin", "Singh"], "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"].
string_1 = "Robin Singh"
string_2 = "I love arrays they are my favorite"
arr1 = string_1.split()
print(arr1)
arr2 = string_2.split()
print(arr2)


# Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport". Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
names = ["Robin", "Singh"]
action = "Welcome"
place = "airport"
print(f"Hello, {names[0]} {names[1]}! {action} to {place}")


# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
words_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(words_list))


# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(2, 777)
del numbers [6]
print(numbers)