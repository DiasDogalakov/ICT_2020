a = float(input("Введите количество контейнеров объёмом меньше или равно 1 литр: ")) # <=1 литр
b = float(input("Введите количество контейнеров объёмом больше 1 литра: "))          # > 1 литр
summa = ((a * 0.10) + (b * 0.25))
print(str(round(summa, 2)) + "$")
