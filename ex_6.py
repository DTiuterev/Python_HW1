#6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
print('Вы введете день недели цифрой, а я напишу, рабочий он или выходной')
n = int(input('Введите день недели (число от 1 до 7): '))
if n < 1 or n > 7:
    print('Вы ввели некорректный номер дня недели')
elif n == 6 or n == 7:
    print(f'День недели с номером {n} - выходной')
else:
    print(f'День недели с номером {n} - рабочий')

