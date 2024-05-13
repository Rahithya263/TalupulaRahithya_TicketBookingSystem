from abc import abstractmethod, ABC


class BookingSystem(ABC):
    @abstractmethod
    def create_event(self, event):
        pass

    @abstractmethod
    def book_tickets(self, event_id, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_available_seats(self, event_id):
        pass
