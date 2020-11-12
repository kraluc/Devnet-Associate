user_database = [] # simulating a database

class User:
    def __init__(self, username, email):
        self.username = username # model determines object data
        self.email = email

    @staticmethod # do not require object instance
    def get_user(user_id):
        for user in user_database:
            if int(user.Id) == int(user_id):
                return user
        return False

    @staticmethod
    def get_users():
        return user_database

    def store_user(self): # storage dependent implementation
        user_id = len(user_database) + 1
        self.id = user_id
        user_database.append(self)
        return True

