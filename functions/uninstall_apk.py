import time

from functions import adb_shell_pm


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



def uninstall_app_func():

    adb_shell_pm.adb_shell_pm_function()

    print(bcolors.WARNING + "\nBefore we start the uninstall. Please make sure which app you want to uninstall. This procedure cant be undone." +bcolors.ENDC)
    #Here we ask the user if he really wants to uninstall apk

    print('\n' * 2)

    uninstall_app = input("Which app do you want to uninstall. Please enter the package name (like com.instagram.android) and press enter\n\n>>> ")

    print('\n' * 2)


    print("Okay, u want to uninstall:\n" , uninstall_app)


    print("I will now uninstall" , uninstall_app ,  "from your device in\n3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    def uninstall_apk():
        from ppadb.client import Client as AdbClient
        # Default is "127.0.0.1" and 5037
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        for device in devices:
            device.uninstall(uninstall_app)
    uninstall_apk()
    #call install apk function (in this case we use kik.apk)