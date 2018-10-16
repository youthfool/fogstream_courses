""" 
Процентная ставка по вкладу составляет P процентов годовых,
которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести
два числа: величину вклада через год в рублях и копейках.
Дробная часть копеек отбрасывается.
"""

# nice input
# print("Enter the rate")
rate = int(input())
# print("Enter the deposit rubles")
deposit_ruble = int(input())
# print("Enter the deposit penny")
deposit_penny = int(input())

# total sum on deposit in penny
deposit_sum = deposit_ruble * 100 + deposit_penny

result_sum = deposit_sum + (deposit_sum / 100) * rate

result_ruble = int(result_sum / 100)
result_penny = int(result_sum) % 100

# nice output
# print("Contribution amount in a year: {} rubles and {} penny".format(result_ruble, result_penny))
print(result_ruble)
print(result_penny)

