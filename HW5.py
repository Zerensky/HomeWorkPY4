# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


result = 0
with open('file1.txt', 'r') as file1:
    st1 = file1.read()

with open('file2.txt', 'r') as file1:
    st2 = file1.read()

result = st1 + ' + ' + st2
print(result)

with open ('file3.txt', 'w') as file1:
    file1.write(result)



