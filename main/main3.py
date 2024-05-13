def book_tickets(available_tickets, no_of_booking_tickets):
    if available_tickets >= no_of_booking_tickets:
        remaining_tickets = available_tickets - no_of_booking_tickets
        print("Tickets booked successfully!")
        print("Remaining tickets:", remaining_tickets)
    else:
        print("Sorry, tickets not available for the requested quantity.")

def main():
    try:
        available_tickets = int(input("Enter the number of available tickets: "))
        no_of_booking_tickets = int(input("Enter the number of tickets you want to book: "))

        if available_tickets < 0 or no_of_booking_tickets < 0:
            print("Invalid input. Please enter positive integers for available tickets and booking tickets.")
        else:
            book_tickets(available_tickets, no_of_booking_tickets)
    except ValueError:
        print("Invalid input. Please enter valid integers for available tickets and booking tickets.")

if __name__ == "__main__":
    main()
