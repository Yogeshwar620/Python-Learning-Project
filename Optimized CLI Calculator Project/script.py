# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2
# def mul(n1, n2):
#     return n1 * n2
# def div(n1, n2):
#     return n1 / n2
# def mod(n1, n2):
#     return n1 % n2
#
# a = 0
# Move = True
# n1 = int(input("Enter 1st number: "))
# print("+/n-/n//n*/n%")
# opp = input("Enter a operator: ")
# n2 = int(input("Enter 2nd number: "))
# if opp == "+":
#     a = add(n1, n2)
# elif opp == "-":
#     a = sub(n1, n2)
# elif opp == "*":
#     a = mul(n1, n2)
# elif opp == "/":
#     a = div(n1, n2)
# elif opp == "%":
#     a = mod(n1, n2)
# print(f"The result is {a}")
#
#
# while Move:
#     cont = input("If you want to continiue calcution with the previous output the type 'y' else type 'n'")
#     if cont == 'n':
#         break
#     n1 = a
#     print("+/n-/n//n*/n%")
#     opp = input("Enter a operator: ")
#     n2 = int(input("Enter 2nd number: "))
#     if opp == "+":
#         a = add(n1, n2)
#     elif opp == "-":
#         a = sub(n1, n2)
#     elif opp == "*":
#         a = mul(n1, n2)
#     elif opp == "/":
#         a = div(n1, n2)
#     elif opp == "%":
#         a = mod(n1, n2)
#     print(f"The result is {a}")



#------------ Another Way To DO It ----------------------



def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2


operation ={
    "+": add,
    "-":sub,
    "*": mul,
    "/": div,
    "%": mod,
}

def calculator():
    should_accumulate = True
    num1 = float(input("Enter first number: "))

    while should_accumulate:

        for symbol in operation:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        num2 = float(input("Enter second number: "))
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = (input("type 'y' to continue calculation with previous answer, or type 'n' to start a new calculation"))
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*30)
            calculator()

calculator()
