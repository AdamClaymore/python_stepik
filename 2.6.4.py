# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке
start = 1
a = int(input())
b = [[0 for j in range(a)] for i in range(a)]

j = 0

for i in range(a):
        b[j][i] = start
        start = start + 1
for j in range(a-1):
         b[j+1][i] = start
         start = start + 1

for k in range(a-1):
         b[a-1][a - k - 2] = start
         start = start + 1
for m in range(a-2):
         b[a-2-m][a-a] = start
         start = start + 1

      #print(b[j][i], end=" ")
for y in range(5):
    for j in range(5):
        print(b[y][j], end="\t")
    print("\n")


