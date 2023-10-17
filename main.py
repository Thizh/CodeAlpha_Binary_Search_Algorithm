'''
Project Name: Binary Search Algorithm

Author: Thisitha Wickramarachchi

Description: This program will take any input starting from 0 to any range 
that you specify and display a range of numbers with a difference of two..
'''

#take inputs from user
startPoint = int(input("Add a starting number: "))
endPoint = int(input("Add a ending number: "))

#display a range of numbers with a difference of two
for i in range(startPoint, endPoint, 2) :
    print(i)