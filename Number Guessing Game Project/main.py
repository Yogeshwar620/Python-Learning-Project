from art import logo
import random
value_num = random.randint(1,100)
print(logo)
gus = random.choice(value_num)
# for _ in range(1,100):
#     gus =
print("""Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.""")
diff = input("Choose a difficulty type: easy or hard: ")

if diff == "easy":
    attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number:")
    for num in range(1, 11):
        guess = int(input("Guess the number: "))
        if guess < gus:
            attempt -= 1
            print("Too low")
            print(f"You have {attempt} attempts remaining to guess the number:")
        elif guess > gus:
            attempt -= 1
            print("Too high")
            print(f"You have {attempt} attempts remaining to guess the number:")
        else:
            print(f"You got it! The answer was {guess}")
            break
else:
    attempt = 5
    print(f"You have {attempt} attempts remaining to guess the number:")
    for num in range(1, 6):
        guess = int(input("Guess the number: "))
        if guess < gus:
            attempt -= 1
            print("Too low")
            print(f"You have {attempt} attempts remaining to guess the number:")
        elif guess > gus:
            attempt -= 1
            print("Too high")
            print(f"You have {attempt} attempts remaining to guess the number:")
        else:
            print(f"You got it! The answer was {guess}")
