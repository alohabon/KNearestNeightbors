import csv
from operator import itemgetter
import math

class knn(object):

    def __init__(self, x1, x2, x3, x4, x5, y):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.y = y

#metode yang digunakan adalah metode Euclidean
def hitungEuc(x1, x2, x3, x4,x5,y1,y2,y3,y4,y5 ):
    #rumus metode euclidean
    euc = math.sqrt( ((x1-y1)**2) + ((x2-y2)**2) + ((x3-y3)**2) + ((x4-y4)**2) + ((x5-y5)**2) )
    return euc

DataTrain = [] 
DataTest = [] 

#men-scan data csv
with open('DataTrain_Tugas3_AI.csv') as data:
    readerTrain = csv.DictReader(data)
    for row in readerTrain:
        DataTrain.append(knn(float(row['X1']), float(row['X2']), float(row['X3']), float(row['X4']), float(row['X5']), float(row['Y'])))

with open('DataTest_Tugas3_AI.csv') as data:
    readerTest = csv.DictReader(data)
    for row in readerTest:
        DataTest.append(knn(float(row['X1']), float(row['X2']), float(row['X3']), float(row['X4']), float(row['X5']), None))

#menentukan nilai k (nilai tetangga terdekat)
k = 3

for datest in DataTest:
    Neigh = []
    for datrain in DataTrain:

        #menghitung jarak dengan metode euclidean
        euc1 = hitungEuc(datest.x1 ,datrain.x1 ,datest.x2 ,datrain.x2 ,datest.x3 ,datrain.x3 ,datest.x4 ,datrain.x4 ,datest.x5 ,datrain.x5)
        klas = datrain.y

        #menyortir hasil jarak dari yang terkecil 
        Neigh.sort(key=itemgetter(0))
        count0 = 0
        count1 = 0
        count2 = 0
        count3 = 0

        #mengelompokkan hasil jarak sebelumnya
        Neigh.append([euc1, klas])

    #menghitung jumlah masing" kelas knnya
    for i in range(k):
        if (Neigh[i][1] == 0):
            count0 += 1
        elif (Neigh[i][1] == 1):
            count1 += 1
        elif (Neigh[i][1] == 2):
            count2 += 1
        elif (Neigh[i][1] == 3):
            count3 += 1

    #menentukan kelas untuk data testnya
    if max(count0,count1,count2,count3)==count0:
        datest.y = 0
    elif max(count0,count1,count2,count3)==count1:
        datest.y = 1
    elif max(count0,count1,count2,count3)==count2:
        datest.y = 2
    elif max(count0,count1,count2,count3)==count3:
        datest.y = 3

#untuk menuliskan kembali hasilnya pada csv baru(datest.y)
with open('TebakanTugas3.csv','w', newline='') as csvfile:
    fieldnames = ['hasil']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(DataTest)):
        writer.writerow({'hasil': DataTest[i].y})
