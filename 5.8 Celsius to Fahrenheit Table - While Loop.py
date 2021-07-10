#Design a program that displays a table of the Celsius temperatures 0 through 20, 
#and their Fahrenheit equivalents. 
#The formula for converting a temperature from Celsius to Fahrenheit is
#F = 9/5 C + 32
#where F is the Fahrenheit temperature and C is the Celsius temperature. 
#Your program must use a loop to display the table.

# Joel Christian

#This program displays a table of Celsius temperature 0 through 20
#and their Fahrenheit equivalents utilizing a While loop


def main():
    #Display the title and report header
    print("\nCelsius temprature and its Fahrenheit Equivalent")
    print("--------------------------------------------------")
    print("Celsius\t\tFahrenheit")
    print("--------------------------------------------------")

    #Initialize the Celsius variable
    c = 0

    #While loop that calculates and displays the Fahrenheit equivalent for its Celsius counterpart
    while (c <= 20):
        f = ((9/5) * c + 32)
        print(c,"\t\t", format(f,'.1f'))
        c = c + 1
        
#Calling the main module
main()
