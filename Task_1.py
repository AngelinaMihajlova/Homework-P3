# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции. 
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

num = []

def get_sum(num):
    s = 0
    for i in range(1, len(num), 2):
        s += num[i]    
    print(s)

get_sum([2,3,5,9,3])
get_sum([1,5,25,3,15,20])
