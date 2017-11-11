import os
import app
import json

class User:

    def __init__(self, user, username, password, cap=15):
        """
        Initializer for the class
        """
        args = {'username': [user], 'media_types': ['none'], 'media_metadata': False, 'usernames': [user], 'verbose': 0, 'maximum': cap, 'login_user': username, 'login_only': False, 'destination': './', 'quiet': False, 'comments': True, 'filename': None, 'filter': None, 'search_location': False, 'tag': False, 'location': False, 'login_pass': password, 'retain_username': False, 'include_location': False, 'latest': False}
        self.scraper = app.start(args)
        self.json = json.loads(self.scraper)
        #rint self.json
        #print self.json


    def isValidUser(self):
        return self.json is None

user = User("jhuanghuang", "puss_dragon8", "passwd", cap=1)
