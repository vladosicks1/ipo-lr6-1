#Написать программу, которая:
#Создаёт список из 6 строк (строки определяются в коде, на ваш вкус).
#Подсчитывает количество строк, содержащих букву a.
#Использует циклы для подсчета.

strings = ['аааааааа руенну','цукйуйцу','нукупр','мгкцт','ййаааплоррр','вппарпрр']
x = 0

for i in strings:
    for j in i:
        if j == "а" or j == "А":
            x+=1
            break

print("Количество строк, содержащих букву а:",x)