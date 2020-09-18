meal = float(input("Стоимость вашего заказа: "))
tip = meal * 0.18
tax = meal * 0.10
meal_with_tax_and_tip = meal + tip + tax
total = tax + tip + meal_with_tax_and_tip
print(str(round(total, 2)) + "$")
