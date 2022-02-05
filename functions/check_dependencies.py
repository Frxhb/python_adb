import os
from pydoc import cli
import subprocess
import sys
import time
import re

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

def check_all_dependencies():


    print (bcolors.WARNING + "Going to check your dependencies...\n" + bcolors.ENDC)

    print (bcolors.OKBLUE + "-  packaging-module\n" + bcolors.ENDC)

    def pack_dep():
        os.system("pip3 install packaging")
    pack_dep()

    print (bcolors.OKBLUE + "-  python3-pip\n"+ bcolors.ENDC)
    def pip_dep():

        python_pip_one_location= os.path.exists('/usr/bin/pip')
        python_pip_two_location= os.path.exists('/usr/bin/pip3')

        if (python_pip_one_location == True) or python_pip_two_location == True:
            print (bcolors.OKGREEN + "      python3-pip is installed! ✓\n" + bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      python3-pip isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the python3-pip.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing python3-pip...")
                os.system("sudo apt install python3-pip")
            else:
                print("Okay! Close program now.\n")
                exit()

    pip_dep()

    print (bcolors.OKBLUE + "-  ppab-module\n" + bcolors.ENDC)

    def ppadb_dependecy():
        os.system("pip install -U pure-python-adb")    

    ppadb_dependecy()

    print (bcolors.OKBLUE + "-  python-version\n"+ bcolors.ENDC)

    def python_dependency():
        from packaging import version
        sys_ver = sys.version
        sliced_sys_ver = sys_ver[0:7]
        clip_remove = sliced_sys_ver.replace("(","").replace(")","")

        destination_ver = "3.6"

        print(bcolors.WARNING + "Your python version seemts to be...\n" + bcolors.ENDC)
        time.sleep (1)
        print (bcolors.WARNING + clip_remove + bcolors.ENDC +"\n")

        if version.parse(clip_remove) >= version.parse(destination_ver):
            print (bcolors.OKGREEN + "[✓]Your python version seems to be compatible...\n" + bcolors.ENDC)
        else:
            print (bcolors.FAIL + "[x]Your installed version is not compatible..." + bcolors.ENDC)
            ask_user_update_python = input ("You want to install the compatible python version (3.6.x)?\nY/n\n>>>")
            if ask_user_update_python in ["Yes", "y", "Y", "yes"]:
                os.system("sudo apt install python3")
            else:
                print("Okay! Close program now.\n")
                exit()

    python_dependency()

    print (bcolors.OKBLUE + "-  adb\n"+ bcolors.ENDC)

    def adb_dep():

        adb_file=os.path.exists('/usr/bin/adb')

        if (adb_file == True):
            print (bcolors.OKGREEN + "      adb is installed! ✓\n" + bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      adb isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the ppadb module.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing adb...")
                os.system("sudo apt install android-tools-adb")
            else:
                print("Okay! Close program now.\n")
                exit()

    adb_dep()