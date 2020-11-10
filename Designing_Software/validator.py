class Validator:
    def run Test(self, DB):
        print('Checking if app is ready...')
        if 'Users' in DB.keys():
            return True
        else:
            return False