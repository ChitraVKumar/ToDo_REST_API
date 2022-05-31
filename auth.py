# creating a local db for users to not iterate multiple times we r using mapping.

users = [
    {
        'id': 1,
        'username': 'cvk',
        'password': 'asdf'
    }
]

#mapping every user inside a dict with a name

usernmae_mapping = { 'cvk': {
        'id': 1,
        'username': 'cvk',
        'password': 'asdf'
    }
}

#mapping the user with the id

userid_mapping = { 1: {
        'id': 1,
        'username': 'cvk',
        'password': 'asdf'
    }

}

def authenticate(username, password):
    user = usernmae_mapping.get(username, None)
    if user and user.password== password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)