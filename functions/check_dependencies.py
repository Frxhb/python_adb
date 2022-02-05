import os
import subprocess
import sys
from packaging import version
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
    print (bcolors.OKBLUE + "1.  ppab-module\n" + bcolors.ENDC)

    def ppadb_dependecy():

        ppadbfile_one= os.path.exists('/usr/local/lib/python3.8/dist-packages/ppadb')
        ppadbfile_two=os.path.exists('/home/francesco/.local/lib/python3.8/site-packages/ppadb/')

        if (ppadbfile_one == True) or (ppadbfile_two == True):
            print (bcolors.OKGREEN + "      ppadb is installed! ✓\n" + bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      ppadb isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the ppadb module.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing ppadb-module...")
                package_ppadb = "pure-python-adb"
                def install(package_ppadb):
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package_ppadb])
                install(package_ppadb) 
            else:
                print("Okay! Close program now.\n")
                exit()

    ppadb_dependecy()

    print (bcolors.OKBLUE + "2.  python-version\n"+ bcolors.ENDC)

    def python_dependency():
        sys_ver = sys.version
        sliced_sys_ver = sys_ver[0:7]
        replaced_string = sliced_sys_ver.replace(" ", "")

        numeric_string_pyver = re.sub("[^0-9]", "", replaced_string)

        destination_ver = "3.6"

        print(bcolors.WARNING + "Your python versio seemts to be...\n" + bcolors.ENDC)
        time.sleep (1)
        print (bcolors.WARNING + replaced_string + bcolors.ENDC +"\n")

        if version.parse(replaced_string) >= version.parse(destination_ver):
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



    print (bcolors.OKBLUE + "3.  python3-pip\n"+ bcolors.ENDC)
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

    print (bcolors.OKBLUE + "4.  adb\n"+ bcolors.ENDC)

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

    def pack_dep():

        pack_dep_file = ('/usr/lib/python3/dist-packages/pip/_internal/utils/packaging.py')
        
        if (pack_dep_file == True):
            print (bcolors.OKGREEN + "      packaging is installed! ✓\n" + bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      packaging isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the packacking module.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing packaging...")
                os.system("pip install packaging")
            else:
                print("Okay! Close program now.\n")
                exit()
    pack_dep()

    sys_ver = sys.version
    sliced_sys_ver = sys_ver[0:7]
    destination_ver = "3.6"
    if version.parse(sliced_sys_ver) >= version.parse(destination_ver):
        print("")

    ppadbfile_one= os.path.exists('/usr/local/lib/python3.8/dist-packages/ppadb')
    ppadbfile_two=os.path.exists('/home/francesco/.local/lib/python3.8/site-packages/ppadb/')

    python_pip_one_location= os.path.exists('/usr/bin/pip')
    python_pip_two_location= os.path.exists('/usr/bin/pip3')

    adb_file=os.path.exists('/usr/bin/adb')

    pack_dep_file = ('/usr/lib/python3/dist-packages/pip/_internal/utils/packaging.py')


    if (ppadbfile_one == True) or (ppadbfile_two == True) and (python_pip_one_location == True) or (python_pip_two_location == True) and (adb_file == True) and (pack_dep_file):
        print (bcolors.OKGREEN + "Everything seems to be fine! We can continue!\n" + bcolors.ENDC)
        time.sleep(2)
        print ("Clearing for better view....")
        time.sleep(1)
        os.system("clear")
    else:
        print(bcolors.FAIL + "Error occured. Please check your dependencies manually:\n1. Python 3.6x+\n2. Python3-pip\n3. pure-python-adb\n4. packaging" + bcolors.ENDC)