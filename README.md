# Complaint Analysis Tool Background
The Medical Device Complaint Analysis Tool analyzes customer complaint data to determine the occurrence ranking of a harm per the risk management medical device standard ISO 14971:2019 (Table 1).

Table 1: Probability of Occurrence Rankings
![image](https://github.com/enr21/ComplaintAnalysis/assets/119016017/be869c97-7417-461a-a9cf-f4bd269f9583)

This tool was created for a medical device company which manufactures two devices (Device A and Device B) with 9 known harms applicable to each device. The 9 known harms are: bleeding, pain, allergic reaction, injection, hematoma, nervus injury, embolism, cardiovascular collapse, and death.

# Data
There are three data files provided. One file containing complaint data for Device A and Device B. Two files containing device data, one file for each device.

## Complaint Data File
Filename: ComplaintData2022

The ComplaintData2022 file contains a list of 10,000+ complaints for the year 2022. The data file includes the following information for each complaint: month of occurrence (column 1), SKU (column 2), harm (column 3).

## Device Info Data Files
Filename for Device A: skuListA
Filename for Device B: skuListB

Each data file contains a list of SKUs representing the device in column 1. For each SKU, the file identifies the number of units sold for each month of 2022 in columns 2 to 13.
