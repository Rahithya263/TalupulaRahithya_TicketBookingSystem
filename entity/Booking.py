
class Booking:
    def __init__(self):
        self.customers = []
        self.event = self.event
        self.total_cost = 0

    def calculate_booking_cost(self, num_tickets):
        self.total_cost = num_tickets * self.event.ticket_price

    def book_tickets(self, num_tickets):
        if self.event.book_tickets(num_tickets):
            self.calculate_booking_cost(num_tickets)
            return True
        else:
            return False

    def cancel_booking(self, num_tickets):
        self.event.cancel_booking(num_tickets)

    def get_available_no_of_tickets(self):
        return self.event.available_seats

    def get_event_details(self):
        return self.event