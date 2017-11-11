import os


class User:

    def __init__(self, user, username, password):
        """
        Initializer for the class
        """
        cap = 50; #50 images is the upper limit
        inputs = {"user" : user, "capacity" : cap, "username" : username, "password" : password}
        command = "instagram-scraper {user} -m {capacity} -t image --media-metadata -u {username} -p {password}".format(**inputs)
        os.system(command)
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.dest_path = self.dir_path + "/" + user


    def isValidUser(self):
        """Returns true if the user exsists"""
        return os.path.isdir(self.dest_path)


    def getImages(self):
        """
        Queries the images from instagram and puts it in api/{user}.
        Function returns a list of image locations
        """
        cap = 50; #50 images is the upper limit
        files = os.listdir(self.dest_path) # returns list
        files = [self.dest_path + "/" + x for x in files if x.endswith(".jpg")]
        return files


    def getProfilePicture(self):
        """
        Queries the images from instagram and puts it in api/{user}.
        Function returns a list of image locations
        """

    def getComments(self):
        


user = User("jhuanghuang", "puss_dragon8", "passwd")
print user.getImages()