import os
import time
import glob

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

def install_app_func():

    print("Before we start the installation. Please put your apk files which u want to install under ./python_adb/apks <-")
    #Here we ask the user if he wants to add more .apks to the given folder.

    print('\n' * 2)

    input("Press enter when you want to move on...")

    print('\n' * 2)


    print("I have found the following files:")

    initial_count = 0
    direc = ('./apks')
    files = os.listdir(direc)

    os.chdir(direc)
    for file in glob.glob("*.apk"):
        initial_count += 1
        print('[', initial_count, ']' , file)

    inp = input("Which apk do you want to install? Please just type in a number and press enter.\n>>>")
    apk_choice = files[int(inp)-1]

    print('\n' * 1)
    #input("Which apk do you want to install?")


    print(bcolors.WARNING+ "Please check your phone! You may need to manually accept the installation." + bcolors.ENDC)

    time.sleep(3)

    print("I will install" , apk_choice ,  "on your device in\n3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    joint_path = os.path.expanduser('./apks/' +apk_choice)
    #Hier nutzt man os.path um den /home/username dynmaisch zu gestalten
        
    from ppadb.client import Client as AdbClient
    apk_path = joint_path
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
        
    devices = client.devices()
    for device in devices:
        os.system("adb install " + apk_choice)