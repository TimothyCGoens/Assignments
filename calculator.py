
first_number = int(input("Please enter a number: "))
operator = input("Please enter a math operator: ")
second_number = int(input("Please enter a second number: "))



def add(num1, num2):
    return num1 + num2

add_answer = add(first_number, second_number)


def sub(num1, num2):
    return num1 - num2

sub_answer = sub(first_number, second_number)


def multi(num1, num2):
    return num1 * num2

multi_answer = multi(first_number, second_number)


def division(num1, num2):
    return num1 / num2

division_answer = division(first_number, second_number)


if operator == '-':
    print(sub_answer)
elif operator == '+':
    print(add_answer)
elif operator == '*':
    print(multi_answer)
elif operator == '/':
    print(division_answer)
else:
    print("error")
