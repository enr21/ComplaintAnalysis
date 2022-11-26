import ComplaintLib

AFile = open('SKUDeviceA.txt', 'r')
skuA = AFile.read().split(",")

BFile = open('SKUDeviceB.txt', 'r')
skuB = BFile.read().split(",")

ComplaintFile = open('ComplaintData.txt', 'r')

skuListA = []
skuListB = []

for i in skuA:
    skuListA.append(int(i))

for i in skuB:
    skuListB.append(int(i))

