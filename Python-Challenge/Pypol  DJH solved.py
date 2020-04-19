# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:46:03 2020

@author: david
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:19:06 2020

@author: david
"""
#


#Step 1 import file
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# =============================================================================
# 
# #Step 2
    TotalVotes=0
    KahnVotes=0
    LiVotes=0
    CorreyVotes=0
    OTooleyVotes= 0
        
# #set up variables
    for row in csvreader:
        
        
        
#Step 3 Identify columns 
        # 
        Vote = row[0]
        Candidate = row[2]
        # 
# #Step 4 Establish vote counting
# 

        if row[2] == "Khan":
            KahnVotes = KahnVotes+1
        elif row[2] == "Li":
            LiVotes=LiVotes+1
        elif row[2] == "Correy":
            CorreyVotes=CorreyVotes+1
        elif row[2]=="O'""Tooley":
            OTooleyVotes=OTooleyVotes+1
# 
#totalvotes 
TotalVotes=KahnVotes+LiVotes+CorreyVotes+OTooleyVotes

      
#     
#     
# #calculate percentages
#     
KahnPercent=round(KahnVotes/TotalVotes * 100, 3)
CorreyPercent=round(CorreyVotes/TotalVotes * 100, 3)
LiPercent=round(LiVotes/TotalVotes * 100, 3)
OTooleyPercent=round(OTooleyVotes/TotalVotes * 100, 3)
#rounded_value = round(rounded_value + randn, 3)

#print
print(f"Election Results")
print(f"----------------------------")
print(f"Kahn: {KahnPercent}%, {KahnVotes}")
print(f"Correy: {CorreyPercent}%, {CorreyVotes}")
print(f"Li: {LiPercent}%, {LiVotes}")
print(f"OTooley: {OTooleyPercent}%, {OTooleyVotes}")
print("----------------------------")

#determine and print winner
if KahnVotes>CorreyVotes and KahnVotes>LiVotes and KahnVotes>OTooleyVotes:
    print(f"Winner: Kahn")
elif CorreyVotes>LiVotes and CorreyVotes>OTooleyVotes:
    print(f"Winner: Correy")
elif LiVotes>OTooleyVotes:
    print(f"Winner: Li")
else: 
    print(f"Winner: OTooley")

