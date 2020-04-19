# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:06:30 2020

@author: david
"""




#Step 1 import file
import os
import csv

# Set path for file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv,'r', encoding='utf-8') as f:        
    
    csv_reader= csv.reader(f)
    next(csv_reader)
    month = 0
    total_months=0
    profit_loss=0
    av_change=0
    date_col=None
    previous_row=int(next(csv_reader)[1])
    net_chang_list=[]
    greatest_sd_decrease=["", 0.0]
    greatest_sd_increase=["", 99]
    
    for row in csv_reader:
        net_change=int(row[1])-previous_row
        net_chang_list=net_chang_list+[net_change]
        net_change_month=row[0]
        total_months += 1
        profit_loss += 1
        
        if net_change<greatest_sd_decrease[1]:
            greatest_sd_decrease[1] = net_change
            greatest_sd_decrease[0] = net_change-month
        elif net_change > greatest_sd_increase[1]:
            greatest_sd_increase[1] = net_change
            greatest_sd_increase[0] = net_change_month
        
net_average = sum(net_chang_list) / len(net_chang_list)

financi
print("Financial Analysis")
print("______________________")
print(f'Total Months: {total_months}')
print(f'Total: {profit_loss}')
print(f'Average Change: {net_average}')
print(f'Greatest Increase in Profits: {greatest_sd_increase[0]}, ${greatest_sd_increase[1]}')
print(f'Greatest Decrease in Profits: {greatest_sd_decrease[0]}, ${greatest_sd_decrease[1]}')

#         # 
# 
# 
# =============================================================================
