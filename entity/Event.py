from enum import Enum

class EventType(Enum):
    MOVIE = 'Movie'
    SPORTS = 'Sports'
    CONCERT = 'Concert'

class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = EventType(event_type)

    def calculate_total_revenue(self, num_tickets_sold):
        return num_tickets_sold * self.ticket_price

    def getBookedNoOfTickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Insufficient seats available.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")

    def print_info(self):
        print(f"Event: {self.event_name}\nDate: {self.event_date}\nTime: {self.event_time}")
        self.venue.print_info()
        print(
            f"Total Seats: {self.total_seats}\nAvailable Seats: {self.available_seats}\nTicket Price: {self.ticket_price}\nEvent Type: {self.event_type}")

    def display_event_details(self):
        print("Event Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Event Type:", self.event_type)