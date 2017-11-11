import os
import app
import json

class User:

    def __init__(self, user, username, password, cap=15):
        """
        Initializer for the class
        """
        cap = 15; #50 images is the upper limit
        args = {'username': [user], 'media_types': ['none'], 'media_metadata': False, 'usernames': [user], 'verbose': 0, 'maximum': cap, 'login_user': username, 'login_only': False, 'destination': './', 'quiet': False, 'comments': True, 'filename': None, 'filter': None, 'search_location': False, 'tag': False, 'location': False, 'login_pass': password, 'retain_username': False, 'include_location': False, 'latest': False}
        scraper = app.start(args)
        scraper.scrape()
        scrap =  json.dumps(scraper.posts, indent=4, sort_keys=True, ensure_ascii=False)
        self.json = json.loads(scrap)
        self.pic = scraper.profilepic
        #rint self.json
        #print json.dumps(self.json, indent=4)


    def isValidUser(self):
        return not self.json is None

    def getProfilePicture(self):
        return self.pic

if __name__ == "__main__":
    user = User("0lonestar", "chrisdfisch", "passwd")
    print (user.json)
    for image in user.json:
        comments = image['comments']['data']
        print (image['edge_media_to_caption']['edges'][0]['node']['text'])

