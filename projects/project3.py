# Number to words .
#  Create a python function that takes an integer number and print the number in words
from num2words import num2words
def words(Given_Number): #give i number and output word of this number
    if Given_Number == int(Given_Number):
        return num2words(Given_Number)
    else:
        return "Plese Type i number..."

sixty = words(60)