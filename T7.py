#Take input for a student's name and marks in three subjects. Calculate the average 
#marks and print the result with a meaningful message.

name = input("enter student's name:")#name prompt

#marks prompt
M1 = float(input("Enter your marks in subject 1:"))
M2 = float(input("Enter your marks in subject 2: "))
M3 = float(input("Enter your marks in subject 3:"))

averagemarks =((M1+M2+M3)/3)#Average marks calculation
print ("Marks in subject 1:" , M1)
print ("Marks in subject 2:" , M2)#marks display
print ("Marks in subject 3:" , M3)
print("Average Marks:", f"{averagemarks:.2f}")# Display average to 2 decimal places

#conditions for showing meaningful message 

if averagemarks >= 85:
    print("Amazing job!")

elif averagemarks >= 70:
    print("Good job!")

else:
    print("Need to work more.")
