import sqlite3

class User: # creating user objects instead of dicts to store user info
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username): # fins the username in the database using the username
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            # user = User(row[0], row[2], row[3])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
    @classmethod
    def find_by_id(cls, _id): # fins the username in the database using the username
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            # user = User(row[0], row[2], row[3])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
