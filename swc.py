import copy

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
        branch_list = []
        self.branch_list.append([0,0])

        for record in self.data :
            self.branch_list.append([record[0]])
            self.branch_list[record[0]].append(record[6])

        for record in self.branch_list :
            if record[1] >0 :
                self.branch_list[record[1]].append(record[0])

    def write(self, filename):
        f = open(filename, "w")
        f.write(self.header)
        for record in self.data :
            line = str(record[0]) +" "+ str(record[1]) +" "+ str(record[2]) +" "+ str(record[3]) +" "+ str(record[4]) +" "+ str(record[5]) +" "+ str(record[6]) +"\n"
            f.write(line)
            

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


    def branch_list_to_data(self):
        data = copy.deepcopy(self.data)
        reduce_map = []
        i = 1

        for record in self.branch_list :
            if record[0] == 0 :
                reduce_map.append(0)
            else:
                reduce_map.append(i)
                i+=1
        
        for i in range(len(self.data)):
            data[i][0] = reduce_map[data[i][0]]
            if data[i][6] > 0:
                data[i][6] = reduce_map[self.branch_list[i+1][1]]


        self.data = []
        for record in data:
            if(record[0]!=0):
                self.data.append(record)




    def reduct1(self):
        for record in self.branch_list :
            #self.show_branch_list()
            #print "-----------------------------------------"
            if len(record) == 3 and record[1]>0:
                target = record[0]
                record[0] = 0
                for record2 in self.branch_list :
                    if target == record2[1] :
                        record2[1] = record[1]
                        while self.branch_list[record2[1]][0] == 0 :
                            record2[1] = self.branch_list[record2[1]][1]
        
        self.branch_list_to_data()

    def reduct2(self):

        
