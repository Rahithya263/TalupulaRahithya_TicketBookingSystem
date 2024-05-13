from entity.TicketBookingSystem import TicketBookingSystem
from exception.myexceptions import EventNotFoundException, InvalidBookingIDException
from entity.Event import Event
from entity.Event import EventType
from dao.EventServiceProviderImpl import EventServiceProviderImpl

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats,
                 ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats,
                         ticket_price, EventType.MOVIE)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print("Genre:", self.genre)


class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats,
                 ticket_price, artist, type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats,
                         ticket_price, EventType.CONCERT)
        self.artist = artist
        self.type = type

    def display_event_details(self):
        super().display_event_details()
        print("Artist:", self.artist)


class Sports(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats,
                 ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats,
                         ticket_price, EventType.SPORTS)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print("Sport:", self.sport_name)


class TicketBookingSystem:
    def __init__(self):
        # Replace the connection string with your actual database connection details
        connection_string = {
            'host': 'localhost',
            'database': 'TicketBookingSystem',
            'user': 'root',
            'password': 'Radhi1234'
        }
        self.events_dao = EventServiceProviderImpl(connection_string)  # Instantiate the DAO class

    # Other methods of TicketBookingSystem...

    def create_event(self, event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name):
        event = None
        if event_type == "Movie":
            event = Movie(event_name, event_date, event_time, venue_name, total_seats, total_seats,
                          ticket_price, "Action", "Actor", "Actress")
        elif event_type == "Concert":
            event = Concert(event_name, event_date, event_time, venue_name, total_seats, total_seats,
                            ticket_price, "Artist", "Theatrical")
        elif event_type == "Sports":
            event = Sports(event_name, event_date, event_time, venue_name, total_seats, total_seats,
                           ticket_price, "Football", "India vs Pakistan")
        else:
            print("Invalid event type!")
            return None

        # Store the event in the database using the DAO
        if event:
            success = self.events_dao.create_event(event)
            if success:
                print("Event created successfully!")
                return event
            else:
                print("Failed to create event in the database.")
                return None

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        if event.available_seats >= num_tickets:
            event.available_seats -= num_tickets
            total_cost = event.ticket_price * num_tickets
            print(f"Tickets booked successfully! Total cost: {total_cost}")  # New line added
            return total_cost
        else:
            print("Not enough available seats.")
            return None

    def cancel_tickets(self, event, num_tickets):
        event.available_seats += num_tickets
        print("Tickets cancelled.")

    def main(self):
        while True:
            print("1. Create Event")
            print("2. Display Event Details")
            print("3. Book Tickets")
            print("4. Cancel Tickets")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                event_name = input("Enter event name: ")
                event_date = input("Enter event date: ")
                event_time = input("Enter event time: ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Concert/Sports): ")
                venue_name = input("Enter venue name: ")
                self.create_event(event_name, event_date, event_time, total_seats, ticket_price, event_type, venue_name)
            elif choice == "2":
                for event in self.events:
                    self.display_event_details(event)
            elif choice == "3":
                if not self.events:
                    print("No events available. Please create an event first.")
                else:
                    event_index = int(input("Enter event index: "))
                    if event_index < 0 or event_index >= len(self.events):
                        print("Invalid event index.")
                    else:
                        num_tickets = int(input("Enter number of tickets: "))
                        total_cost = self.book_tickets(self.events[event_index], num_tickets)
                        if total_cost:
                            print(f"Total cost: {total_cost}")

            elif choice == "4":
                event_index = int(input("Enter event index: "))
                num_tickets = int(input("Enter number of tickets to cancel: "))
                self.cancel_tickets(self.events[event_index], num_tickets)
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the ticket booking system
if __name__ == "__main__":
    ticket_system = TicketBookingSystem()
    ticket_system.main()
