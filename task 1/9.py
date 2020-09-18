summa = float(input())

summa1 =  summa + summa * 0.04
summa2 = summa1 + summa1 * 0.04
summa3 = summa2 + summa2 * 0.04
print("After 1 year: " + str(round(summa1, 2)) + "$")
print("After 2 year: " + str(round(summa2, 2)) + "$")
print("After 3 year: " + str(round(summa3, 2)) + "$")
