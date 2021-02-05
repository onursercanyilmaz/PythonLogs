class User:
    def __init__(self, userid, username):
        #initiliazing... constructor
        #print("object has created!")
        self.userid = userid
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1



user1 = User("001", "osy")
user2 = User("002", "yso")
print(f"{user1.username}, follower: {user1.follower}, following : {user1.following}")
print(f"{user2.username}, follower: {user2.follower}, following : {user2.following}")

user1.follow(user2)

print(f"{user1.username}, follower: {user1.follower}, following : {user1.following}")
print(f"{user2.username}, follower: {user2.follower}, following : {user2.following}")
"""
it is very error prone
user1 = User()
user1.id = "001"
user1.name = "onur"

user2 = User()
user2.id = "002"
user2.name = "sercan"

print(user1.id)
print(user2.name)

"""