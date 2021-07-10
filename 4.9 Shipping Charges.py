#The Fast Freight Shipping Company charges the following rates:
#Weight of Package                          Rate per Pound
#2 pounds or less                               $1.10
#Over 2 pounds but not more than 6 pounds       $2.20
#Over 6 pounds but not more than 10 pounds      $3.70
#Over 10 pounds                                 $3.80
#Design a program that asks the user to enter the weight of a package, 
#and then displays the shipping charges.

#Joel Christian

#This program accepts the weight of the package,
#determines the rate per pound,
#calculates and siplays the total rate of shipping

#Create and initialize a global variable to store the shipping rate
rate = 0.0

def main():
    #Get the weight of the package
    weight = float(input("Enter the weight of the package: "))

    #Determine the rate per pound
    getRate(weight)

    #Calculate and display the total shipping cost
    getTotal(weight)

#The getRate module determines the rate of shipping
#based on the weight of the package
def getRate(weight):
    global rate
    if weight <= 2.0:
        rate = 1.10
    else:
        if weight <=6.0:
            rate = 2.20
        else:
            if weight <= 10.0:
                rate = 3.70
            else:
                rate = 3.80

#The getTotal module calculates,
#and displays the total shipping charge
def getTotal(weight):
    global rate
    #Calculate the total shipping cost
    totalAmt = weight * rate

    #Display the shipping rate 
    print("\nYour shipping rate per pound is: $", format(rate, '.2f'))

    #Display the total shipping charge
    print("\nYour total shipping charge is: $", format(totalAmt, '.2f'))

#Call the main function
main()
    
