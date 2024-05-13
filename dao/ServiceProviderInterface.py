# dao/ServiceProviderInterface.py
from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class IBookingSystemServiceProvider(ABC):
    @abstractmethod
    def calculate_booking_cost(self, num_tickets):
        pass

    @abstractmethod
    def book_tickets(self, event_name, num_tickets, array_of_customer):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass


class ServiceProviderInterface(ABC):
    @abstractmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        pass

    @abstractmethod
    def book_tickets(self, event_id, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass
