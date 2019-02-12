print('Thank you very much for dining with us this evening.')
my_name = input('I trust your service was impeccable Mr...? ')
print(f'''Ah, Mr. {my_name}. I hope everything was to your satisfaction.  If it
wasn't, you can make sure to hit them where it really hurts!  Their tip!''')
total_cost = float(input('Now, how much was the total for your dinner? '))
tip_percent = float(input(f'''This should be interesting...what percent tip would you
like to leave Mr. {my_name} '''))
print(f"Wonderful Mr. {my_name}.")

def tip_calculator(total, percent):
    percent = percent / 100
    return ((total * percent) + total)

total_with_tip = tip_calculator(total_cost, tip_percent)

print(f"""You're total this evening Mr. {my_name} is {total_with_tip}. I do hope
you have a wonderful night and please visit us again!""")
