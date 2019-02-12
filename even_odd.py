print("""Let's play a game of even/odds!  It's really easy to play.  You give
me a number, and I'll tell you if it's odd or even!""")

number = int(input("What is your first number? "))

def even_odd(num):
    if num % 2 == 0:
        print("EVEN!")
    else:
        print("ODD!")

answer = even_odd(number)

#play_again = input('Would you like to play again? Y/N? ')

#if play_again == 'Y':
#    number = input("Awesome!  What is your new number?")
#    even_odd(number)
