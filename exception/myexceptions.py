
class EventNotFoundException(Exception):
    pass

class InvalidBookingIDException(Exception):
    pass

# Update TicketBookingSystem class to include exception handling
class TicketBookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        # Implementation to create event
        pass

    def book_tickets(self, event_name, num_tickets):
        # Check if event exists
        if event_name not in [event.event_name for event in self.events]:
            raise EventNotFoundException("Event not found.")

        # Implementation to book tickets
        pass

    def cancel_booking(self, booking_id):
        # Check if booking ID is valid
        if booking_id < 0 or booking_id >= len(self.bookings):
            raise InvalidBookingIDException("Invalid booking ID.")

        # Implementation to cancel booking
        pass

# Handle exceptions in the main method
def main():
    ticket_system = TicketBookingSystem()
    try:
        # Example usage triggering EventNotFoundException
        ticket_system.book_tickets("NonExistentEvent", 2)
    except EventNotFoundException as e:
        print("Error:", e)

    try:
        # Example usage triggering InvalidBookingIDException
        ticket_system.cancel_booking(-1)
    except InvalidBookingIDException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
