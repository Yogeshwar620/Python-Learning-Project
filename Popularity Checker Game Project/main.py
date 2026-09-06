import random
from art import logo
from art import vs
from game_data import data
#print logo
print(logo)
# length = 1
name_a = ''
followers_a = 0
description_a = ''
country_a = ''
name_b = ''
followers_b = 0
description_b = ''
country_b = ''
score = 0
# first candidate name
def data_assign(document):
    global name_a
    global followers_a
    global description_a
    global country_a
    global name_b
    global followers_b
    global description_b
    global country_b
    global score
    a = random.choice(document)
    b = random.choice(document)
    while a == b:
        b = random.choice(document)
    name_a = a['name']
    name_b = b['name']
    followers_a = a['follower_count']
    followers_b = b['follower_count']
    description_a = a['description']
    description_b = b['description']
    country_a = a['country']
    country_b = b['country']
    print(f"{name_a}, a {description_a}, from {country_a}")
    print(vs)
    print(f"{name_b}, a {description_b}, from {country_b}")

data_assign(data)
user_choice = input("Who is more popular? Type 'A' or 'B': ").lower()

def compare(followers_a, followers_b):
    # global followers_a
    # global followers_b
    global user_choice
    if followers_a > followers_b:
        if user_choice == 'a':
            return True
        elif user_choice == 'b':
            return False
        else:
            return None
    elif followers_a < followers_b:
        if user_choice == 'a':
            return False
        elif user_choice == 'b':
            return True
        else:
            return None

value = compare(followers_a, followers_b)

def game():
    global user_choice
    global value
    data_assign(data)
    user_choice = input("Who is more popular? Type 'A' or 'B': ").lower()
    value = compare(followers_a, followers_b)

def sol():
    global score
    global value
    while True:
        if value:
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"Your Current Score is: {score}")
        else:
            print("\n" * 20)
            print(logo)
            print(f"Your Final Score is: {score}")
            break
        game()
sol()




