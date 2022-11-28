# Upper limit for each occurrence ranking
O1 = 1 / 1000000
O2 = 1 / 100000
O3 = 1 / 10000
O4 = 1 / 1000
O5 = 1

# Dictionaries to associate the total complaints received to its corresponding harm
AComplaintDict = {"embolism" : 0, "infection" : 0, "pain" : 0, "death" : 0, "bleeding" : 0, "allergic reaction" : 0, "cardiovascular collapse" : 0, "nerve injury" : 0, "hematoma" : 0}
BComplaintDict = {"embolism" : 0, "infection" : 0, "pain" : 0, "death" : 0, "bleeding" : 0, "allergic reaction" : 0, "cardiovascular collapse" : 0, "nerve injury" : 0, "hematoma" : 0}

# List of device harms
HarmList = ["embolism", "infection", "pain", "death", "bleeding", "allergic reaction", "cardiovascular collapse", "nerve injury", "hematoma"]

# Function defined to calculate total count for each harm
def HarmCount(complaint, harm):
    Count = complaint.count(harm)
    return Count

# Function defined to calculate the probability of occurrence to determine occurrence ranking
def Occurrence(count, units):
    probability = (count / units)
    if probability <= O1:
        OccRank = "O1"
    elif probability > O1 and probability <= O2:
        OccRank = "O2"
    elif probability > O2 and probability <= O3:
        OccRank = "O3"
    elif probability > O3 and probability <= O4:
        OccRank = "O4"
    else:
        OccRank = "O5"
    return OccRank

# Function defined to create a list of SKUs for a given device
def skuList(filename):
    File = open(filename, 'r')
    List = File.read().split(",")
    File.close()
    skuList = []
    for i in List:
        skuList.append(int(i))
    return skuList

# Create class Complaint with objects: month, sku, harm
class Complaint():

    def __init__(self, month, sku, harm):
        self.month = month
        self.sku = int(sku)
        self.harm = harm
    
    def getMonth(self):
        return self.month
    
    def getSKU(self):
        return self.sku
    
    def getHarm(self):
        return self.harm

# Function defined to split a given string into three substrings with variables month, sku, and harm
def makeComplaint(infoStr):
    month, sku, harm = infoStr.split(" ")
    return Complaint(month, sku, harm)

# Function defined to read and overwrite complaint data file
def OverwriteComplaint(file):
    ComplaintFile = open(file, 'r')
    complaint = (ComplaintFile.read())
    complaint = complaint.replace("allergic reaction", "allergic_reaction")
    complaint = complaint.replace("cardiovascular collapse", "cardiovascular_collapse")
    complaint = complaint.replace("nerve injury", "nerve_injury")
    ComplaintFile.close()
    ComplaintFile = open('ComplaintData2022.txt', 'w')
    ComplaintFile.write(complaint)
    ComplaintFile.close()

# Function defined to identify which device a given SKU belongs to
def IdentifySKU(skuList, file):
    Harm = []
    Month = []
    ComplaintFile = open(file, 'r')
    x = makeComplaint(ComplaintFile.readline())
    for line in ComplaintFile:
        x = makeComplaint(line)
        identifySKU = x.getSKU()
        for i in skuList:
            if identifySKU == i:
                Harm.append(x.getHarm().replace("\n", ""))
                Month.append(x.getMonth())
    return Harm #need to also return month, revisit