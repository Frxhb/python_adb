import subprocess 
#Import subprocess module to be able to start subprocesses
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

def connect_to_client():

    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    global adb_devicesL
    adb_devicesL = subprocess.run(['adb' , 'devices' , '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    global device
    device = client.device(adb_devicesL)
    model_check = "model"
    if str(model_check) in str(adb_devicesL): 
        print("I have found the following device:\n")
        print(adb_devicesL.split()[8])
        print(adb_devicesL.split()[7])
    else:
        print(bcolors.FAIL + "No device found.\nPlease make sure your device is properly connected and usb-debugging is enabled.\n\n" + bcolors.ENDC)
        ask_again = input("Would you like to re-run the programm? Y/n:\n>>>")
        if ask_again in ['yes', 'Yes' , 'Y' , 'y']:
            connect_to_client()
        else:
            print(bcolors.FAIL+ "Okay, programm will close." + bcolors.ENDC)
            exit()

connect_to_client()