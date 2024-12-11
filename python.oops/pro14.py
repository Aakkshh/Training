class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  
    def get_password(self):
       
        return "******"

    def set_password(self, new_password):
       
        if len(new_password) >= 6: 
            self.__password = new_password
        else:
            raise ValueError("Password must be at least 6 characters long")

    def __str__(self):
        return f"username: {self.username}, password: {self.get_password()}"


user = User(username="john_doe", password="secure123")

print(user)  
