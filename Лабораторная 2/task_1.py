money_capital = float(input("How much money do you have?"))
salary = float(input("How much do you earn?"))
spend =float(input("How much do you spend?"))
float(spend)
increase=5
budget= salary+money_capital
month = 0
if(spend>salary):
    while True:
        if (budget>spend):
            budget-=spend;
            month+=1;
        else:
            break;
        if(budget>=0):
            spend = spend*(1+(increase/100))
            budget+=salary;
        else:
            break;
    print(month)
