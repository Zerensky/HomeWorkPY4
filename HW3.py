# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list = [5, 6, 8, 5, 8, 10]
list1 = []
count = 0
for i in range(len(list)):
    while count < len(list):
        if list[count] == list[i] and count != i:
            count = 0
            break
        count +=1
    else:
        list1.append(list[i])
        count = 0
print(list1)


# или

# def unique_elements(list):
#     new_list = []
#     for i in numbers:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# numbers = [-3, -2, -1, 0, 0, 0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8, 9, 10, 11]
# print(numbers)
# print(unique_elements(numbers))



