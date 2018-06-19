## Made by: Hugo Rodriguez
## My Social Network

class User:
    def __init__(self, username):
        self.username = username
##        self.firstName = " "
##        self.lastName = " "
##        self.bio = " "
        self.friends = []
        self.posts = []

    def addPost(self, post):
        self.posts.append(post)

    def addFriend(self, human):
        self.friends.append(human)

    def unFriend(self, person):
                self.friends.remove(person)

    def showUsernames(self):
        for friend in self.friends:
            print (friend.username)

##    def addFirstName(self, firstName):
##        self.firstName = firstName
##
##    def addLastName(self, lastName):
##        self.lastName = lastName
##
##    def addBio(self, bio):
##        self.bio = bio

    def viewNewsFeed(self, friends):
        for friend in self.friends:
            print(friend.posts)
            


if __name__ == "__main__":
##    firstName = "Hugo"
##    lastName = "Rodriguez"
    username = "JuiceIsNoice"
##    bio = "Sup I'm noice"
##    userID = "0000"

    hugo = User(username)
    obama = User("TheRockObama")
    mojojojo = User("Mojo-Jojo")
    chuck = User("CoolChuck123")

    hugo.addFriend(obama)
    hugo.addFriend(mojojojo)
    hugo.addFriend(chuck)
    hugo.showUsernames()
    obama.addPost("IM OBAMA")
    mojojojo.addPost("I WILL TAKE OVER THE WORLD MWUAHAHAHAHA")
    chuck.addPost("Y0 I'm c00l3st chuck 4live g0t m0n3y 4 d4yz")
    hugo.viewNewsFeed(hugo.friends)
    hugo.unFriend(chuck)
    hugo.showUsernames()


##    hugo.unFriend(User("mojojojo"))
    #hugo.showUsernames()
##    hugo.addFirstName("Hugo")
##    hugo.addLastName("Rodriguez")
##    hugo.addBio("Noice")


##            print(lucy.firstName, lucy.lastName)
##            lucy.posts.append("THIS IS NOICENESS")
##            print(lucy.posts)
##
##            print(mojojojo.firstName, mojojojo.lastName)
##            mojojojo.posts.append("I WILL TAKE OVER THE WORLD")
##            print(mojojojo.posts
