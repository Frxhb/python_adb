import os
import check_adb_connection
import restart_bootloader
import time

check_adb_connection.check_adb_con()
#call check connection

ask_user_fastboot = input ("Do you want to reboot into fastboot mode?\nY/n\n>>>")
#ask user if wants to reboot into fastboot mode

if ask_user_fastboot in ['yes', 'Yes', 'Y', 'y']:

    restart_bootloader.restart_bootloader_func()
    #booting into fastboot mode
    print("Entering fastboot mode ...")

    time.sleep(10)

    print("I have found the following devices:")
    os.system("fastboot devices")
    #checking if device was successfuly booted into fastboot mode

else:
    print("ok....")