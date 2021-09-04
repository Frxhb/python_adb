## Tkinter for python_adb

from   tkinter import *
import string
from typing import Collection
import time
import os

from functions import connect_to_client
from functions import install_apk
from functions import adb_shell_pm
from functions import adb_shell
from functions import reboot_recovery
from functions import restart_bootloader
from functions import restart_phone
from functions import uninstall_apk

def close_window():
    root.destroy()

root = Tk()
root.title("ADB_PYTHON_GUI")
root.geometry("600x600") 

Button1 = Button(root, text="RUN", command=connect_to_client.connect_to_client)
Button1.grid(row=2, column=2)