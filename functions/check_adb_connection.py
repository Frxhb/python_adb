from ppadb.client import Client as AdbClient
import subprocess

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

def check_adb_con():

    client = AdbClient(host="127.0.0.1", port=5037)
    global adb_devicesL
    adb_devicesL = subprocess.run(['adb' , 'devices' , '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    global device
    device = client.device(adb_devicesL)
    model_check = "model"
    if str(model_check) in str(adb_devicesL):
        print(bcolors.OKGREEN + "Adb connection works ✓\n"+bcolors.ENDC)
        print("I have found the following device(s):\n")
        print(bcolors.OKGREEN + adb_devicesL.split()[9] + bcolors.ENDC)
        print(bcolors.OKGREEN + adb_devicesL.split()[8] + bcolors.ENDC)
        print(bcolors.OKGREEN + adb_devicesL.split()[7] + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "I haven't found any device. Please make sure your device is connected sucessfully!" + bcolors.ENDC)