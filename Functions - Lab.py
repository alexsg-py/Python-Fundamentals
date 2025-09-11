# 1. Absolute Value
#Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().

# CODE:

list_of_strings = input().split()

list_of_numbers = []

for n in list_of_strings:
    number = float(n)
    list_of_numbers.append(number)

list_of_absolute_numbers = []

for num in list_of_numbers:
    absolute_number = abs(num)
    list_of_absolute_numbers.append(absolute_number)

print(list_of_absolute_numbers)

___

# 2. Grades

#Write a function that receives a grade between 2.00 and 6.00 and print the corresponding grade in words.
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

# CODE:

def grades(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6:
        return "Excellent"


grade = float(input())

print(grades(grade))

___

# 3. Calculations

#Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
#The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", and "subtract".

# CODE:

command = input()
first_num = int(input())
second_num = int(input())


def calculation(a, b, operator):
    result = None
    if command == "multiply":
        result = a * b
    elif command == "divide":
        result = a // b
    elif command == "add":
        result = a + b
    elif command == "subtract":
        result = a - b
    return result


print(calculation(first_num, second_num, command))

___

# 4. Repeat String

#Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. Print the result of the function. Try using lambda.

# CODE:

string = input()
counter = int(input())

repeat_string = lambda a, b: a * b

result = repeat_string(string, counter)

print(result)

___

# 5. Orders

#Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are: 
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

#Print the result formatted to the second decimal place.

# CODE:

product = input()
quantity = int(input())


def profit(bought_product, bought_quantity):
    result = None

    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2

    return result


final_profit = profit(product, quantity)

print(f"{final_profit:.2f}")

___

# 6. Calculate Rectangle Area

#Create a function that calculates and returns the area of a rectangle by a given width and height. Print the result on the console.

# CODE:

height = int(input())
width = int(input())


def area(rec_height, rec_width):
    calculated_area = height * width
    return calculated_area


rec_area = area(height, width)

print(rec_area)

___

# 7. Rounding

#Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().

# CODE:

given_numbers = input().split()

given_numbers_as_integer = []
rounded_numbers = []


def rounding():
    for n in given_numbers:

        integer_number = float(n)
        given_numbers_as_integer.append(integer_number)

    for num in given_numbers_as_integer:
        rounded_number = round(num)
        rounded_numbers.append(rounded_number)


rounding()

print(rounded_numbers)
