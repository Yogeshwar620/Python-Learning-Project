auction = {}
should_continue = True
while should_continue:
    name = input("What is your name: ")
    price = int(input("What's your bid: $"))
    auction[name] = price
    yes_or_no = input("Are there any other bidder's? Type 'yes' or 'no': ").lower()
    if yes_or_no == "no":
        should_continue = False
    elif yes_or_no == "yes":
        print("\n" * 50)
winner = 0
name = ""
for key in auction:
    if auction[key] > winner:
        winner = auction[key]
        name = key
print(f"Winner of this bid is {name} with the bidding amount of ${winner}")
