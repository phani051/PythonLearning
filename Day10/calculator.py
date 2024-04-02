from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return (n1 - n2)

# Multiply


def multiply(n1, n2):
    return (n1 * n2)

# Devide


def devide(n1, n2):
    return (n1/n2)

print(logo)


def calculator():

    n1 = float(input("What's the first number?: "))

    operation = {'+': add, '-': subtract,
                 '*': multiply, '/': devide}

    for i in operation:
        print(i)

    cal_more = True

    while cal_more:
        user_choice = input("Pick operation: ")
        n2 = float(input("What's the next number? "))
        calculation = operation[user_choice]
        answer = calculation(n1, n2)
        print(f"{n1} {user_choice} {n2} = {answer}")
        n1 = answer
        cal_continue = input("Continue with calculations with previous answer(y), start fresh calculations(n) and (q) for quit: ").lower()
        if cal_continue == 'n':
            cal_more = False
            calculator()
        elif cal_continue == 'y':
            cal_more = True
        elif cal_continue == 'q':
            break
calculator()
