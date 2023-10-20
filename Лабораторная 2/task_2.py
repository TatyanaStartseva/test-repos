from multiprocessing.spawn import import_main_path


salary = float(input("How much do you earn?"))
spend =float(input("How much do you spend?"))
float(spend)
increase=3
if(spend>salary):
    for i in range(9):
        if(salary>spend): break;
        spend+=spend*(1+(increase/100))
        salary+=salary

    money_capital=spend-salary
    import math
    print(math.ceil(money_capital))
