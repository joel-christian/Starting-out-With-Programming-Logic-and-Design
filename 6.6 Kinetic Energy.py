#In physics, an object that is in motion is said to have kinetic energy. 
#The following formula can be used to determine a moving object’s kinetic energy:
#KE = 1/2 * m * v^2
#The variables in the formula are as follows: 
#KE is the kinetic energy, 
#m is the object’s mass in kilograms, 
#and v is the object’s velocity, in meters per second.
#Design a function named kineticEnergy that accepts an object’s mass (in kilograms) 
#and, velocity (in meters per second) as arguments. 
#The function should return the amount of kinetic energy that the object has. 
#Design a program that asks the user to enter values for mass and velocity, 
#and then calls the kineticEnergy function to get the object’s kinetic energy.

#I have added an Input Validation requirement for both the inputs.
#Feel free to skip that part if you are not required to do that.

#Joel Christian

#This program accepts mass and velocity of the object from the user,
#validates that both of those values are greater than 0,
#and, displays the kinetic energy of the object in joules.

def main():

    ke = kineticEnergy()

    #Display the result
    print("\nThe kinetic energy of the object is: ", format(ke, '.2f'), "joules.")

#The kineticEnergy module prompts the user to enter the mass and velocity of the object,
#validates that the input is greater than 0,
#calculates the kinetic energy,
#and sends it back to the main function.

def kineticEnergy():

    #Prompt the user to input the mass of the object
    m = float(input("\nEnter the mass (kg) of the object: "))
    
    #Validate that input is greater than 0
    while m <= 0:
        print("ERROR: mass must be greater than 0")
        m = float(input("\nEnter the mass (kg) of the object: "))

    #Prompt the user to input the velocity of the object
    v = float(input("\nEnter the velocity (m/s) of the object: "))

    #Validate that the input is greater than 0
    while v <= 0:
        print("ERROR: velocity must be greater than 0")
        v = float(input("\nEnter the velocity (m/s) of the object: "))
    
    #Calculate the kinetic energy
    
    KE = 1/2 * m * v**2
    return KE

#Calling the main module
main()
