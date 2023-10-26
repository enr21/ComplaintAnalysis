'''
Emily Roman
16:137:552 Final Project
Medical Device Complaint Analysis Tool
Complaint Analysis Main Program
'''

import ComplaintLib
from datetime import datetime

Divider = "----------------------------------------------------------"

# Prints a welcome message when initiating program
print("Welcome to the Medical Device Complaint Analysis tool!")
print(Divider)

# Open sku files and create list with sku information (sku numbers and units sold each month)
ListDevAinfo = ComplaintLib.OpenFile("skuListA.txt")
ListDevBinfo = ComplaintLib.OpenFile("skuListB.txt")

# Uses skuList function defined in the ComplaintLib library to create a list of skus from a given txt file
skuListA = ComplaintLib.skuList(ListDevAinfo)
skuListB = ComplaintLib.skuList(ListDevBinfo)

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
    while device != "Device A" and device != "Device B":
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
    
def main():
    # Start of Complaint Analysis tool
    # Prompts user to input filename to be analyzed
    while True:
        try:
            ComplaintFile = input("Please enter a filename to analyze: ")
            ComplaintInfo = ComplaintLib.OpenFile(ComplaintFile)
            break
        # Error handling implemented; if filename provided by user is not found, user will be re-prompted to enter a filename
        except FileNotFoundError:
            print("File not found. Please try again.")
            print(Divider)
    print(Divider)
    
    # Using OverwriteComplaint function defined in the ComplaintLib library, data is cleaned for analysis
    ComplaintList = ComplaintLib.OverwriteComplaint(ComplaintInfo)
    
    # Prompts user to input desired analysis type using the defined InputAnalysis function
    AnalysisType = InputAnalysis()
    print(Divider)
    # If user chooses SKU analysis ("1"), the program prompts the user to identify SKU number using the defined InputSKU function
    if AnalysisType == "1":
        skuType = int(InputSKU(skuListA, skuListB))
        UnitsSold = ComplaintLib.IdentifyUnitsSKU(ListDevAinfo, ListDevBinfo, skuType)
        AnalysisObject = "SKU " + str(skuType)
    # If user chooses Device analysis ("2"), the program prompts the user to idenify device name using the defined InputDevice function
    elif AnalysisType == "2":
        deviceType = InputDevice()
        AnalysisObject = deviceType
        if deviceType == "Device A":
            UnitsSold = ComplaintLib.IdentifyUnitsDevice(ListDevAinfo)
        elif deviceType == "Device B":
            UnitsSold = ComplaintLib.IdentifyUnitsDevice(ListDevBinfo)
    print(Divider)

    # Prompts user to input harm to analyze using the defined InputHarm function
    harmType = int(InputHarm())
    if harmType < 10:
        ComplaintHarm = ComplaintLib.HarmList[harmType - 1]
    print(Divider)

    # Program creates/analyzes data stacks based on user analysis and harm inputs
    # If the user chose to analyze all harms, program iterates through each harm - creating/analyzing data stacks for each harm
    date = str(datetime.now())
    if harmType == 10:
        for i in ComplaintLib.HarmList:
            if AnalysisType == "1":
                AnalysisStack = ComplaintLib.CreateSKUStack(ComplaintList, skuType, i)
            elif AnalysisType == "2":
                AnalysisStack = ComplaintLib.CreateDeviceStack(ComplaintList, skuListA, skuListB, deviceType, i)
            # Program prints, creates report, and creates plots of the analysis results
            ComplaintLib.ResultOutput(AnalysisObject, i, AnalysisStack, UnitsSold, date, ComplaintFile)
    # If the user chose to analyze one harm, data stack is created for that harm and analyzed
    else:
        if AnalysisType == "1":
            AnalysisStack = ComplaintLib.CreateSKUStack(ComplaintList, skuType, ComplaintHarm)
        elif AnalysisType == "2":
            AnalysisStack = ComplaintLib.CreateDeviceStack(ComplaintList, skuListA, skuListB, deviceType, ComplaintHarm)
        # Program prints, creates report, and creates plots of the analysis results
        ComplaintLib.ResultOutput(AnalysisObject, ComplaintHarm, AnalysisStack, UnitsSold, date, ComplaintFile)

    # Prompt user to rerun or quit program
    print("Thank you for using the Medical Device Complaint Analysis Tool!")
    print("Enter 1 to perform another analysis")
    print("Enter any other character to quit program")
    RerunInput = input("")
    if RerunInput == "1":
        print(Divider)
        main()
    
if __name__ == '__main__':
    main()
