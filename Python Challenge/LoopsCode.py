# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:41:08 2020

@author: david
"""
#Using a while loop, ask the user "How many numbers?", 
#then print out a chain of ascending numbers, starting at 0.


#After the results have printed ask the user if they would 
#like to continue.


#If "y", restart the process, starting at 0 again.


#If "n", exit the chain.


#NOTE: Rather than just displaying numbers constantly 
#starting at 0, have the numbers begin at the end of the 
#previous chain.


#a variable to determine whether the loop keeps running
playing = "y"
#a variable to track the number for the loops
lastnumber=0

#a while loop for start the game; userchoice is the number entered by the users

while playing=="y":
    
    userchoice=(int(input( "How many numbers? ")))
    
    userchoice+=lastnumber
#establish a for loop to collect and print the results  
    for i in range (lastnumber, userchoice):
        print(i)
        lastnumber=lastnumber+1
        
    playing = input("Do you want to keep playing? (y) or (n)?" )

    if playing == 'n':
        print(f"Thank you for playing!")
        break
    elif playing == 'y':
        continue 
    else:
        playing = input("You have to choose y to continue or n to end." )

