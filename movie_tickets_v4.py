
""" Movie theatre ticketing system - v4
Confirm order"""

def confirm_order(ticket, number, cost):
    """ Confirms ticket order """
    confirm = ''
    while confirm != 'Y' and confirm != 'N':
        confirm = input(f"\n You have ordered {number} {ticket} ticket(s) at a cost of ${cost * number:.2f}\n 'Y'")
    if confirm == 'Y':
        return True
    else:
        return False                  


def get_price(type_):
    """ Calculates price """
    
    prices = [['A', 12.5], ['C', 7], ['S', 9], ['G', 0]]
    for price in prices:
        if price [0] == type_:
            return price[1]

def sell_ticket():
    """Component 1 of project: Welcome screen and set up variables"""
    
    print('************* Fanfare Movies - Ticketing System *************')
    
    print('Welcome to Fanfare Movies.')
    
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0
    
    """ Component 2 Get category and number of tickets required """
    ticket_wanted = "Y"
    while ticket_wanted == 'Y':
        ticket_type = input("What type of ticket do you want: \n\
                            \t 'A' is for Adult, or \n\
                            \t 'S' is for Student, or \n\
                            \t 'C' is for Child, or \n\
                            \t 'G' is for Gift Voucher \n\
                            >> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want?: "))
        cost = get_price(ticket_type)
    
        if confirm_order(ticket_type, num_tickets, cost):
            print("Order confirmed")
        else:
            print("Order cancelled")
                        
        ticket_wanted = input("Do you want to order another ticket? (Y / N): ").upper()
    
# Main routine
sell_ticket()