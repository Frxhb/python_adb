from ppadb.client import Client as AdbClient
import subprocess

def check_adb_con():

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