'''
Project Name: Binary Search Algorithm

Author: Thisitha Wickramarachchi

Description: This program will take any input starting from 0 to any range 
that you specify and display a range of numbers with a difference of two.
'''

#take inputs from user
while True :
    startPoint = int(input("Add a starting number: "))
    if startPoint >= 0 :
        break
    else :
        print("Enter a number bigger than 0")
        continue

while True:    
    endPoint = int(input("Add a ending number: "))
    if endPoint >= 0 :
        break
    else :
        print("Enter a number bigger than 0")
        continue

#display a range of numbers with a difference of two
for i in range(startPoint, endPoint, 2) :
    print(i)
