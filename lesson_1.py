import chardet
import subprocess


# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str1 = 'разработка'
str2 = 'сокет'
str3 = 'декоратор'
print(type(str1))
print(type(str2))
print(type(str3))
print(str1)
print(str2)
print(str3)
uni1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
uni2 = '\u0441\u043e\u043a\u0435\u0442'
uni3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(uni1))
print(type(uni2))
print(type(uni3))
print(uni1)
print(uni2)
print(uni3)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

byte1 = b'class'
byte2 = b'function'
byte3 = b'method'
# byte4 = b'Привет'
print(type(byte1))
print(type(byte2))
print(type(byte3))
print(byte1)
print(byte2)
print(byte3)
print(len(byte1))
print(len(byte2))
print(len(byte3))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s_1 = b'attribute'
s_2 = b'класс'
s_3 = b'функция'
s_4 = 'type'

# «type» невозможно записать в байтовом типе.
# s_3 = b'функция'
# SyntaxError: bytes can only contain ASCII literal characters.

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_s = ['разработка', 'сокет', 'декоратор']
strs_in_bytes = []

for s in str_s:
    s = s.encode('utf-8', errors='namereplace')
    strs_in_bytes.append(s)
    print(s)

for s in strs_in_bytes:
    print(s.decode('ascii', errors='replace'))
    print(s.decode(chardet.detect(s)['encoding']))

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

ping_results = ''

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results += line.decode('cp866')

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results += line.decode('cp866')

print(ping_results.encode('utf-8').decode('utf-8'))

# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно
# открыть файл в формате Unicode и вывести его содержимое.


with open('test_file.txt', 'w') as file:
    file.write('сетевое программирование\nсокет\nдекоратор\n')
    print(type(file))
with open('test_file.txt', 'r', encoding='utf8') as file:
    for line in file:
        print(line)