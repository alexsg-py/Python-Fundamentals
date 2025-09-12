# 1. Comment

#Create a class with the name "Comment". The __init__ method should accept 3 parameters:
# •	username
# •	content
# •	likes (optional, 0 by default)
#Use the exact names for your variables
#Note: there is no input/output for this problem. Test the class yourself and submit only the class

# CODE:

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes



comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

___

# 2. Party

#Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters. 
#You will be given names of people (on separate lines) until you receive the command "End". Use the created class to solve this problem. After you receive the "End" command, print 2 lines:
# •	"Going: {people}" - the people should be separated by comma and space ", ".
# •	"Total: {total_people_going}"
#Note: submit all of your code, including the class

# CODE:

class Party:
    def __init__(self):
        self.people = []


party = Party()

command = input()

while command != "End":
    party.people.append(command)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")

___

# 3. Email

#Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
#You will receive some information (separated by a single space) until you receive the command "Stop". The first element will be the sender, the second one – the receiver, and the third one – the content. 
#On the final line, you will be given the indices of the sent emails separated by comma and space ", ". 
#Call the send() method for the given indices of emails. For each email, call the get_info() method.

# CODE:

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()

while command != "Stop":
    tokens = command.split(" ")
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())

# 4. Zoo

#Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo. 
#There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species, adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format: 
#"{Species} in {zoo_name}: {names}
#Total animals: {total_animals}" 
#On the first line, you will receive the name of the zoo. On the second line, you will receive number n. On the following n lines you will receive animal info in the format: "{species} {name}". 
#Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird". 
#On the final line, you will receive a species. 
#At the end, print the info for that species and the total count of animals in the zoo.

# CODE:

def get_info(species):
    result = ""


class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        result = ""

        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"

        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))

___

# 5. Circle

#Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter. Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
# •	calculate_circumference() - returns the circumference of the circle
# •	calculate_area() - returns the area of the circle
# •	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector

# CODE:

class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.__pi * self.radius * self.radius


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
