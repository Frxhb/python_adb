import os
import subprocess
import sys
import time

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

    print(bcolors.WARNING + "##################### Dependency Check ###########################################\n\n" + bcolors.ENDC)
    print(bcolors.WARNING + "In order to run this script, a few dependencies are required. You may need to enter your sudo passwd.Going to install them..." + bcolors.ENDC)
    print(bcolors.WARNING + "Required dependencies:\n\n" + bcolors.ENDC)
    print(bcolors.OKCYAN + "-    android-tools-adb" + bcolors.ENDC)
    print(bcolors.OKCYAN + "-    pure-python-adb"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "-    packaging"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "-    pip3"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "-    python3.6x"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "-    fastboot-tools\n\n"+ bcolors.ENDC)
    print(bcolors.WARNING + "##################################################################################\n" + bcolors.ENDC)

    def pip_dep():

        python_pip_one_location= os.path.exists('/usr/bin/pip')
        python_pip_two_location= os.path.exists('/usr/bin/pip3')

        if (python_pip_one_location == True) or python_pip_two_location == True:
            print("")
        else:
            print (bcolors.WARNING + "      python3-pip isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the python3-pip.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing python3-pip...")
                os.system("sudo apt install python3-pip -y")
            else:
                print("Okay! Close program now.\n")
                exit()

    pip_dep()

    def pack_dep():
        os.system("pip3 install packaging")
    pack_dep()

    def bsfour_dep():
        os.system("pip3 install beautifulsoup4")
    bsfour_dep()

    def ppadb_dependecy():
        os.system("pip3 install -U pure-python-adb")   

    ppadb_dependecy()

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
            print (bcolors.OKGREEN + "[✓] Your python version is compatible...\n" + bcolors.ENDC)
        else:
            print (bcolors.FAIL + "[x]Your installed version is not compatible..." + bcolors.ENDC)
            ask_user_update_python = input ("You want to install the compatible python version (3.6.x)?\nY/n\n>>>")
            if ask_user_update_python in ["Yes", "y", "Y", "yes"]:
                os.system("sudo apt install python3 -y")
            else:
                print("Okay! Close program now.\n")
                exit()

    python_dependency()

    def adb_dep():

        adb_file=os.path.exists('/usr/bin/adb')

        if (adb_file == True):
            print ("")
        else:
            print (bcolors.WARNING + "      adb isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the adb module.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing adb...")
                os.system("sudo apt install android-tools-adb -y")
            else:
                print("Okay! Close program now.\n")
                exit()

    adb_dep()

    def fastboot_tools_install():

        fastboot_file=os.path.exists('/usr/bin/fastboot')

        if (fastboot_file == True):
            print ("")
        else:
            print (bcolors.WARNING + "      fastboot isn't installed! ✕\n" + bcolors.ENDC)
            ask_user_install_ppadb = input("To move on you need to install the fastboot module.\nYou want to install it now?\nY/n\n>>>")
            if ask_user_install_ppadb in ['yes', 'Yes', 'Y', 'y']:
                print("Installing fastboot...")
                os.system("sudo apt install fastboot -y")
            else:
                print("Okay! Close program now.\n")
                exit()
    
    fastboot_tools_install()

#  + ">/dev/null 2>&1"