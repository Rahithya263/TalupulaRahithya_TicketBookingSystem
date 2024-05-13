from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    @abstractmethod
    def display_event_details(self):
        pass

    @abstractmethod
    def book_tickets(self, num_tickets):
        pass

    @abstractmethod
    def cancel_booking(self, num_tickets):
        pass

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        print("Event Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Genre:", self.genre)
        print("Actor Name:", self.actor_name)
        print("Actress Name:", self.actress_name)

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Insufficient seats available.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")

class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, artist, event_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price)
        self.artist = artist
        self.event_type = event_type

    def display_event_details(self):
        print("Event Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Artist:", self.artist)
        print("Event Type:", self.event_type)

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Insufficient seats available.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")

class Sport(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print("Event Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Sport Name:", self.sport_name)
        print("Teams Name:", self.teams_name)

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.event_name}.")
        else:
            print("Insufficient seats available.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")
