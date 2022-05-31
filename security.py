from werkzeug.security import safe_str_cmp
from user import User


users = [
    User(1, 'cvk', 'asdf')
]

#mapping every user inside a dict with a name and id

usernmae_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = usernmae_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password): # compares string safely
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)