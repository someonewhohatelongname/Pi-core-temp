import os
import time
from tkinter import *


root = Tk()

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

#while True:
        #print(measure_temp())
        #time.sleep(1)
def output():
    
    w.pack()
    root.after(1000, output)
    w.config(text=measure_temp()) 
    
w = Label(root,text=measure_temp())    
output()

    
root.mainloop()
    