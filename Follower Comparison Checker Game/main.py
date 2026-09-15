class User:
    """Class name first letter should always be capital"""
#     # pass  #this is a empty class
     

# user_1 = User()          # here we created our first object
# user_1.id = "376"              # here we created our first Attributr
# user_1.name = "Yogeshwar"
# print(user_1.name)

# user_2 = User()          # here we created our first object
# user_2.id = "378"              # here we created our first Attributr
# user_2.name = "Yogesh"
# print(user_2.name)
    def __init__(self, user_id,username):   # Constructer - initialized, now whenever a new object is being constructed by this class this function will automatically called.
        print("when ever a new user is created") 
        self.id = user_id
        self.name = username
        self.followers = 0 #it is not always necessary to pass our value of attribute, some time also created attribute and intialize inside the fuction also which we need to start at certain point but after some time we need to modify it.
        self.following = 0
    def follow(self, user):
        self.following += 1
        user.followers += 1
user_1 = User("372","Yogeshwar")
print(user_1.id)
user_2 = User("376","Yogesh")
print(user_2.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
