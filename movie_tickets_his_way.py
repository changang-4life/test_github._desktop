
def sell_ticket():
    """ Component 1 of project: Welcome screen and set up variables """
    
    print("************* Fanfare Movies - Ticketing System *************")
    
    print('Welcome to Fanfare Movies')
    
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0
    
    """ Component 2 of project: Get caregory and number of tickets required """
    
    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What type of ticket do you want? Enter: \n\
                        \t'A' for Adult, or \n\
                        \t'S' for Student, or \n\
                        \t'C' for Child, or \n\
                        \t'G' for Gift Voucher\n\
                        >> ").upper()
        
    num_tickets = int(input(f"How many {ticket_type} tickets do you want:"))
    
    print(f"\n You have ordered {num_tickets} {ticket_type} tickets(s)! ")
    
    ticket_wanted = input("Do you want to order another ticket (Y / N ): ").upper()
    
sell_ticket()