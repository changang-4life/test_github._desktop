# Movie theatre ticketing system - v1
# Welcome screen and initialise variables



def welcome():
    # Component 1 of project: Welcome screen and set up variables
    
    print("************ Fanfare Movies - Ticketing System ************\n")

adult_tickets = 0
student_tickets = 0
child_tickets = 0
gift_tickets = 0
    
total_tickets = 0
total_sales = 0 # (total sales)


# Component 2 of project: Get details of sale
def show_categories():
    
    available_categories = ['Adult tickets', 'Student tickets', 'Child tickets', 'Gift tickets']
    
    print("Available tickets categories are:")
    for category in available_categories:
        print('- ',category)
    print()
       
 
def ask_ticket_num(): 
    user_ticket_input = int(input("Please enter the amount of tickets you would like: "))
    return user_ticket_input

def ask_ticket_type():
    ticket_type = str(input("Please enter the type of ticket you would like (i.e., 'Adult', 'Gift'):\n"))
    return ticket_type

welcome()
show_categories()
ticket_type = ask_ticket_type().capitalize()

# Component 3 of project: Calculate Price
def price_calculator():
    if ticket_type == 'Adult':
        price = adult_price * ticket_num
        return price
    
    if ticket_type == 'Student':
        price = student_price * ticket_num
        return price
    
    if ticket_type == 'Child':
        price = child_price * ticket_num
        return price
        


adult_price = 20
student_price = 15
child_price = 5


# Main routine  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


ticket_num = ask_ticket_num()

price = price_calculator()

# Component 4 of project: Get Confirmation + Component 5 of project: Update the Totals

print(f'You would like {ticket_num} {ticket_type} tickets for ${price}.')
user_confirmation = str(input('Confirm order?: (Y / N): '))

if user_confirmation.capitalize() == 'Y':
    total_sales += price
    total_tickets += ticket_num
    
    if ticket_type == 'Adult':
        adult_tickets += ticket_num
        
    if ticket_type == 'Student':
        student_tickets += ticket_num
        
    if ticket_type == 'Child':
        child_tickets += ticket_num
        
# Component 6 of project: Ask for next sale or user quits
    
