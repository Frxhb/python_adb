# Author:

 #Francesco (Frxhb)
# Date:
 # 01.08.2021
# Edited:
 # 05.02.2022
# OS:
 # linux-mint 20.2 Cinnamon / Ubuntu

# First we need to import all modules we need:
import time
# Import time to use functions like time.sleep
import os
# Import os to use e.g. os.path.expanduser

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

def banner():
    print("")
    print(bcolors.FAIL + "##################################################################################" + bcolors.ENDC)
    print(bcolors.OKBLUE + "#  ______     __  __     _________   ___   ___      ______       ___   __        #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "# /_____/\   /_/\/_/\   /________/\ /__/\ /__/\    /_____/\     /__/\ /__/\      #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "# \:::_ \ \  \ \ \ \ \  \__.::.__\/ \::\ \\  \ \   \:::_ \ \     \::\_\\   \ \     #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#  \:(_) \ \  \:\_\ \ \    \::\ \    \::\/_\ .\ \   \:\ \ \ \    \:. `-\  \ \    #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "#   \: ___\/   \::::_\/     \::\ \    \:: ___::\ \   \:\ \ \ \    \:. _    \ \   #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "#    \ \ \       \::\ \      \::\ \    \: \ \\::\ \   \:\_\ \ \     \. \`-\  \ \  #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#     \_\/        \__\/       \__\/     \__\/ \::\/    \_____\/     \__\/ \__\/  #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "#                                                                                #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "#                          ________       ______        _______                  #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#                         /_______/\     /_____/\     /_______/\                 #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "#                         \::: _  \ \    \:::_ \ \    \::: _  \ \                #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "#                          \::(_)  \ \    \:\ \ \ \    \::(_)  \/_               #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#                           \:: __  \ \    \:\ \ \ \    \::  _  \ \              #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "#                            \:.\ \  \ \    \:\/.:| |    \::(_)  \ \             #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "#                             \__\/\__\/     \____/_/     \_______\/             #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#                                                                                #"+ bcolors.ENDC)
    print(bcolors.OKGREEN + "#                                                                                #"+ bcolors.ENDC)
    print(bcolors.OKCYAN + "#                                                                                #"+ bcolors.ENDC)
    print(bcolors.OKBLUE + "#                                                    by: @Frxhb and @LemonTaste77#" +bcolors.ENDC)
    print(bcolors.FAIL + "##################################################################################" + bcolors.ENDC)


banner()
# Call banner

print('\n' * 2)

from functions import check_dependencies

check_dependencies.check_all_dependencies()

from functions import install_apk
from functions import adb_shell_pm
from functions import adb_shell
from functions import reboot_recovery
from functions import restart_bootloader
from functions import restart_phone
from functions import uninstall_apk
from functions import check_adb_connection
from functions import magisk_func
from functions import download_twrp
from functions import fastboot_connect
from functions import boot_custom_recovery
#import of all functions

def main_function():

    def ask_user_run():
    
        user_input = input('\nWould you like to do something else? Y/n >>>')

        if user_input in ['yes', 'Yes', 'Y', 'y']:
            main_function()
        else:
            print("Okay, program will close in 2 seconds...\n")
            time.sleep(2)
            exit()


    os.system('adb start-server')
    #subprocess.run(['chmod' , '777', './connect_to_client.py'])
    # giving permissions
    from functions import connect_to_client
    connect_to_client
    # Call connect to client function

    print('\n' * 2)

    print("You can choose between those functions right now:\n")

    print(bcolors.OKBLUE + "APK:\n" + bcolors.ENDC)
    print("     1. Install")
    print("     2. Uninstall\n")
    print(bcolors.OKBLUE + "Reboot phone:\n" + bcolors.ENDC)
    print("     3. Normal reboot")
    print("     4. Reboot into bootloader")
    print("     5. Reboot into stock recovery\n\n")
    print(bcolors.OKBLUE + "Start shell:\n" + bcolors.ENDC)
    print("     6. ADB-shell\n")
    print("     7. List installed apps\n")
    print(bcolors.OKBLUE + "Fastboot utilities:\n" + bcolors.ENDC)
    print("     8. Download latest custom recovery -> twrp.img\n")
    print("     9. Reboot into fastboot\n")
    print("     10. Boot custom recovery (twrp)\n")
    print(bcolors.OKBLUE + "Other:\n" + bcolors.ENDC)
    print("     11. Check ADB connection\n")
    print("     12. Download latest magisk.zip\n")


    #del choose_function
    global choose_function8
    choose_function = input("Which tool do you want to use?\n\n>>>")

    if choose_function == "1":
        print("Okay, you want to install an apk. Lets go...")
        install_apk.install_app_func()

    elif choose_function == "2":
        print("Okay, you want to uninstall an apk. Lets go...")
        uninstall_apk.uninstall_app_func()

    elif choose_function == "3":
        ask_user_restart = input(
            bcolors.WARNING + "Are you sure you want to restart your phone?\nY/n\n\n>>>" + bcolors.ENDC)
        if ask_user_restart in ['yes', 'Yes', 'Y', 'y']:
            print("Okay, you want to restart your phone. Lets go...")
            time.sleep(1)
            print(bcolors.OKGREEN +
                  "Sucessfully rebooted your phone!\n" + bcolors.ENDC)
            restart_phone.restart_phone_func()
        else:
            print("Okay!\n")

    elif choose_function == "4":
        ask_user_restart_bloader = input(
            bcolors.WARNING + "Are you sure you want to restart your phone into bootloader?\nY/n\n>>>" + bcolors.ENDC)
        if ask_user_restart_bloader in ['yes', 'Yes', 'Y', 'y']:
            print("Okay, you want to restart your phone. Lets go...")
            restart_bootloader.restart_bootloader_func()
        else:
            print("Okay!\n")

    elif choose_function == "5":
        ask_user_restart_rec = input(
            bcolors.WARNING + "Are you sure you want to restart your phone into recovery?\nY/n\n>>>" + bcolors.ENDC)
        if ask_user_restart_rec in ['yes', 'Yes', 'Y', 'y']:
            print("Okay, you want to restart your phone. Lets go...")
            reboot_recovery.reboot_recovery_func()
        else:
            print("Okay!Close program now.\n")

    elif choose_function == "6":
        ask_user_restart = input(
            bcolors.WARNING + "Are you sure you want to start ADB shell??\nY/n\n>>>" + bcolors.ENDC)
        if ask_user_restart in ['yes', 'Yes', 'Y', 'y']:
            adb_shell.adb_shell_function()
        else:
            print("Okay!\n")

    elif choose_function == "7":
        adb_shell_pm.adb_shell_pm_function()

    elif choose_function == "8":
        download_twrp.download_twrp_func() 

    elif choose_function == "9":
        fastboot_connect.fastboot_func()
        
    elif choose_function == "10":
        #boot custom recovery
        boot_custom_recovery.boot_custom_rec()

    elif choose_function == "11":
        check_adb_connection.check_adb_con()
    
    elif choose_function == "12":
        magisk_func.download_magisk_zip()
        
    else:
        print(bcolors.FAIL + "Wrong choice!" + bcolors.ENDC)


    ask_user_run()

main_function()