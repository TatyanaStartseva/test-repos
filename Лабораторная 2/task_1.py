money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 5
budget = salary+money_capital
month = 0
if spend > salary:
    while True:
        if budget > spend:
            budget -= spend
            month += 1
        else:
            break
        if budget >= 0:
            spend = spend*(1+(increase/100))
            budget += salary
        else:
            break

print("Количество месяцев, которое можно протянуть без долгов:", month)
