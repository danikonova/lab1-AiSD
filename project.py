with open('1.txt', mode='r') as f:
    a = f.readline().split()
b = []
a1 = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
      6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
a2 = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
      5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
      8: 'восемьдесят', 9: 'девяносто'}
a3 = {0: '', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
      14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
      17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
a4 = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
      5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот',
      9: 'девятьсот'}
count = 0
for i in range(len(a) - 1):
    if int(a[i], 2) < int(a[i + 1], 2):
        count += 1
    else:
        b.append(int(a[i - count], 2))
        count = 0
if count != 0:
    b.append(int(a[i - count + 1], 2))
for j in range(len(b)):
    i = str(b[j])
    dlina = len(i)
    count = 0
    while len(i) != count:
        if dlina == 4:
            print('одна тысяча', end=' ')
            dlina = dlina - 1
            count += 1
        if dlina == 3:
            if int(i[count]) != 0:
                print(a4[int(i[count])], end=' ')
            dlina = dlina - 1
            count += 1
        if dlina == 2 and int(i[-2]) == 1:
            if int(i[count]) != 0:
                print(a3[int(i[count:])], end=' ')
            dlina = dlina - 2
            count += 2
        elif dlina == 2:
            if int(i[count]) != 0:
                print(a2[int(i[count])], end=' ')
            dlina = dlina - 1
            count += 1
        if dlina == 1:
            if int(i[count]) != 0:
                print(a1[int(i[count])], end=' ')
            dlina = dlina - 1
            count += 1
            print()