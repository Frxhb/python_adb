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

def adb_shell_pm_function():        

        print("Which Apps do you want to display?\n")
        print(bcolors.OKBLUE + "1. Third party apps\n" + bcolors.ENDC)
        # print("or\n")
        print(bcolors.WARNING + "2. System apps\n" + bcolors.ENDC)
        # print("or\n")
        print(bcolors.OKGREEN + "3. All packages\n" + bcolors.ENDC)
        print("Just type in the number and press enter:\n")

        app_list_input = input(">>> ")

        if app_list_input in ['1', 'one', 'One', 'Third party apps']:
            os.system("adb shell pm list packages -3")

        elif app_list_input in ['2', 'two', 'Two', 'System apps']:
            os.system("adb shell pm list packages -s")

        elif app_list_input in ['3', 'three', 'Three', 'All packages']:
            os.system("adb shell pm list packages")