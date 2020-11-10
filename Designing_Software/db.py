from init import Initialization


class DB:
    def __init__(self):
        seld.dB = None

    def setupdB(self):
        print('Creating database...')
        self.dB = {}
        init = Initialization()
        self.DB = init.loadData(DB)
