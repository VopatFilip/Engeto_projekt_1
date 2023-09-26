"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Filip Vopát
email: vopat.f@gmail.com
discord: Vopat#9797
"""

# Define the texts
texts = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# User authentication
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


def login():
    username = input("username: ")
    password = input("password: ")

    if users.get(username) == password:
        print("_" * 40)
        print(f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.")
        print("_" * 40)
    else:
        print("Invalid username or password. Please try again.")
        exit()


login()

# Get the selected text
while True:
    number = input("Enter a number between 1 and 3 to select a text: ")
    if number.isdigit() and 1 <= int(number) <= 3:
        break
    print("Invalid input. Please enter a number between 1 and 3.")

selected_text = texts[int(number) - 1]

# Analyze the selected text
words = selected_text.split()
titlecase_words = [word for word in words if word.istitle()]
uppercase_words = [word for word in words if word.isupper()]
lowercase_words = [word for word in words if word.islower()]
numeric_strings = [word for word in words if word.isdigit()]

# Word count
word_count = len(words)
titlecase_count = len(titlecase_words)
uppercase_count = len(uppercase_words)
lowercase_count = len(lowercase_words)
numeric_count = len(numeric_strings)
numeric_sum = sum(int(word) for word in numeric_strings)

# Display the results
print("_" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all numbers is {numeric_sum}.")
print("_" * 40)

# Word length distribution table
word_length_distribution = {}
for word in words:
    length = len(word)
    if length in word_length_distribution:
        word_length_distribution[length] += 1
    else:
        word_length_distribution[length] = 1

max_occurrences_width = max(word_length_distribution.values())
print(f"{'LEN':<3} | {'OCCURRENCES':<{max_occurrences_width}} | {'NR.':<3}")
print("_" * 40)
for length, count in sorted(word_length_distribution.items()):
    print(f"{length:<3} | {'*' * count:<{max_occurrences_width}} | {count:<3}")
