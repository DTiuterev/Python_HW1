#9.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
n = str(input('Введите номер четверти плоскости координат римскими цифрами (I, II, III или IV): '))
if n in['I', 'II', 'III', 'IV']:
    if n == 'I':
        print(f'Число в {n} четверти может иметь координаты х и у от 0 до плюс бесконечности.')
    elif n == 'II':
        print(f'Число во {n} четверти может иметь координату х от минус бесконечности до 0 и у от 0 до плюс бесконечности.')
    elif n == "III":
        print(f'Число в {n} четверти может иметь координату х и y от минус бесконечности до 0.')
    elif n == "IV":
        print(f'Число в {n} четверти может иметь координату х от 0 до плюс бесконечности и y от минус бесконечности до 0.')

else:
    print('Введено некорректное римское число или иной символ.')