#Imports needed
from datetime import datetime
import os
from tkinter import *
from tkinter import messagebox

#setting variables
time=datetime.now()
current=time.strftime("%H:%M:%S")
time=("The time is: " + current + " ")
user=("Current signed in User: " + os.getlogin() + " ")
wd=("Current Working Directory: " + os.getcwd() + " ")

#combines all variables into one
tuw=(time + user + wd)

#code for popup window
messagebox.showinfo("Project", tuw)