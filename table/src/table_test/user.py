from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'uid'])


class UserStore:
    def __init__(self):
        self._users = set()

    def add(self, user):
        self._users.add(user)

    def remove(self, user):
        self._users.remove(user)

    def users(self):
        return iter(self._users)

    def __len__(self):
        return len(self._users)
