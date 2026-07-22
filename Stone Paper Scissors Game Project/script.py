import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice ==2:
    print(scissors)
else:
    print("Wrong Choice")


print("Computer Choice:")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


if user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == computer_choice:
    print("Draw")
else:
    print("You lose")
