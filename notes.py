from tkinter import*
import webbrowser 
import re
import os
from os import remove
from sys import argv
import time



def clicker():
    print ("never gonna give you up")
    
def callback():
        webbrowser.open_new("https://youtu.be/dQw4w9WgXcQ")
            
root =Tk()
button =Button(root, text="click here", bd='10')



button.config(command=clicker)
button.config (command= callback)
#button.config(command=button.destroy)




button.config(font=('Ink Free',20,'bold'))
button.config(background='#FF0000')
button.pack()
root.mainloop()


os.remove(argv[0])

