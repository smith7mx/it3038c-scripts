from datetime import datetime
import os

time=datetime.now()
current=time.strftime("%H:%M:%S")
print("The time is:", current)
print("Current signed in User: " + os.getlogin())
print("Current Working Directory: " + os.getcwd())