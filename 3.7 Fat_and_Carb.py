#Joel Christian

#A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her
#evaluation, she asks members for the number of fat grams and carbohydrate grams that they
#consumed in a day. Then, she calculates the number of calories that result from the fat, using the
#following formula: Calories from Fat = Fat Grams × 9
#Next, she calculates the number of calories that result from the carbohydrates, using the following
#formula: Calories from Carbs = Carb Grams × 4
#The nutritionist asks you to design a modular program that will make these calculations.

#This program accepts the number of fat and carbohydrates gram consumed,
#calculates the total calories using fat grams,
#calculates the total calories using catbohydrates gram,
#then calculates the total calories from fat and carb calories
#and displays the total calories results.

#Create global constants
FATCAL_MULTIPLIER = 9
CARBCAL_MULTIPLIER = 4

#Create and initialize a global variable to store the total calories
totalCalories = 0

def main():
    #Get the number of fat grams
    inputFat = float(input("Enter the number of fat grams consumed: "))
    
    #Get the number of carbohydrates grams
    inputCarb = float(input("enter the number of carbohydrates grams consumed: "))

    #Calculates and displays the number of fat calories
    setFat(inputFat)
    #Calculates and displays the number of carb calories
    setCarb(inputCarb)
    #Displays the total calories from both fat and carbs
    print("The total number of calories consumed is: ", totalCalories)

#The setFat function calculates and displayes the total number of fat calories
#and adds it to the total calories
def setFat(totalFat):
    fatCal = totalFat * FATCAL_MULTIPLIER
    global totalCalories
    totalCalories = totalCalories + fatCal
    print("The total number of Fat Calories is:", fatCal)

#The setCarb function calculates and displays the total number of carbohydrates calories
#and adds it to the total calories
def setCarb(totalFat):
    carbCal = totalFat * CARBCAL_MULTIPLIER
    global totalCalories
    totalCalories = totalCalories + carbCal
    print("The total number of Carbohydrates Calories is:", carbCal)

#Call the main function
main()
