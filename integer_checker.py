
def integer_checker(question):
    number = ''
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("That was not a number")
    
    
# Main routine
num_tickets = integer_checker("How many tickets?: ")
print(f"You have ordered {num_tickets} number of tickets.")