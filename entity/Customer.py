
class Customer:
    def __init__(self, customer_name, email, phone_number):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)
