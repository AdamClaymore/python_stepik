# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке
start = 1
a = int(input())
b = [[0 for j in range(a)] for i in range(a)]
b[a // 2][a // 2] = a * a
for r in range(a // 2):
    j = 0
    for i in range(a - r - r):
        b[j + r][i + r] = start
        start = start + 1
    for j in range(a - 1 - r - r):
        b[j + 1 + r][i + r] = start
        start = start + 1
    for k in range(a - 1 - r - r):
        b[a - 1 - r][a - k - 2 - r] = start
        start = start + 1
    for m in range(a - 2 - r - r):
        b[a - 2 - m - r][a - a + r] = start
        start = start + 1
for y in range(a):
    for j in range(a):
        print(b[y][j], end=" ")
    print("")
