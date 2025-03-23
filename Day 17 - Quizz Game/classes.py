class User:
    # constructor
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Jill")
print(user_1.id)
print(user_1.followers)
user_2 = User("002", "Jack")
user_1.follow(user_2)
print(user_1.following)