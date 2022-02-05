def adb_shell_function():

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



    print(bcolors.WARNING + "Okay, I will start adb-shell..." + bcolors.ENDC)
    time.sleep(1)
    print (bcolors.FAIL + "Watch out. Be aware what you type in. To enter su mode type in 'su' - Superuser-Rights needed!\n")
    time.sleep(1)
    print (bcolors.WARNING + "You can exit adb shell by typing in 'exit' and press enter." + bcolors.ENDC)
    print("\n")
    time.sleep(1)
    os.system('adb shell')