""" Movie theatre """

def integer_checker(question):
    number = ''
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("That was not a number")
    
    

""" Movie theatre ticketing system - v6
Print summary of tickets sold"""

def print_summary(tickets_sold, adult, student, child, gift, total):
    """ Summary of sales """
    print('=' * 40)
    print(f"The total tickets sold today was {tickets_sold}\n")
    print(f'This was made up of: \n \t{adult} tickets for adults; and\n \t{student} tickets for students; and\n \t{child} tickets for children; and \t{gift} gift vouchers\n Sales for the day came to ${total:.2f}')
    print('=' * 40)
    

def confirm_order(ticket, number, cost):
    """ Component 4 - Confirm ticket order """
    confirm = ''
    while confirm != 'Y' and confirm != 'N':
        confirm = input(f"\n You have ordered {number} {ticket} ticket(s) at a cost of ${cost * number:.2f}\n 'Y' or 'N' to confirm: ").upper()
    if confirm == 'Y':
        return True
    else:
        return False                  


def get_price(type_):
    """ Component 3 of project - Calculate price """
    
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
        valid_types = ['A', 'S', 'C', 'G']
        ticket_type = input("What type of ticket do you want: \n\
                            \t 'A' is for Adult, or \n\
                            \t 'S' is for Student, or \n\
                            \t 'C' is for Child, or \n\
                            \t 'G' is for Gift Voucher \n\
                            >> ").upper()
        if ticket_type not in valid_types:
            print('Not a valid ticket type')
        else:
            num_tickets = integer_checker((f"How many {ticket_type} tickets do you want?: "))
            cost = get_price(ticket_type)
        
            if confirm_order(ticket_type, num_tickets, cost):
                print("Order Confirmed")
                # Component 5 - Update Totals
                total_sales += cost
                tickets_sold += cost * num_tickets
                if ticket_type == 'A':
                    adult_tickets += num_tickets
                    
                elif ticket_type == 'S':
                    student_tickets += num_tickets
                    
                elif ticket_type == 'C':
                    child_tickets += num_tickets
                    
                elif ticket_type == 'G':
                    gift_tickets += num_tickets
            else:
                print("Order Cancelled")
                            
            ticket_wanted = input("Do you want to order another ticket? (Y / N): ").upper()
        
    print_summary(tickets_sold, adult_tickets, student_tickets, child_tickets, gift_tickets, total_sales)
    
# Main routine
sell_ticket()
print('Goodbye.\n Thanks for choosing Fanfare Movies')