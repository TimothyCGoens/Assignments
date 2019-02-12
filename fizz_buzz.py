print("Welcome back everyone!  It's now time for the lighting round of FIZZ or BUZZ!")
print("""For those of you following at home, it's simple.  Our contestants need
to give us a number that is either divisible by 3, by 5, or by both!""")
name = input("First up, why don't you tell us your name? ")
print(f"""Well {name}, I hope you are ready to go, because the timer starts right
NOW! """)
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FIZZBUZZ")
elif number % 5 == 0:
    print("BUZZ")
elif number % 3 == 0:
    print("FIZZ!!")
else:
    print("Sorry, you lose!")
