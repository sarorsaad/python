# create a python function that takes a text from the user and print the text in colors

from cgi import test
from termcolor import colored
def textcolor(color):
    global text
    text = input("type ur word: ")
    return colored(text ,color)

red = textcolor("green")
print(red)