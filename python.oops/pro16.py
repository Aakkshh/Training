class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def display_details(self):
        print(f"Address: \"{self.address}\", Number of Rooms: {self.num_rooms}, Price: {self.price}")


house = House(address="456 Elm St", num_rooms=4, price=350000)

house.display_details() 
