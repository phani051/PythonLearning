# Class creation
class User:
    # Attributes
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating Object using Class
user1 = User(5, "Phani")


print(user1.id, user1.username, user1.followers)
user1.follow(user1)
print(user1.username, user1.followers, user1.following)
