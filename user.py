class User: # creating user objects instead of dicts to store user info
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

