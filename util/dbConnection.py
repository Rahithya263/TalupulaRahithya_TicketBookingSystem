import mysql.connector

class DBConnection:
    @staticmethod
    def getconnection():
        host = 'localhost'
        database = 'TicketBookingSystem'
        user = 'root'
        password = 'Radhi1234'
        try:
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if conn.is_connected():
                print('DB is Connected')
                return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None


class PropertyUtil:
    @staticmethod
    def getpropertystring():
        return DBConnection.getconnection()

