import os
import app
import json

class User:

    def __init__(self, user, username, password, cap=15):
        """
        Initializer for the class
        """
        cap = 30; #50 images is the upper limit
        args = {'username': [user], 'media_types': ['none'], 'media_metadata': False, 'usernames': [user], 'verbose': 0, 'maximum': cap, 'login_user': username, 'login_only': False, 'destination': './', 'quiet': False, 'comments': True, 'filename': None, 'filter': None, 'search_location': False, 'tag': False, 'location': False, 'login_pass': password, 'retain_username': False, 'include_location': False, 'latest': False}
        self.scraper = app.start(args)
        self.json = json.loads(self.scraper)
        #rint self.json
        #print self.json


    def isValidUser(self):
        return not self.json is None

    def getImages(self):
        #TODO
        pass


    def getProfilePicture(self):
        #TODO
        pass

    def getComments(self):
        #TODO
        pass

if __name__ == "__main__":
    user = User("0lonestar", "chrisdfisch", "passwd")
    print (user.json)
    for image in user.json:
        comments = image['comments']['data']
        print (image['edge_media_to_caption']['edges'][0]['node']['text'])
        return self.json is None

