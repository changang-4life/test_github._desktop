
""" Movie theatre ticketing system - v2
Get category and number of tickets required
"""

def sell_tickets():
    """Component 1 of project: Welcome screen and set up variables"""
    
    print('************* Fanfare Movies - Ticketing System *************')
    
    print('Welcome to Fanfare Movies.')
    
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0
    
    """ Component 2 Get vategory and number of tickets required """
    ticket_wanted = "Y"
    while ticket_wanted == 'Y':
        ticket_type = input("What type of ticket do you want: \n\
                            \t 'A' is for Adult, or \n\
                            \t 'S' is for Student, or \n\
                            \t 'C' is for Child, or \n\
                            \t 'G' is for Gift Voucher \n\
                            >> ").upper()
    
# Main routine
sell_tickets()