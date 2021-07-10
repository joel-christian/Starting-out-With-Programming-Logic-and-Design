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

    #Get the mass of the object
    m = getMass()

    #Get the velocity of the object
    v = getVelocity()

    #Calculate the kinetic energy of the object
    ke = calcKE(m, v)

    #Display the result
    print("\nThe kinetic energy of the object is: ", format(ke, '.2f'), "joules.")

#The getMass module prompts the user to enter the mass of the object,
#validates that the value is greater than 0,
#and returns the value to the main module
def getMass():

    #Prompt the user to input the mass of the object
    mass = float(input("\nEnter the mass (kg) of the object: "))
    
    #Validate that input is greater than 0
    while mass <= 0:
        print("ERROR: Mass must be greater than 0")
        mass = float(input("\nEnterthe mass (kg) of the object: "))
    return mass

#The getVelocity module prompts the user to enter the velocity of the object,
#validates that the value is greater than 0,
#and returns the value to the main module
def getVelocity():

    #Prompt the user to input the velocity of the object
    velocity = float(input("\nEnter the velocity (m/s) of the object: "))

    #Validate that the input is greater than 0
    while velocity <= 0:
        print("ERROR: Velocity must be greater than 0")
        velocity = float(input("\nEnter the velocity (m/s) of the object: "))
    return velocity

#The calcKE module calculates the kinetic energy of the object
def calcKE(m, v):
    
    KE = 1/2 * m * v**2
    return KE

#Calling the main module
main()
