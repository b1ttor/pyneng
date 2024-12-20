# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

# УМНЫЙ МЕТОД

result = '''
{0:<10}{1:<10}{2:<10}{3:<10}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}  
'''
ip = "192.168.3.1".split('.')

print(result.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))

'''
ГЛУПЫЙ МЕТОД
ip = "192.168.3.1"
ipbb = ip.split('.')
ip1 = int(ipbb[0])
ip2 = int(ipbb[1])
ip3 = int(ipbb[2])
ip4 = int(ipbb[3])

ip1b = bin(ip1)[2:]
ip2b = bin(ip2)[2:]
ip3b = '000000' + bin(ip3)[2:]
ip4b = '0000000' + bin(ip4)[2:]

print('{:<10} {:<10} {:<10} {:<10}'.format(ip1, ip2, ip3, ip4))
print('{:<10} {:<10} {:<10} {:<10}'.format(ip1b, ip2b, ip3b, ip4b))
'''