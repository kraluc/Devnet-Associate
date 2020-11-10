import validator


initData = {
    'Users' : [
        { 'name' : 'Jon', 'title' : 'Manager' },
        { 'name' : 'Jamie', 'title' : 'SRE' }
    ]
}

class Initialization:
    def __init__(self):
        self.data = initData
        self.validator = validator.Validator()

    def loadData(self, DB):
        print(self.data)
        DB = self.data
        validate = self.validator.runTest(DB)
        if validate:
            return DB
        else:
            raise exception('Data not loaded')
