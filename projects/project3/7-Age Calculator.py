#  create a python function that takes user birthdate and prints how old he is

from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
             (birthDate.month, birthDate.day))
    return age
print(calculateAge(date(1973, 10, 28)), "years")