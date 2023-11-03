import json

sum_mul: float = 0.00
sum_: float = 0.00

with open('input.json', 'r') as file:
    data = json.load(file)
    for i in data:
        sum_mul = i["score"] * i["weight"]
        sum_ += sum_mul

print('%.3f' % sum_)
