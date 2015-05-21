class Swc:
    filename = ""

    def __init__(self, filename):
        self.filename = filename
        self.data = ""
        print filename
        self.loadswc()

    def loadswc(self, filename):
        self.filename = filename
        self.loadswc()

    def loadswc(self):
        f = open(self.filename, "r")
        for line in f.readlines():
            
        #self.data = f.read()
        f.close()

    def printfile(self):
        print self.data

