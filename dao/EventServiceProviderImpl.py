import mysql.connector
from dao.ServiceProviderInterface import ServiceProviderInterface
from util.dbConnection import PropertyUtil

class EventServiceProviderImpl:
    def __init__(self, connection_string):
        self.events = None
        self.connection_string = connection_string
        self.conn = self.get_database_connection()

    def get_database_connection(self):
        try:
            conn = mysql.connector.connect(**self.connection_string)
            if conn.is_connected():
                print('DB is Connected')
                return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None


    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        try:
            cursor = self.conn.cursor()
            sql_query = "INSERT INTO Event (event_name, date, time, total_seats, available_seats, ticket_price, event_type, venue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (event_name, date, time, total_seats, total_seats, ticket_price, event_type, venue))
            self.conn.commit()
            cursor.close()
            print("Event created successfully and stored in the database.")
        except mysql.connector.Error as error:
            print("Error creating event:", error)

    def book_tickets(self, event_id, num_tickets):
        try:
            conn = self.get_database_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT available_seats FROM Event WHERE event_id = %s", (event_id,))
            result = cursor.fetchone()
            if result:
                available_seats = result[0]
                if available_seats >= num_tickets:
                    new_available_seats = available_seats - num_tickets
                    cursor.execute("UPDATE Event SET available_seats = %s WHERE event_id = %s",
                                   (new_available_seats, event_id))
                    cursor.execute("INSERT INTO Booking (event_id, num_tickets) VALUES (%s, %s)",
                                   (event_id, num_tickets))
                    conn.commit()
                    print(f"{num_tickets} tickets booked successfully.")
                else:
                    print("Not enough available seats.")
            else:
                print("Event not found.")
            cursor.close()
            conn.close()
        except mysql.connector.Error as error:
            print("Error booking tickets:", error)

    def cancel_booking(self, booking_id):
        try:
            conn = self.get_database_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Booking WHERE booking_id = %s", (booking_id,))
            conn.commit()
            print("Booking cancelled successfully.")
            cursor.close()
            conn.close()
        except mysql.connector.Error as error:
            print("Error cancelling booking:", error)

    def get_event_details(self):
        return self.events

    def get_available_no_of_tickets(self):
        available_tickets = sum(event['available_seats'] for event in self.events)
        return available_tickets
