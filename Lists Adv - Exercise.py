# 1. Which Are In?

#You will be given two sequences of strings, separated by ", ". 
#Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

# CODE:

string_one = input().split(", ")
string_two = input().split(", ")

result = []

final_result = []

for word in string_one:
    for wd in string_two:
        if word in wd:
            result.append(word)

for wd in result:
    if wd not in final_result:
        final_result.append(wd)

print(final_result)

___

# 2. Next Version

#You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
#You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version. 
#For example, if the current version is "1.3.4", the next version will be "1.3.5". 
#The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below. 

# CODE:

current_version = input().split(".")

current_version_int = [int(el) for el in current_version]


current_version_int[2] += 1

if current_version_int[2] > 9:
    current_version_int[2] = 0
    current_version_int[1] += 1

if current_version_int[1] > 9:
    current_version_int[1] = 0
    current_version_int[0] += 1

current_version_str = [str(el) for el in current_version_int]

print(".".join(current_version_str))

___

# 3. Word Filter

#Using comprehension, write a program that receives some text, separated by space, and takes only those words whose length is even. Print each word on a new line.

# CODE:

text = input().split()

even_words = [el for el in text if len(el) % 2 == 0]

print("\n".join(even_words))

___

# 4. Number Classification

#Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
#Note: Zero is counted as a positive number

# CODE:

given_numbers = [int(el) for el in input().split(", ")]

positive = [el for el in given_numbers if el >= 0]
negative = [el for el in given_numbers if el < 0]
even = [el for el in given_numbers if el % 2 == 0]
odd = [el for el in given_numbers if el % 2 != 0]

positive_str = [str(el) for el in positive]
negative_str = [str(el) for el in negative]
even_str = [str(el) for el in even]
odd_str = [str(el) for el in odd]

print(f'Positive: {", ".join(positive_str)}')
print(f'Negative: {", ".join(negative_str)}')
print(f'Even: {", ".join(even_str)}')
print(f'Odd: {", ".join(odd_str)}')

___

# 5. Office Chairs

#You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
#On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors. 
#Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors). 
#Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".

# CODE:

number_of_rooms = int(input())

free_chairs = 0
less_chairs = 0

for room in range(1, number_of_rooms + 1):
    chairs_and_people = input().split()
    chairs = chairs_and_people[0]
    people = int(chairs_and_people[1])

    if len(chairs) < people:
        chairs_needed = people - len(chairs)
        less_chairs += 1
        print(f"{chairs_needed} more chairs needed in room {room}")

    if len(chairs) > people:
        free_chairs += len(chairs) - people

if less_chairs == 0:
    print(f"Game On, {free_chairs} free chairs left")

# 6. Electron Distribution

#You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
#You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
# •	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# •	You should start filling the shells from the first one at the first position.
# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
#In the end, print a list with the filled shells.

# CODE:

number_of_electrons = int(input())

filled_shells = []

shell = 1

while number_of_electrons != 0:

    shell_to_fill = 2 * shell**2

    if shell_to_fill > number_of_electrons:
        filled_shells.append(number_of_electrons)
        break

    filled_shells.append(shell_to_fill)
    shell += 1
    number_of_electrons -= shell_to_fill

print(filled_shells)

___

# 7. Group of 10s

#Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
#Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
#For more clarification, see the examples below.

# CODE:

input_string = input()

numbers = list(map(int, input_string.split(", ")))

max_number = max(numbers)
max_group = (max_number // 10 + (1 if max_number % 10 != 0 else 0)) * 10

for group in range(10, max_group + 1, 10):
    lower_bound = group - 9
    upper_bound = group
    group_numbers = [n for n in numbers if lower_bound <= n <= upper_bound]
    print(f"Group of {group}'s: {group_numbers}")

# 8. Decipher This!

#You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

# CODE:

message = input().split(' ')
deciphered = []

for word in message:
    ascii_char = [char for char in word if char.isdigit()]
    word_list = [char for char in word if char not in ascii_char]

    first_letter = chr(int(''.join(ascii_char)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + ''.join(word_list)
    deciphered.append(new_word)

print(' '.join(deciphered))
