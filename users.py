class UsersDict:
    def __init__(self):
        self.users = {}

    def add_user(self, handle, dic={}):
        self.users[handle] = dic

    def incr_user_field_by(self, handle, field, incrBy):
        if (field in self.users[handle]):
            self.users[handle][field] += incrBy
        else:
            self.users[handle][field] = incrBy

    def append_user_field_with(self, handle, field, item):
        self.users[handle][field].append(item)

    def get_user_dict(self, handle):
        return self.users[handle]

if __name__ == '__main__':
    users = UsersDict()
    users.add_user('chris')
    users.incr_user_field_by('chris', 'num_tags', 1)
    