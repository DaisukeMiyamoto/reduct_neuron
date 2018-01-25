import copy
from math import sqrt

'''
from neuromorpho.org

The three dimensional structure of a neuron can be represented in a SWC format (Cannon et al., 1998). SWC is a simple Standardized format. Each line has 7 fields encoding data for a single neuronal compartment:
an integer number as compartment identifier
type of neuronal compartment 
   0 - undefined
   1 - soma
   2 - axon
   3 - basal dendrite
   4 - apical dendrite
x coordinate of the compartment
y coordinate of the compartment
z coordinate of the compartment
radius of the compartment
parent compartment
'''


class Swc:
    pi = 3.1415926535
    show_debufinfo=0
    filename = ""
    data = []
    branch_list = []
    header = ""
    base_header = \
'''\
#ORIGINAL_SOURCE neb_SWC_Tools
#SOMA_AREA 
#SHINKAGE_CORRECTION 1.000000 1.000000 1.000000
#VERSION_NUMBER 0.1
#VERSION_DATE 2015-06-20
#SCALE 1.0 1.0 1.0
'''
    def __init__(self, **kwds):
        if('filename' in kwds):
            self.filename = kwds['filename']
            self.data = []
            self.header = ""
            self.branch_list = []
            self.loadswc()
        else:
            self.filename = ""
            self.data = []
            self.header = ""
            self.branch_list = []
        if('set_fingerprint' in kwds):
            if(kwds['set_fingerprint']==1):
                self.set_fingerprint()
        if('show_debuginfo' in kwds):
            if(kwds['show_debuginfo']==1):
                self.show_debuginfo=1
        else:
            self.show_debuginfo=0



    def genswc(self, ncmp):

        self.data = []
        self.header = self.base_header
        self.data.append([1, 0, 10.0, 10.0, 10.0, 1.0, -1])
        i=1
        while(i<ncmp):
            i += 1
            self.data.append([i, 0, 10.0, 9.9+i*0.1, 10.0, 1.0, i-1])

        self.data_to_branch_list()

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
        self.data_to_branch_list()

    def data_to_branch_list(self):
        self.branch_list = []
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
        self.filename = filename

    def show_branch_list(self):
        for record in self.branch_list :
            if len(record) != 0 :
                print(record)

    def show_filename(self):
        print(self.filename)

    def show_data(self):
        for record in self.data :
            print(record)

    def show_header(self):
        print(self.header)

    def show_hist(self):
        hist = [0] * 20

        for record in self.branch_list :
            if(len(record)>=2 and record[0]!=0) :
                hist[len(record)-2]+=1

        for i in range(len(hist)) :
            print("%d : %d" % (i, hist[i]))

    def size_of_data(self):
        return len(self.data)

    def branch_list_to_data(self):
        data = copy.deepcopy(self.data)
        reduce_map = []
        i = 1

        for record in self.branch_list:
            if record[0] == 0 :
                reduce_map.append(0)
            else:
                reduce_map.append(i)
                i+=1

        if self.show_debuginfo==1:
            print("branch_list")
            print(self.branch_list)

            print("reduce_map")
            print(reduce_map)

        for i in range(len(self.data)):
            data[i][0] = reduce_map[data[i][0]]
            if data[i][6] > 0:
                data[i][6] = reduce_map[self.branch_list[i+1][1]]


        self.data = []
        for record in data:
            if(record[0]!=0):
                self.data.append(record)

        self.data_to_branch_list()

    def get_filename(self):
        return self.filename

    def get_total_length(self):
        length = 0
        for record in self.data:
            if(record[6]!=-1):
                #print "sqrt( (%f-%f)**2 + (%f-%f)**2 + (%f-%f**2) )" % (record[2], self.data[record[6]-1][2], record[3], self.data[record[6]-1][3], record[4], self.data[record[6]-1][4])
                length += sqrt( \
                                (record[2] - self.data[record[6]-1][2])**2 \
                                + (record[3] - self.data[record[6]-1][3])**2 \
                                + (record[4] - self.data[record[6]-1][4])**2 \
                        )
        return length

    def get_total_volume(self):
        vol = 0
        for record in self.data:
            if(record[6]!=-1):
                vol += sqrt( \
                                (record[2] - self.data[record[6]-1][2])**2 \
                                + (record[3] - self.data[record[6]-1][3])**2 \
                                + (record[4] - self.data[record[6]-1][4])**2 \
                        ) * ((record[5] + self.data[record[6]-1][5])/2)**2 * self.pi
        return vol

    def get_n_cmp(self):
        return(self.size_of_data())

    def reduct1(self):
        # remove terminal node
        if self.show_debuginfo==1:
            print("branch_list")
            print(self.branch_list)

        vollist = []
        for i in range(len(self.branch_list)) :
            vollist.append([i, self.data[i-1][5]])

        vollist.sort(key=lambda x:x[1])
        for i in range(len(vollist)) :
            if len(self.branch_list[vollist[i][0]]) == 2 :
                self.branch_list[vollist[i][0]][0] = 0

        self.branch_list_to_data()


    def reduct2(self):
        # remove non branching node

        for record in self.branch_list:
            #self.show_branch_list()
            #print "-----------------------------------------"
            if len(record) == 3 and record[1]>0:
                target = record[0]
                record[0] = 0
                for record2 in self.branch_list :
                    if target == record2[1] :
                        record2[1] = record[1]
                        while self.branch_list[record2[1]][0] == 0:
                            record2[1] = self.branch_list[record2[1]][1]

        self.branch_list_to_data()


    def set_fingerprint(self):
        for record in self.data:
            record[1] = record[0]

