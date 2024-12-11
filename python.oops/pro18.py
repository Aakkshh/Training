class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def update_rating(self, new_rating):
        
        if 0 <= new_rating <= 5:
            self.rating = new_rating
        else:
            print("Rating must be between 0 and 5.")

    def display_details(self):
        print(f"Name: \"{self.name}\", Cuisine Type: \"{self.cuisine_type}\", Rating: {self.rating}")

restaurant = Restaurant(name="Sushi Place", cuisine_type="Japanese", rating=4.5)

restaurant.update_rating(4.8)  

restaurant.display_details()  
