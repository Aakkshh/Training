class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"Title: \"{self.title}\", Director: \"{self.director}\", Rating: {self.rating}"

title = "Inception"
director = "Christopher Nolan"
rating = 8.8
movie = Movie(title, director, rating)

print(movie)  
