#A car's miles-per-gallon (MPG) can be calculated using the formula, 
#MPG = Miles driven /  Gallons of gas used.  
#Design and construct a program that asks the user for the number of miles driven, 
#and the gallons of gas used.  
#It should calculate the car's miles-per-gallon, 
#and display the result on the screen.

#Joel Christian

#Get the number of miles driven
milesDriven = float(input('Enter the number of miles driven: '))

#Get the number of gallons of gas used
gasGallons = float(input('Enter the number of gallons of gas used:'))

#Calculate the Miles Per Gallon(MPG)
mpg = milesDriven/gasGallons

#Display the Miles per Gallon used
print('The Miles Per Gallon(MPG) is: ', mpg)
