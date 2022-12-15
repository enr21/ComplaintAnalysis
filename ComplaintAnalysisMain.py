import ComplaintLib

Divider = "------------------------------------------------------"
SoldUnits = 100000000

# Uses skuList function defined in the ComplaintLib library to create a list of skus from a given txt file
skuListA = ComplaintLib.skuList("SKUDeviceA.txt")
skuListB = ComplaintLib.skuList("SKUDeviceB.txt")

# Function defined obtaining user input to determine which analysis type to perform
def InputAnalysis():
    print("Which of the following analyses would you like to perform?")
    print("1. SKU Analysis")
    print("2. Device Analysis")
    analysis = (input("Enter number here: "))
    # If user does not enter "1" or "2", while loop will repeatedly execute prompting user to input one of the options listed
    # While loop will terminate once user inputs "1" or "2"
    while analysis != "1" and analysis != "2":
        print(Divider)
        analysis = (input("Please enter one of the options listed above: "))
    return analysis

# Function defined obtaining user input to determine which SKU to analyze
def InputSKU(skuListA, skuListB):
    sku = input("Please enter the SKU you wish to analyze: ")
    # If user does not enter a number indicated in either SKU list, while loop will repeatedly execute promoting user to input a valid SKU
    # While loop will terminate once user inputs a number listed in one of the two SKU lists
    skuListCombined = skuListA + skuListB
    x = False
    while x is False:
        for i in skuListCombined:
            if sku == str(i):
                return sku
        print(Divider)
        sku = input("Please enter a valid SKU number: ")

# Function defined obtaining user input to determine which device to analyze
def InputDevice():
    device = input("Please enter the device you wish to analyze: ")
    # If user does not enter "Device A" or "Device B", while loop will repeatedly execute promoting user to input a valid device name
    # While loop will terminate once user inputs "Device A" or "Device B"
    while device != "Device A" or device != "Device B":
        print(Divider)
        device = input("Please enter a valid device name: ")
    return device

# Function defined obtaining user input to determine which harm to analyze
def InputHarm():
    print("Which of the following harms would you like to analyze?")
    print("1. Embolism")
    print("2. Infection")
    print("3. Pain")
    print("4. Death")
    print("5. Bleeding")
    print("6. Allergic Reaction")
    print("7. Cardiovascular Collapse")
    print("8. Nerve Injury")
    print("9. Hematoma")
    print("10. All of the above")
    harm = input("Enter number here: ")
    # If user does not enter one of the listed options, while loop will repeatedly execute prompting user to input a valid option
    # While loop will terminate once user inputs one of the listed options
    x = False
    while x is False:
        for i in list(range(1, 11)):
            if harm == str(i):
                return harm
        print(Divider)
        harm = input("Please enter one of the options listed above: ")

# Function defined to create data stack for a given SKU and given harm
def CreateSKUStack(dataFile, skuType, harmType):
    AnalysisStack = ComplaintLib.skuStack(dataFile, skuType, harmType)
    return AnalysisStack

# Function defined to create data stack for a given device and given harm
def CreateDeviceStack(dataFile, skuListA, skuListB, deviceType, harmType):
    if deviceType == "Device A":
        skuList = skuListA
    elif deviceType == "Device B":
        skuList = skuListB
    AnalysisStack = ComplaintLib.DeviceStack(dataFile, skuList, deviceType, harmType)
    return AnalysisStack

# Function defined to print analysis results
def PrintAnalysis(harm, stack, units):
    print("Complaint Analysis for " + str(harm) + ":")
    total = 0
    for i in ComplaintLib.MonthList:
        count = stack.count(i)
        total += count
        occurrence = ComplaintLib.Occurrence(count, units)
        print(i + " - complaints received: " + str(count))
        print(i + " - occurrence ranking: " + occurrence)
    print("Total number of complaints received " + ": " + str(total))
    print(Divider)

def main():
    # Start of Complaint Analysis tool
    print("Welcome to the Medical Device Complaint Analysis tool!")
    print(Divider)
    
    # Prompts user to input filename to be analyzed
    # Using OverwriteComplaint function defined in the Complaint Lib library, data is cleaned for analysis
    dataFile = input("Please enter a filename to analyze: ")
    ComplaintLib.OverwriteComplaint(dataFile)
    print(Divider)
    
    # Prompts user to input desired analysis type using the defined InputAnalysis function
    # If user chooses SKU analysis, the program prompts the user to identify SKU number using the defined InputSKU function
    # If user chooses Device analysis, the program prompts the user to idenify device name using the defined InputDevice function
    AnalysisType = InputAnalysis()
    print(Divider)
    if AnalysisType == "1":
        skuType = InputSKU(skuListA, skuListB)
    elif AnalysisType == "2":
        deviceType = InputDevice()
    print(Divider)
    
    # Prompts user to input desired harm to analyze using the defined InputHarm function
    harmType = int(InputHarm())
    if harmType < 10:
        ComplaintHarm = ComplaintLib.HarmList[harmType - 1]
    print(Divider)

    # Program creates/analyzes data stacks based on user inputs 
    if harmType == 10:
        for i in ComplaintLib.HarmList:
            if AnalysisType == "1":
                AnalysisStack = CreateSKUStack(dataFile, skuType, i)
                PrintAnalysis(i, AnalysisStack, SoldUnits)
            elif AnalysisType == "2":
                AnalysisStack = CreateDeviceStack(dataFile, skuListA, skuListB, deviceType, i)
                PrintAnalysis(i, AnalysisStack, SoldUnits)
    else:
        if AnalysisType == "1":
            AnalysisStack = CreateSKUStack(dataFile, skuType, ComplaintHarm)
            PrintAnalysis(ComplaintHarm, AnalysisStack, SoldUnits)
        elif AnalysisType == "2":
            AnalysisStack = CreateDeviceStack(dataFile, skuListA, skuListB, deviceType, ComplaintHarm)
            PrintAnalysis(ComplaintHarm, AnalysisStack, SoldUnits)
 
if __name__ == '__main__':
    main()
