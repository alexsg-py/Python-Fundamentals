# 1. No Vowels
#Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
#Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

# CODE:

text = input()

vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

no_vowels = "".join([x for x in text if x not in vowels])

print(no_vowels)

___

# 2. Trains

#You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
#There will be no case in which the index is invalid!
#After you receive the "End" command print the train.

# CODE:

wagons = int(input())

train_length = [0] * wagons

while True:
    command = input().split()

    current_command = command[0]

    if current_command == "End":
        break

    if current_command == "add":

        value_to_add = int(command[1])
        train_length[-1] += value_to_add

    elif current_command == "insert":

        index = int(command[1])
        people_to_add = int(command[2])

        train_length[index] += people_to_add

    elif current_command == "leave":

        ind = int(command[1])
        remove_people = int(command[2])

        train_length[ind] -= remove_people


print(train_length)

___

# 3. To-Do List

#You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
#Return a list containing all to-do notes sorted by importance in ascending order. 
#The importance value will always be an integer between 1 and 10 (inclusive).

# CODE:

notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]

print(result)

___

# 4. Palindrome strings

#On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. 
#First, you should print a list containing all the found palindromes in the sequence. Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

# CODE:

strings = input().split(" ")

searched_palindrome = input()

palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

___

# 5. Sorting Names

#Write a program that reads a single string with names separated by comma and space ", ". 
#Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the resulting list.

# CODE:

names_list = input().split(", ")

sorted_list = sorted(names_list, key=lambda x: (-len(x), x))

print(sorted_list)

___

# 6. Even Numbers

#Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.

# CODE:

number_list = list(map(int, input().split(", ")))

found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))

even_indices = list(filter(lambda a: a != "no", found_indices_or_no))

print( even_indices)

___

# 7. The Office

#You will receive two lines of input: 
# •	a list of employees' happiness as a string of numbers separated by a single space 
# •	a happiness improvement factor (single number).
#Your task is to find out if the employees are generally happy in their office. 
#First, multiply each employee's happiness by the factor.
#Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
#"Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
#"Score: {happy_count}/{total_count}. Employees are not happy!"

# CODE:

employees = input().split()
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employees))

filtered = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
