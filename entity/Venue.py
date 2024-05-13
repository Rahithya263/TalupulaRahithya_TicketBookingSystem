class Venue:
    def __init__(self, venue_name, venue_address):
        self.venue_name = venue_name
        self.venue_address = venue_address

    def print_info(self):
        print(f"Venue: {self.venue_name}\nAddress: {self.venue_address}")

    def display_venue_details(self):
        print("Venue Name:", self.venue_name)
        print("Address:", self.address)

