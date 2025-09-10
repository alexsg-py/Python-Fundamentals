# 1. Strange Zoo

#You are at the zoo, and the meerkats look strange. 
#You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. Your task is to re-arrange the elements in a list so that the animal looks normal again:
#•	On the first position is the head;
#•	On the second position is the body;
#•	On the last one is the tail.

# CODE:

correct_body = []

for _ in range(3):
    data = input()
    correct_body.append(data)

# index swap
correct_body[0], correct_body[2] = correct_body[2], correct_body[0]

print(correct_body)

___

# 2. Courses

# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses. You should create a list of courses and print it.

# CODE:

n = int(input())

my_list = []

for name in range(n):
    course = input()
    my_list.append(course)

print(my_list)
___

# 3. List Statistics

#On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
#•	One with all the positive (including 0) numbers
#•	One with all the negative numbers
#Finally, print the following message: 
#"Count of positives: {count_positives}
#Sum of negatives: {sum_of_negatives}"

# CODE:

n = int(input())

positive_number = []
negative_numbers = []

for num in range(n):
    number = int(input())

    if number >= 0:
        positive_number.append(number)
    elif number < 0:
        negative_numbers.append(number)

print(positive_number)
print(negative_numbers)
print(f"Count of positives: {len(positive_number)}")
print(f"Sum of negatives: {sum(negative_numbers)}")

___

# 4. Search

#On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. 
#You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.

# CODE:

n = int(input())
magic_word = input()

my_list = []
my_filtered_list = []

for _ in range(n):
    phrase = input()
    my_list.append(phrase)
    if magic_word in phrase:
        my_filtered_list.append(phrase)

print(my_list)
print(my_filtered_list)

___

# 5. Numbers Filter

#On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
#•	even
#•	odd
#•	negative
#•	positive
#Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

# CODE:

n = int(input())

my_list = []

for _ in range(n):
    number = int(input())
    my_list.append(number)

command = input()

filtered_numbers = []

if command == "even":
    for num in my_list:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in my_list:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in my_list:
        if num < 0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in my_list:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)
