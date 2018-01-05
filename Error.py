while True:
    x = input('Введите число: ')
    try:
        x = float(x)
        y = 100/x
        break
    except ValueError:
        print("Ошибка")
    except ZeroDivisionError:
        y = 'бесконечность'
        break
print(y)
