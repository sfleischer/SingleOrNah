class UsersDict:
    def __init__(self):
        self.users = {}

    def incr_user_field_by(self, handle, field, incrBy):
        if not handle in self.users:
            self.users[handle] = {}

        if field in self.users[handle]:
            self.users[handle][field] += incrBy
        else:
            self.users[handle][field] = incrBy

    def append_user_field_with(self, handle, field, item):
        if not handle in self.users:
            self.users[handle] = {}

        if field in self.users[handle]:
            self.users[handle][field].append(item)
        else:
            self.users[handle][field] = [item]
            
    def get_user_dict(self, handle):
        return self.users[handle]

    def set_propic_url(self, handle, url):
        if not handle in self.users:
            self.users[handle] = {}
        self.users[handle]['profile_pic_url'] = url


if __name__ == '__main__':
    users = UsersDict()
    users.incr_user_field_by('chris', 'num_tags', 1)