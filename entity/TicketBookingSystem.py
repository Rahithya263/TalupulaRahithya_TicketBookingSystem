from entity.Event import Event


class EventNotFoundException(Exception):
    pass

class InvalidBookingIDException(Exception):
    pass

class TicketBookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        event = Event(event_name, date, time, venue, total_seats, total_seats, ticket_price, event_type)
        self.events.append(event)

        print("Event created successfully!")

    def book_tickets(self, event_id, num_tickets):
        event = self.get_event(event_id)
        if event:
            if event.available_seats >= num_tickets:
                # Book tickets for the event
                event.book_tickets(num_tickets)
                print(f"{num_tickets} tickets booked for event {event.event_name}.")
            else:
                raise EventNotFoundException("Event not found.")
        else:
            raise InvalidBookingIDException("Invalid booking ID.")

    def cancel_booking(self, booking_id):
        if 0 <= booking_id < len(self.bookings):
            booking = self.bookings[booking_id]
            event = booking.event
            event.cancel_booking(booking.num_tickets)
            print("Booking canceled successfully.")
        else:
            raise InvalidBookingIDException("Invalid booking ID.")

    def get_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None