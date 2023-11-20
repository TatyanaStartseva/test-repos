numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
first_part = numbers[0:4:1]
second_part = numbers[5::1]
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_sum = (sum(first_part)+sum(second_part))/ (len(first_part)+ len(second_part)+1)
numbers[4] = numbers_sum
print("Измененный список:", numbers)
