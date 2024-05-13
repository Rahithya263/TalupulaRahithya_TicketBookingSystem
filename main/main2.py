def calculate_ticket_cost(ticket_type, num_tickets):
    base_price = 0
    if ticket_type == "Silver":
        base_price = 50
    elif ticket_type == "Gold":
        base_price = 100
    elif ticket_type == "Diamond":
        base_price = 150
    else:
        print("Invalid ticket type!")
        return None

    total_cost = base_price * num_tickets
    return total_cost

def book_tickets_loop():
    while True:
        ticket_type = input("Enter the ticket type (Silver/Gold/Diamond) or type 'Exit' to quit: ").capitalize()
        if ticket_type == "Exit":
            print("Exiting ticket booking system...")
            break

        num_tickets = int(input("Enter the number of tickets you want to book: "))
        if num_tickets <= 0:
            print("Invalid number of tickets. Please enter a positive integer.")
            continue

        total_cost = calculate_ticket_cost(ticket_type, num_tickets)
        if total_cost is not None:
            print("Total cost for", num_tickets, ticket_type, "tickets:", total_cost)

if __name__ == "__main__":
    book_tickets_loop()
