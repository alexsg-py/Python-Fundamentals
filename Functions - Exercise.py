# 1. Smallest of three numbers

# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function.

# CODE:

def smallest_num(num_one, num_two, num_three):
    smallest_number = 0
    if num_one < num_two and num_one < num_three:
        smallest_number = num_one
    elif num_two < num_one and num_two < num_three:
        smallest_number = num_two
    elif num_three < num_one and num_three < num_two:
        smallest_number = num_three

    return smallest_number


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(smallest_num(number_one, number_two, number_three))

___

# 2. Add and subtract

#You will receive three integer numbers. 
#Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
#Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. Print the result of the subtract() function on the console.

number_one = int(input())
number_two = int(input())
number_three = int(input())


def sum_numbers(num_one, num_two):
    result_add = num_one + num_two
    return result_add


result_addition = sum_numbers(number_one, number_two)


def subtract(add_result, num_three):
    result_subtract = add_result - num_three
    return result_subtract


print(subtract(result_addition, number_three))

___

# 3. Characters in range

#Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), separated by a single space. Print the result on the console.

# CODE:

def get_characters(first_character : str, second_character : str):
    characters = []

    for current_char in range(ord(first_character) + 1, ord(second_character)):
        characters.append(chr(current_char))

    return characters


char_one = input()
char_two = input()


missing_characters = get_characters(char_one, char_two)

print(" ".join(missing_characters))

___

# 4. Odd and even sum

#You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number. The result should be returned as a single string in the format: 
#"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
#Print the result of the function on the console.

# CODE:

number = int(input())


def even_odd_sum(num : int):
    even_sum = 0
    odd_sum = 0

    for digit in str(number):

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        elif int(digit) % 2 != 0:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


sum_result = even_odd_sum(number)

print(sum_result)

___

# 5. Even Numbers

#Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. Use filter().

# CODE:

def even(number):
    return number % 2 == 0


numbers_as_string = input().split()
numbers_as_integer = []

for num in numbers_as_string:
    numbers_as_integer.append(int(num))

result = filter(even, numbers_as_integer)

print(list(result))

___

# 6. Sort

#Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted list of numbers in ascending order. Use sorted().

# CODE:

numbers_as_string = input().split()
numbers_as_integer = []

for num in numbers_as_string:
    numbers_as_integer.append(int(num))

print(sorted(numbers_as_integer))

___

# 7. Min, Max and Sum

#Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
#The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

# CODE:

numbers_as_string = input().split()
numbers_as_integer = []

for num in numbers_as_string:
    numbers_as_integer.append(int(num))

print(f"The minimum number is {min(numbers_as_integer)}")
print(f"The maximum number is {max(numbers_as_integer)}")
print(f"The sum number is: {sum(numbers_as_integer)}")

___

# 8. Palindrome Integers

#A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives a list of positive integers, separated by comma and space ", ". 
#The function should check if each integer is a palindrome - True or False. Print the result.

# CODE:

def palindrome_check(number):
    return number == number[::-1]


user_input = input().split(", ")

for num in user_input:
    result = palindrome_check(num)
    print(result)
