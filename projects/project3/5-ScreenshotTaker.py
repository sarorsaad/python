# Create a python script that take a desktop screenshot every minute , and save them in a new folder on the desktop

# Program to take screenshot
import schedule   
import pyscreenshot
def screenshots():
    image = pyscreenshot.grab()
    image.show()
    image.save("Task.png")

schedule.every(10).minutes.do(screenshots)
s = screenshots()