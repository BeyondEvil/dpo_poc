class User(object):

    def __init__(self, user_name, email):
        self._user_name = user_name
        self._email = email

    @property
    def identifier(self):
        return self._user_name

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return "password"

    SIGNATURE = {'name': str, 'email': str}

    @classmethod
    def create(cls, name, email):
        return cls(name, email)
