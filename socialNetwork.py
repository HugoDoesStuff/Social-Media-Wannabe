## Made by: Hugo Rodriguez
## My Social Network

class User:
    def __init__(self, username, userID):
        self.username = username
##        self.firstName = " "
##        self.lastName = " "
##        self.bio = " "
        self.friends = []
        self.posts = []
        self.userID = userID

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

    def addPost(self, content):
        self.postContent = content

    def createPost(self, content):
         myPost = posts(content)
         self.posts.append(myPost)
         myPost.createPostID(len(posts))

    def createUserID(self, num):
        self.postID = num

class Post:
    def __init__(self, content):

        self.content = content
        self.postID = " "
        self.comments = []

    def createPostID(self, num):
        self.postID = num


class Network:
    def __init__(self):
        self.users = []
    
    def createUser(self, username):
        
        mySize = int(len(self.users))+1
        myUser = User(username, mySize)
##        myUser.createUserID(mySize)
        self.users.append(myUser)
        print(len(self.users))
        
        print("USER CREATED")
    
    def addConnection(self, user1, user2):
        user1OBJ = self.getOBJ(user1)
        user2OBJ = self.getOBJ(user2)

        user1OBJ.addFriend(user2OBJ)
        user2OBJ.addFriend(user1OBJ)

    def getOBJ(self, username):
        userID = self.getUserID(username)
        userOBJ = self.users[userID-1]
        print(userOBJ.username)
        return userOBJ

    def getUserID(self, username):
        for i in self.users:
            if i.username == username:
                return i.userID

if __name__ == "__main__":
##    firstName = "Hugo"
##    lastName = "Rodriguez"
##    username = "JuiceIsNoice"
##    bio = "Sup I'm noice"
##    userID = "0000"
    network = Network()
    network.createUser("JuiceIsNoice")
    network.createUser("HI")
    network.createUser("diana")
    diana = network.getOBJ("diana")
    juice = network.getOBJ("JuiceIsNoice")
    hi = network.getOBJ("HI")
    
    
    
    #juice = network.getOBJ("JuiceIsNoice")
##    obama = network.getOBJ("TheRockObama")
##    mojojojo = network.getOBJ("Mojo-Jojo")
    
    
    

##    hugo = User(username)
##    obama = User("TheRockObama")
##    mojojojo = User("Mojo-Jojo")
##    chuck = User("CoolChuck123")

##    hugo.addFriend(obama)
##    hugo.addFriend(mojojojo)
##    hugo.addFriend(chuck)
##    hugo.showUsernames()
##    obama.createPost("IM OBAMA")
##    mojojojo.createPost("I WILL TAKE OVER THE WORLD MWUAHAHAHAHA")
##    chuck.createPost("Y0 I'm c00l3st chuck 4live g0t m0n3y 4 d4yz")
##    hugo.viewNewsFeed(hugo.friends)
##    hugo.unFriend(chuck)
##    hugo.showUsernames()


##    hugo.unFriend(User("mojojojo"))
##    hugo.showUsernames()
##    hugo.addFirstName("Hugo")
##    hugo.addLastName("Rodriguez")
##    hugo.addBio("Noice")


##    print(lucy.firstName, lucy.lastName)
##    lucy.posts.append("THIS IS NOICENESS")
##    print(lucy.posts) 
## 
##    print(mojojojo.firstName, mojojojo.lastName)
##    mojojojo.posts.ap pend("I WILL TAKE OVER THE WORLD")
##    print(mojojojo.posts       
