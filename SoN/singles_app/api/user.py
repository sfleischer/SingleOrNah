import os
import app
import json

class User:

    def __init__(self, user, username, password):
        """
        Initializer for the class
        """
        cap = 15; #50 images is the upper limit
        args = {'username': [user], 'media_types': ['none'], 'media_metadata': False, 'usernames': [user], 'verbose': 0, 'maximum': cap, 'login_user': username, 'login_only': False, 'destination': './', 'quiet': False, 'comments': True, 'filename': None, 'filter': None, 'search_location': False, 'tag': False, 'location': False, 'login_pass': password, 'retain_username': False, 'include_location': False, 'latest': False}
        self.scraper = app.start(args)
        self.json = json.loads(self.scraper)
        #print self.json


    def isValidUser(self):
        #TODO
        pass


    def getImages(self):
        #TODO
        pass


    def getProfilePicture(self):
        #TODO
        pass

    def getComments(self):
        #TODO
        pass


user = User("jhuanghuang", "puss_dragon8", "passwd")
