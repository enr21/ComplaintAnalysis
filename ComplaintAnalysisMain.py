import ComplaintLib

def main():
    skuListA = ComplaintLib.skuList("SKUDeviceA.txt")
    skuListB = ComplaintLib.skuList("SKUDeviceB.txt")
    dataFile = input("Enter a filename to analyze: ")
    ComplaintLib.OverwriteComplaint(dataFile)
    HarmsDevA = ComplaintLib.IdentifySKU(skuListA, dataFile)
    HarmsDevB = ComplaintLib.IdentifySKU(skuListB, dataFile)
    print(HarmsDevA)
    print(HarmsDevB)

main()