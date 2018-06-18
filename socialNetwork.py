## Made by: Hugo Rodriguez
## My Social Network

class user:
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    def addFriend(self,username):
        self.friends.append(username)

##    def unFriend():

    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print (friends.posts)


   

if __name__ == "__main__":
    firstName = "Hugo"
    lastName = "Rodriguez"
    username = "JuiceIsNoice"
    bio = "Sup I'm noice"
    userID = "0000"

    hugo = user(firstName, lastName, username, bio, userID)
    lucy = user("Lucy", "Lucille", "lucygoosy", "I like geese", "0123")
    mojojojo = user("Mojo", "Jojo", "mojojojo", "I am mojo jojo", "1234")

    hugo.addFriend("lucygoosy")
    hugo.addFriend("mojojojo")
    print(hugo.friends)

    hugo.viewNewsFeed(username)

##            print(lucy.firstName, lucy.lastName)
##            lucy.posts.append("THIS IS NOICENESS")
##            print(lucy.posts)
##
##            print(mojojojo.firstName, mojojojo.lastName)
##            mojojojo.posts.append("I WILL TAKE OVER THE WORLD")
##            print(mojojojo.posts)

    

    
