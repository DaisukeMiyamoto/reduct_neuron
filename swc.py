class Swc:
    filename = ""
    data = []
    header = ""
    branch_list = []

    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.header = ""
        self.branch_list = []
        self.loadswc()

    def loadswc(self, filename):
        self.filename = filename
        self.loadswc()

    def loadswc(self):
        f = open(self.filename, "r")
        i = 0
        for line in f:
            if line[0]=="#" :
                self.header += line
            else :
                record = line.split(" ")
                if len(record)==7:
                    self.data.append([int(record[0]), int(record[1]), float(record[2]), float(record[3]), float(record[4]), 
                                      float(record[5]), int(record[6])])
                    i+=1                
        f.close()
        self.make_branch_list()

    def make_branch_list(self):
        self.branch_list.append([0, 0])

        for record in self.data :
            self.branch_list.append([record[0]])
            self.branch_list[record[0]].append(record[6])

        for record in self.branch_list :
            if record[1] != -1 :
                self.branch_list[record[1]].append(record[0])
#        self.show_branch_list()

    def show_branch_list(self):
        for record in self.branch_list :
            if len(record) != 0 :
                print record


    def show_data(self):
        for record in self.data :
            print record

    def show_header(self):
        print self.header


    def show_hist(self):
        hist = [0] * 20

        for record in self.branch_list :
            if(len(record)>=2 and record[0]!=0) :
                hist[len(record)-2]+=1

        for i in range(len(hist)) :
            print "%d : %d" % (i,  hist[i])



