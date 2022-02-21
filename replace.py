class Replace:
    def __init__(self, file, search, replace):
        self.file = file
        self.search = search
        self.replace = replace
    '''REPLACE SINGLE STRING '''
    def repsingle(self):
        FILE = self.file.replace(self.search, self.replace)
        return FILE

    #REPLACE STRINGS FROM A LIST
    def rep(self):
        count = len(self.search)
        X = 0   
        #change character
        FILE = self.file
        while X < count:
            try:
                FILE = FILE.replace(self.search[X], self.replace[X])
            except IndexError:
                FILE = FILE.replace(self.search[X], '')
            X += 1 
        return FILE
        
