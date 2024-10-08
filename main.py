first_num = int(input("Введите первое число для сравнения: "))
second_num = int(input("Введите второе число для сравнения: "))
third_num = int(input("Введите третье число для сравнения: "))
if (first_num > second_num and first_num > second_num):
    print(f"Наибольшим числом из трех является певрое({first_num}): {first_num}>{second_num};{third_num}")
elif (second_num > first_num and second_num > third_num):
    print(f"Наибольшим числом из трех является второе({second_num}): {second_num}>{first_num};{third_num}")  
elif (third_num > second_num and third_num > first_num):
    print(f"Наибольшим числом из трех является третье({third_num}): {third_num}>{second_num};{first_num}")
else :
    print("Все числа, введенные вами равны")
