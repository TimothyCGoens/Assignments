print('Hello there!  My name is App the Adding Wizard!')
print('You can call me App for short.')
my_name = input('What is your name? ')
print(f'I can take any two numbers you give me {my_name} and PRESTO, add them together!')
first_number = int(input(f'What is your first number {my_name}? '))
print('Hmmm, that is a most curious choice.')
second_number = int(input(f'Okay, {my_name} what is your second number? '))
print('That is an excellent choice if I do say so myself!')
print('Now for me to work my magic, literally!')

def add_two_numbers(num1, num2):
    return num1 + num2

answer = add_two_numbers(first_number, second_number)

print(f'ALAKAZAM! Your answer is {answer}!')
