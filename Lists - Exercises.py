# 1. Invert Values

#"Write a program that receives a single string containing positive and negative numbers separated by a single space. 
#Print a list containing the opposite of each number."

# CODE:

string_numbers = input().split(" ")

numbers_as_integers = []

for current_number in string_numbers:
    current_number_as_integer = int(current_number)
    inverted_number = -current_number_as_integer
    numbers_as_integers.append(inverted_number)

print(numbers_as_integers)

___

# 2. Multiples List

#"Write a program that receives two numbers (factor and count). 
#It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor. 
#The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor."

# CODE:

factor = int(input())
count = int(input())

multiples_list = []

for index in range(1, count + 1):

        multiples_list.append(factor * index)

print(multiples_list)

___

# 3. Football Cards

#"Most football fans love it for the goals and excitement. Well, this problem does not. You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
#The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. 
#If one of the teams has less than 7 players remaining, the referee stops the game immediately, and the team with less than 7 players loses.
#The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g., the card "B-7" means player #7 from team B received a card.
#The task: You will be given a sequence of cards (could be empty), separated by a single space. You should print the count of remaining players on each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}". 
#If the referee terminated the game, print an additional line: "Game was terminated".
#Note for the random tests: If a player who has already been sent off receives another card - ignore it."

# CODE:

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

players = input().split()
game_was_terminated = False

for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_was_terminated:
    print("Game was terminated")

___
# 4. Number Beggars

#You will receive 2 lines of input. On the first line, you will receive a single string of integers, separated by a comma and a space ", ". 
#On the second line, you will receive a count of beggars. Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last number in the list.
#For example, [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], and the second one collects [2, 4]. 
#The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7, and 3, as they will respectively take [1, 4], [2, 5], and [3].
#Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n. The list length could be even shorter - i.e., the last beggars will take nothing (0).

# CODE:

money_as_string = input().split(", ")
count_of_beggars = int(input())

total_list = []
money_as_integer = []

starting_index = 0

for money in money_as_string:
    money_as_integer.append(int(money))

for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for index in range(starting_index, len(money_as_integer), count_of_beggars):
        current_beggar_sum += money_as_integer[index]

    total_list.append(current_beggar_sum)
    starting_index += 1

print(total_list)

___

# 5. Faro Shuffle

#A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
#For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
#Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
#Note: The length of the deck of cards will always be an even number.

# CODE:

deck = input().split()
count_of_shuffles = int(input())

for _ in range(count_of_shuffles):
    half_deck = len(deck) // 2
    deck_one = deck[:half_deck]
    deck_two = deck[half_deck:]

    faro_shuffled_deck = []

    for index in range(half_deck):
        faro_shuffled_deck.append(deck_one[index])
        faro_shuffled_deck.append(deck_two[index])

    deck = faro_shuffled_deck

print(deck)

___

# 6. Survival of the Biggest

#Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n represents the count of numbers to remove from the list. 
#You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

# CODE:

given_integers = input().split()
count_of_numbers_to_remove = int(input())

list_of_integers = []
list_of_integers_two = []

for index in given_integers:
    number = int(index)
    list_of_integers.append(number)
    list_of_integers_two.append(number)

list_of_integers.sort(reverse=True)

for num in range(count_of_numbers_to_remove):
    list_of_integers.pop(-1)

corrected_list = [item for item in list_of_integers_two if item in list_of_integers]

result = ", ".join(map(str, corrected_list))

print(result)

___

# 7. Easter Gifts

#As a good friend, you decide to buy presents for your friends.
#Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
#"{gift1} {gift2} {gift3}… {giftn}"
#Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"

# •	Find the gifts with this name in your collection, if any, and change their values to "None".  
# •	"Required {gift} {index}"
# •	If the index is valid, replace the gift on the given index with the given gift. 
# •	"JustInCase {gift}"
# •	Replace the value of your last gift with this one. 

#In the end, print the gifts on a single line, except the ones with the value "None", separated by a single space in the following format:
#"{gift1} {gift2} {gift3} … {giftn}"

#Input / Constraints
# •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
# •	On the following lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.

#Output

# •	Print the gifts in the format described above.



# CODE:

gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command_split = command.split()
    command_name = command_split[0]

    if command_name == "OutOfStock":
        gift_item = command_split[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_item:
                gifts[i] = "None"

    elif command_name == "Required":
        gift_item = command_split[1]
        index = int(command_split[2])

        if 0 <= index < len(gifts):
            gifts[index] = gift_item

    elif command_name == "JustInCase":
        gift_item = command_split[1]
        gifts[-1] = gift_item

corrected_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(corrected_gifts))

___

# 8. Seize the fire

#The group of adventurists has gone on their first task. Now they should walk through fire - literally. They should use all the water they have left. Your task is to help them survive.
#Create a program that calculates the water needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.
#First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:
#"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
#Afterward, you will receive the amount of water you have for putting out the fires. There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.

#Type of Fire	Range:
# High	81 - 125
# Medium	51 – 80
# Low	1 - 50

#If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and you need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the total effort. Keep putting out cells until you run out of water. Skip it and try the next one if you do not have enough water to put out a given cell. In the end, print the cells you have put out in the following format:
#"Cells:
 #- {cell1}
 #- {cell2}
 #…
 #- {cellN}"
#"Effort: {effort}"
#The effort should be formatted to the second decimal place. 
#In the end, print the total fire you have put out from all the cells in the following format: 

#"Total Fire: {total_fire}"

#Input / Constraints

# •	On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in the range [1…500].
# •	On the 2nd line, you will receive the water – an integer number in the range [0….100000].

#Output

#Print the output as described above.

# CODE:

# Type of fire:
# High - 81 - 125
# Medium - 51 - 80
# Low - 1 - 50

type_of_fire = input().split("#")
water_quantity = int(input())

effort_for_fire = 0
total_fire = 0

final_list = []


for i in range(len(type_of_fire)):
    fire, value = type_of_fire[i].split(" = ")
    cell_value = int(value)

    if fire == "High" and 81 <= cell_value <= 125:
        if water_quantity < cell_value:
            continue
        effort_for_fire += cell_value * 0.25
        water_quantity -= cell_value
        total_fire += cell_value
        final_list.append(cell_value)

    elif fire == "Medium" and 51 <= cell_value <= 80:
        if water_quantity < cell_value:
            continue
        effort_for_fire += cell_value * 0.25
        water_quantity -= cell_value
        total_fire += cell_value
        final_list.append(cell_value)

    elif fire == "Low" and 1 <= cell_value <= 50:
        if water_quantity < cell_value:
            continue
        effort_for_fire += cell_value * 0.25
        water_quantity -= cell_value
        total_fire += cell_value
        final_list.append(cell_value)

print("Cells:")
for cell in final_list:
    print(f" - {cell}")
print(f"Effort: {effort_for_fire:.2f}")
print(f"Total Fire: {total_fire}")

___

# 9. Hello France

#You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items within your budget and then sell them at a higher price – with a 40% markup.
#You will receive a collection of items and a budget in the following format:
#{type->price|type->price|type->price……|type->price}
#{budget}
#The prices for each of the types cannot exceed a specific price, which is given below:

#Type	Maximum Price

# Clothes	50.00
# Shoes	35.00
# Accessories	20.50

#If the price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
#Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough to buy the train ticket.

#Input / Constraints

# •	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]

#Output

# •	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
#"{price1} {price2} {price3} … {priceN}"
# •	Second, print the profit, formatted to the second decimal point in the following format:
#"Profit: {profit}"
# •	Finally:
# •	If the budget is enough to buy the train ticket, print: "Hello, France!" 
# •	Otherwise, print: "Not enough money."

# CODE:

# clothes - 50
# shoes - 35
# accessories - 20.50

# ticket - 150

collection_of_items = input().split("|")
budget = int(input())

bought_items = []

starting_budget = budget
total_earnings = 0

for item in range(len(collection_of_items)):

    product, price = collection_of_items[item].split("->")
    price_float = float(price)

    if product == "Clothes" and price_float <= 50 and price_float <= starting_budget:
        starting_budget -= price_float
        bought_items.append(price_float)

    if product == "Shoes" and price_float <= 35 and price_float <= starting_budget:
        starting_budget -= price_float
        bought_items.append(price_float)

    if product == "Accessories" and price_float <= 20.50 and price_float <= starting_budget:
        starting_budget -= price_float
        bought_items.append(price_float)

new_prices = []

for money in bought_items:
    markup_money = round(money + (money * 0.40), 2)
    total_earnings += round(markup_money, 2)
    new_prices.append(markup_money)

profit = total_earnings - (budget - starting_budget)
total_money = round(sum(new_prices) + starting_budget, 2)

print(" ".join(f"{x:.2f}"for x in new_prices))
print(f"Profit: {profit:.2f}")

if total_money >= 150:
    print("Hello, France!")
elif total_money < 150:
    print("Not enough money.")

___

# 10. Bread Factory

#As a young baker, you are baking the bread out of the bakery. 
#You have an initial energy of 100 and initial coins of 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
#Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# •	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.". 
# •	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order": 
# •	You've earned some coins (the number in the second part). 
# •	Each time you get an order, your energy decreases by 30 points.
#  	If you have the energy to complete the order, print: "You earned {earned} coins.".
#  	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. 
# •	If you have enough money, you should buy the ingredients and print:
#"You bought {ingredient}."
#•	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 

#If you managed to handle all events throughout the day, print on the following 3 lines: 

#"Day completed!"
#"Coins: {coins}"
#"Energy: {energy}"

#Input / Constraints:

#You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
#"event1|event2| … eventN".
#Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"

#Output

#Print the corresponding messages described above.

# CODE:

initial_energy = 100
initial_coins = 100

max_energy = 100
current_energy = initial_energy
gained_energy = 0

current_coins = initial_coins
gained_coins = 0

working_day_events = input().split("|")

event_counter = len(working_day_events)

for event in range(len(working_day_events)):
    event_name, value = working_day_events[event].split("-")
    event_value = int(value)

    if event_name == "rest":
        energy_before = current_energy
        current_energy += event_value
        if current_energy > max_energy:
            current_energy = max_energy
            gained_energy = current_energy - energy_before
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")
            event_counter -= 1
        else:
            gained_energy += event_value
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")
            event_counter -= 1

    elif event_name == "order":
        if current_energy >= 30:
            gained_coins += event_value
            current_coins += event_value
            current_energy -= 30
            print(f"You earned {gained_coins} coins.")
            event_counter -= 1
        else:
            current_energy += 50
            print("You had to rest!")
            event_counter -= 1

    else:
        if current_coins >= event_value:
            current_coins -= event_value
            print(f"You bought {event_name}.")
            event_counter -= 1
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break

    gained_energy = 0
    gained_coins = 0

if event_counter == 0:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
