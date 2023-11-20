salary = 5000.00  # Ежемесячная зарплата
spend = 6000.00  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03
increase += 1.00
money_capital_ = salary - spend
money_capital = 0.00
if spend > salary:
    for i in range(1, months, 1):
        money_capital += (salary - (spend * (increase ** i)))
money_capital += money_capital_
import math
money_capital = abs(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", "{:.2f}".format(money_capital))
