## Tkinter for python_adb
from functions.adb_shell import adb_shell_function
from   tkinter import *
import tkinter as tk
import string
from typing import Collection
import subprocess
import time
import os
    

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def connect_phone():
    
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    global adb_devicesL
    adb_devicesL = subprocess.run(['adb' , 'devices' , '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    global device
    device = client.device(adb_devicesL)
    model_check = "model"
    if str(model_check) in str(adb_devicesL):
        text1.configure(state='normal')
        text1.delete('1.0', END)
        text1.insert(END, "I have found the following device:\n")
        text1.insert(END, "\n")
        text1.insert(END, adb_devicesL.split()[8])
        text1.insert(END,"\n")
        text1.insert(END, adb_devicesL.split()[7])
        text1.configure(state='disabled')
    else:
        text1.insert(END, "No device connected!\nCheck your connection.")

def disc_phone():
    disconnet_phone = subprocess.run(['adb' , 'disconnect'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    cutt = disconnet_phone.title()

    text1.configure(state='normal')
    text1.delete('1.0', END)
    text1.insert(END,cutt)
    text1.configure(state='disabled')

def close_window(): 
    root.destroy()  

def list_pm_packages():
    list_all_packages = subprocess.run(['adb' , 'shell' , 'pm' ,'list' , 'packages'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace('package:', '')

    text2.configure(state='normal')
    text2.insert('end', list_all_packages)
    text2.configure(state='disabled')

root = Tk()
root.title("ADB GUI")
root.geometry("800x800")

btn1 = Button(root, text="Connect to client", command=connect_phone)
btn1.grid(row=2, column=1)

btn2 = Button(root, text="Disconnect client",command=disc_phone)
btn2.grid(row=3, column=1)

btn4 = Button(root, text="Beenden",command=close_window)
btn4.grid(row=4, column=3)


btn5= Button(root, text="List packages",command=list_pm_packages)
btn5.grid(row=4, column=1)

text1 = Text(root, height = 10, width = 70)
text1.grid(row=1, column=0)
text1.configure(state='disabled')

text2= Text(root, height = 10, width = 70)
text2.grid(row=4, column=0)
text2.configure(state='disabled')



def retrieve_input():

    text4.configure(state='normal')
    
    text4.delete("1.0","end-1c")

    value = text3.get("1.0","end-1c")

    text4.insert('end', value)
    text4.configure(state='disabled')


text3= Text(root, height = 5, width = 35)
text3.grid(row=6, column=0)

WSignUp = Button(root, text="print text", command=retrieve_input).grid(row=3, column=0, sticky=W) #button

text4= Text(root, height = 5, width = 35)
text4.grid(row=7, column=0)
text4.configure(state='disabled')

lbl_phone_status = Label(root, font=("times", 15))
lbl_phone_status.grid(row=0, column=0)
lbl_phone_status.config(text="Phone Status")

lbl_app_list = Label(root, font=("times", 15))
lbl_app_list.grid(row=3, column=0)
lbl_app_list.config(text="App List")

what_uninstall = Label(root, font=("times", 15))
what_uninstall.grid(row=5, column=0)
what_uninstall.config(text="What uninstall?")

root.mainloop()
