# Upper limit for each occurrence ranking
O1 = 1 / 1000000
O2 = 1 / 100000
O3 = 1 / 10000
O4 = 1 / 1000
O5 = 1

# Dictionary to associate severity ranking for each harm
SeverityDictionary = {"embolism" : 5, "infection" : 4, "pain" : 3, "death" : 5, "bleeding" : 2, "allergic reaction" : 3, "cardiovascular collapse" : 5, "nerve injury" : 5, "hematoma" : 5}

# List of months
MonthList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# List of device harm
HarmList = ["embolism", "infection", "pain", "death", "bleeding", "allergic_reaction", "cardiovascular_collapse", "nerve_injury", "hematoma"]

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

# Create superclass Complaint with objects: month, sku, harm
class Complaint:
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

# Create subclass Device
class Device(Complaint):
    def __init__(self, month, sku, harm, device):
        super().__init__(month, sku, harm)
        self.device = device

    def getDevice(self):
        return self.device

    def setDevice(self, device):
        self.device = device

    # Method defined to identify device
    def IdentifyDevice(self, skuList, DeviceType):
        for num in skuList:
            if self.getSKU() == num:
                return self.setDevice(DeviceType)

# Function defined to split a given string into three substrings with variables month, sku, and harm
def makeComplaint(infoStr):
    month, sku, harm = infoStr.split(" ")
    return Complaint(month, sku, harm)

# Function defined to read and overwrite complaint data file
def OverwriteComplaint(file):
    ComplaintFile = open(file, 'r')
    complaint = ComplaintFile.read()
    complaint = complaint.replace("allergic reaction", "allergic_reaction")
    complaint = complaint.replace("cardiovascular collapse", "cardiovascular_collapse")
    complaint = complaint.replace("nerve injury", "nerve_injury")
    ComplaintFile.close()
    ComplaintFile = open('ComplaintData2022.txt', 'w')
    ComplaintFile.write(complaint)
    ComplaintFile.close()

# Create stack for a device (either Device A or Device B) for a given harm
def DeviceStack(file, skuList, DeviceType, HarmType):
    data = open(file, 'r')
    dataList = data.readlines()
    HarmDevice = []
    for line in dataList:
        x = makeComplaint(line)
        complaint = Device(x.getMonth(), x.getSKU(), x.getHarm(), "Device")
        complaint.IdentifyDevice(skuList, DeviceType)
        if complaint.getDevice() == DeviceType:
            HarmDevice.append([complaint.getMonth()])
            if complaint.getHarm().replace("\n", "") != HarmType:
                HarmDevice.pop()
    data.close()
    return HarmDevice

# Create stack for a given SKU for a given harm
def skuStack(file, skuNum, HarmType):
    data = open(file, 'r')
    dataList = data.readlines()
    HarmSKU = []
    for line in dataList:
        complaint = makeComplaint(line)
        if complaint.getSKU() == skuNum:
            HarmSKU.append(complaint.getMonth())
            if complaint.getHarm().replace("\n", "") != HarmType:
                HarmSKU.pop()
    data.close()
    return HarmSKU
    
# Function defined to count the total number of complaints for a given data list
def TotalCount(list):
    count = len(list)
    return count

# Function defined to count the total number of complaints for a given data list and given string
def StrCount(list, string):
    count = list.count([string])
    return count