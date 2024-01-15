import random

minValue = int(input("Let's input min value! \n"))
maxValue = int(input("Then input the max value! \n"))

randomValue = random.randint(minValue, maxValue)


while True:
    choiceValue = int(input("Let's guess the number! \n"))
    if randomValue == choiceValue:
        print("It's correct!! Nice choice")
        break
    else:
        print("It's incorrect. Try again!")


