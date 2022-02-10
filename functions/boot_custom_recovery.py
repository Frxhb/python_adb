import time , os , subprocess , glob

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

def boot_custom_rec():

    print (bcolors.WARNING + "Attention! You are going to boot a custom recovery. Please make sure you know what to do!\n" + bcolors.ENDC)

    ask_user_boot = input("You want to move on?\nY/n >>>")

    if ask_user_boot in ["y" , "Y" , "yes" , "Yes"]:
        print ("\nOkay, we will move on ...")
    else:
        print("Okay, exiting program ...")
        time.sleep(1)
        exit()

    print("Booting into bootloader ...")
    os.system("adb reboot bootloader")
    time.sleep(15)
    
    print("Now checking fastboot connection ...")

    output = str(subprocess.check_output("fastboot devices" , shell=True))
    print(output)

    if "fastboot" in str(output):
        print(bcolors.OKGREEN + "Successfuly rebootet in fastboot mode!" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Something went wrong. Please check your device." + bcolors.ENDC)
        time.sleep(1)
        exit()

    print("I have found the following recovery .img files:")

    initial_count = 0
    directory = ('./recovery')
    rec_files = os.listdir(directory)

    os.chdir(directory)

    for file in glob.glob("*.img"):
        initial_count += 1
        print('[', initial_count, ']' , file)

    inp = input("Which recovery do you want to boot? Please just type in a number and press enter.\n>>>")
    rec_choice = rec_files[int(inp)-1]
    joint_path = os.path.expanduser('./recovery/' +rec_choice)
    rec_path = joint_path

    rec_path_cut = rec_path[10:]
    cwd = os.getcwd()

    cwd_and_rec = cwd + rec_path_cut
    

    print("so?" + cwd_and_rec)

    print('\n' * 1)

    print("I will boot" , rec_choice ,  "to your device ...")

    time.sleep(1)

    print(rec_choice)
    print(rec_path)

    os.system("fastboot boot " + cwd_and_rec)