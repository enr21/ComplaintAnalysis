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

# Calculate total count for each harm
def HarmCount(complaint, harm):
    Count = complaint.count(harm)
    return Count

# Calculate the probability of occurrence to determine occurrence ranking
def Occurrence(HarmCount, units):
    probability = (HarmCount / units)
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