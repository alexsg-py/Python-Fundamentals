# Step 1: Display a menu to the user
# print("🧠 Welcome to the Text Transformation Toolkit!")
# print("Choose a transformation:")
# print("1. Reverse Text")
# print("2. Convert to Uppercase")
# print("3. Convert to Lowercase")
# print("4. Title Case")
# print("5. Count Vowels")
# print("6. Remove All Spaces")
# print("7. Replace Vowels with '*'")
# print("8. Check if Palindrome")
# print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:
    # TODO: Reverse the text using slicing or a loop
    reversed_word = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_word += text[i]
    print(reversed_word)

elif choice == 2:
    # TODO: Convert the text to uppercase using string methods
    print(text.upper())

elif choice == 3:
    # TODO: Convert the text to lowercase using string methods
    print(text.lower())

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    print(text.title())

elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    vowel_counter = 0

    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowel_counter += 1
    print(vowel_counter)

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    text = text.replace(" ", "")
    print(text)

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    for char in text:
        if char == "a":
            text = text.replace("a", "*")
        if char == "e":
            text = text.replace("e", "*")
        if char == "i":
            text = text.replace("i", "*")
        if char == "o":
            text = text.replace("o", "*")
        if char == "u":
            text = text.replace("u", "*")
    print(text)

elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)
    reversed_word = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_word += text[i]
    if text == reversed_word:
        print(f"This is a palindrome. The word {text} spelled backwards is {reversed_word}.")
    else:
        print("The word is not a palindrome.")

elif choice == 9:
    # TODO: Count the frequency of each word and display the result
    word_freq = {}

    for word in text.split():
        word_freq[word] = word_freq.get(word, 1) + 1

    print(word_freq)

else:
    print("❌ Invalid choice! Please restart the program.")
