import db


class App:
    def __init__(self):
        self.running = False
        self.database = db.DB()

    def startProgram(self):
        print('Starting the app...')
        self.database.setupDB()
        self.running = True
