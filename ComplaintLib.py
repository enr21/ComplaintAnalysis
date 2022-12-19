'''
Emily Roman
16:137:552 Final Project
Medical Device Complaint Analysis Tool
Complaint Library
'''

from matplotlib import pyplot as plt

Divider = "----------------------------------------------------------"

# Upper limit for each occurrence ranking
O1 = 1 / 1000000
O2 = 1 / 100000
O3 = 1 / 10000
O4 = 1 / 1000
O5 = 1

# List of months
MonthList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# List of device harms
HarmList = ["embolism", "infection", "pain", "death", "bleeding", "allergic_reaction", "cardiovascular_collapse", "nerve_injury", "hematoma"]

# Function defined to open file and create list of data in file
def OpenFile(filename):
    file = open(filename, 'r')
    list = file.readlines()
    file.close()
    return list

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

# Create superclass Complaint with objects: month, sku, harm
class Complaint:
    def __init__(self, month, sku, harm):
        self.month = month
        self.sku = int(sku)
        self.harm = harm
    
    # Getter methods defined to return month, sku, and harm for a given instance of Complaint
    def getMonth(self):
        return self.month
    
    def getSKU(self):
        return self.sku
    
    def getHarm(self):
        return self.harm

# Function defined to overwrite complaint data list, cleaning data for analysis
def OverwriteComplaint(complaintList):
    newComplaint = []
    for i in complaintList:
        nRemoval = i.replace("\n", "")
        allergicReplace = nRemoval.replace("allergic reaction", "allergic_reaction")
        collapseReplace = allergicReplace.replace("cardiovascular collapse", "cardiovascular_collapse")
        nerveReplace = collapseReplace.replace("nerve injury", "nerve_injury")
        newComplaint.append(nerveReplace)
    return newComplaint

# Function defined to split a given string into three substrings with variables month, sku, and harm
def makeComplaint(infoStr):
    month, sku, harm = infoStr.split(" ")
    # Returns an instance of the Complaint class
    return Complaint(month, sku, harm)

# Create subclass Device with objects: month, sku, harm, device
class Device(Complaint):
    def __init__(self, month, sku, harm, device):
        # Initializes objects (month, sku, harm) from superclass Complaint
        super().__init__(month, sku, harm)
        self.device = device

    # Getter method defined to return device for a given instance of Device
    def getDevice(self):
        return self.device

    # Setter method defined to set device name for a given instance of Device
    def setDevice(self, device):
        self.device = device

    # Method defined to identify device type and set device name for a given instance of Device
    def IdentifyDevice(self, skuList, DeviceType):
        for num in skuList:
            if self.getSKU() == num:
                return self.setDevice(DeviceType)

# Create class skuInfo with objects: sku and UnitsSold
class skuInfo:
    def __init__(self, sku, UnitsSold):
        self.sku = sku
        self.UnitsSold = UnitsSold
    
    # Getter methods defined to return sku and UnitsSold for a given instance of skuInfo
    def getSKUfromList(self):
        return self.sku

    def getUnitsSold(self):
        return self.UnitsSold

# Function defined to split a given string into 13 substrings
# The first substring is defined as the SKU number
# The remaining 12 substrings define the number of units sold for each month
def makeSKUInfo(infoStr):
    sku, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = infoStr.split(" ")
    # Returns an instance of the skuInfo class
    return skuInfo(sku, [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec])

# Function defined to create a list of SKUs for a given device
def skuList(skuInfo):
    skuList = []
    for line in skuInfo:
        x = makeSKUInfo(line)
        skuList.append(int(x.getSKUfromList()))
    return skuList

# Function defined to identify the number of units sold for a given sku number
def IdentifyUnitsSKU(listA, listB, sku):
    UnitsSold = []
    for line in listA:
        x = makeSKUInfo(line)
        if int(x.getSKUfromList()) == sku:
            for i in x.getUnitsSold():
                UnitsSold.append(int(i.replace("\n", "")))
            return UnitsSold
    for line in listB:
        x = makeSKUInfo(line)    
        if int(x.getSKUfromList()) == sku:
            for i in x.getUnitsSold():
                UnitsSold.append(int(i.replace("\n", "")))
            return UnitsSold

# Function defined to identify the number of units sold for a device
def IdentifyUnitsDevice(skuList):
    TotalUnitsSold = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in skuList:
        x = makeSKUInfo(line)
        for i in x.getUnitsSold():
            UnitsSold = int(i.replace("\n", ""))
            TotalUnitsSold[x.getUnitsSold().index(i)] += UnitsSold
    return TotalUnitsSold

# Function defining stack for a given device and harm
def DeviceStack(complaintList, skuList, DeviceType, HarmType):
    HarmDevice = []
    for line in complaintList:
        x = makeComplaint(line)
        complaint = Device(x.getMonth(), x.getSKU(), x.getHarm(), "Device")
        complaint.IdentifyDevice(skuList, DeviceType)
        if complaint.getDevice() == DeviceType:
            HarmDevice.append(complaint.getMonth())
            if complaint.getHarm() != HarmType:
                HarmDevice.pop()
    return HarmDevice

# Function defined to create stack using DeviceStack function per user's choice inputs
def CreateDeviceStack(complaintList, skuListA, skuListB, deviceType, harmType):
    if deviceType == "Device A":
        skuList = skuListA
    elif deviceType == "Device B":
        skuList = skuListB
    AnalysisStack = DeviceStack(complaintList, skuList, deviceType, harmType)
    return AnalysisStack

# Function defining stack for a given SKU and harm
def skuStack(complaintList, skuNum, HarmType):
    HarmSKU = []
    for line in complaintList:
        complaint = makeComplaint(line)
        if complaint.getSKU() == skuNum:
            HarmSKU.append(complaint.getMonth())
            if complaint.getHarm() != HarmType:
                HarmSKU.pop()
    return HarmSKU

# Function defined to create stack using skuStack function per user's choice inputs
def CreateSKUStack(complaintList, skuType, harmType):
    AnalysisStack = skuStack(complaintList, skuType, harmType)
    return AnalysisStack

# Function defined to print analysis results and define y axes for # of complaints and occurrence rankings for a given harm
def AnalysisResults(harm, stack, units):
    total = 0
    y_ComplaintCount = []
    y_OccurrenceRanking = []
    for i in MonthList:
        # Counts the occurrence of each month in stack
        count = stack.count(i)
        # Count of each month appended to list y_ComplaintCount to create y axis data for plotting purposes
        y_ComplaintCount.append(count)
        # Occurrence ranking calculcated for each month using Occurrence function
        occurrence = Occurrence(count, units[MonthList.index(i)])
        # Occurrence ranking for each month appended to list y_OccurrenceRanking to create y axis data for plotting purposes
        y_OccurrenceRanking.append(occurrence)
        total += count
        # Prints count and occurrence for each month
        print(i + ": " + str(count) + " " + str(harm).replace("_", " ") + " complaints - occurrence ranking " + occurrence)
    # Print total count for given harm
    print("Total number of " + str(harm).replace("_", " ") + " complaints received" + ": " + str(total))
    print(Divider)
    # Returns y axis data for complaint count and occurrence ranking for plotting purposes
    return y_ComplaintCount, y_OccurrenceRanking

# Function defined to plot line chart of the analysis results using Matplotlib 
def PlotGraph(y_axisComplaint, y_axisOccurrence, title, y_label):
    # Plots line graph with months on x axis and # of complaints received on y axis
    plt.plot(MonthList, y_axisComplaint, 'bo-')
    # Plots text for each datapoint on line graph indicating the occurrence ranking
    for i in range(12):
        plt.text(MonthList[i], y_axisComplaint[i], y_axisOccurrence[i])
    plt.title(title)
    plt.xlabel("Month")
    plt.ylabel(y_label)
    filename = title
    # Saves then clears plot
    plt.savefig(filename + '.jpg')
    plt.clf()

# Function defined to create report of the analysis results
def CreateReport(AnalysisObject, ComplaintCount, OccurrenceRanking, harm, date, filename):
    # Appends analysis results to report 'ComplaintAnalysisReport.txt'
    # If report does not currently exist, file created with filename 'ComplaintAnalysisReport.txt'
    f = open("ComplaintAnalaysisReport.txt", "a+")
    f.write("File analyzed: " + filename + "\n")
    f.write("Analysis performed on: " + date + "\n")
    f.write("\n")
    f.write("Complaint Analysis for " + AnalysisObject + "\n")
    total = 0
    for i in MonthList:
        count = ComplaintCount[MonthList.index(i)]
        total += count
        occurrence = OccurrenceRanking[MonthList.index(i)]
        f.write(i + ": " + str(count) + " " + str(harm).replace("_", " ") + " complaints - occurrence ranking " + occurrence + "\n")
    f.write("Total number of " + str(harm).replace("_", " ") + " complaints received" + ": " + str(total) + "\n")
    f.write(Divider + "\n")

# Function defined to initiate analysis result outputs
# Outputs include: printed results in terminal, created/displayed plots, created/displayed report
def ResultOutput(AnalysisObject, harm, stack, units, date, filename):
    print("Complaint Analysis for", AnalysisObject)
    y_ComplaintCount, y_OccurrenceRanking = AnalysisResults(harm, stack, units)
    # Plot created for - Complaint Count vs Month
    PlotGraph(y_ComplaintCount, y_OccurrenceRanking, (AnalysisObject + " - analysis of " + str(harm).replace("_", " ") + " complaints"), "# of Complaints")
    CreateReport(AnalysisObject, y_ComplaintCount, y_OccurrenceRanking, harm, date, filename)
