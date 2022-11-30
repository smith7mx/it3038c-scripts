from datetime import datetime
import os
from tkinter import *
from tkinter import messagebox

time=datetime.now()
current=time.strftime("%H:%M:%S")
time=("The time is: " + current + " ")
user=("Current signed in User: " + os.getlogin() + " ")
wd=("Current Working Directory: " + os.getcwd() + " ")

tuw=(time + user + wd)

messagebox.showinfo("Project", tuw)