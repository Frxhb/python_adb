from asyncore import dispatcher_with_send
import subprocess
from ppadb.client import Client as AdbClient
from bs4 import BeautifulSoup
from urllib.request import urlopen
import wget
import os
import time

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


def download_twrp_func():
    
    client = AdbClient(host="127.0.0.1", port=5037)
    adb_devicesL = subprocess.run(['adb' , 'devices' , '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    device = client.device(adb_devicesL)
    model_check = "model"

    if str(model_check) in str(adb_devicesL):
        print(bcolors.OKGREEN + "Adb connection works ✓\n"+bcolors.ENDC)
        print("I have found the following device ID:\n")
        print(bcolors.OKGREEN + adb_devicesL.split()[9] + bcolors.ENDC)
        print("\n")

        device_output = (adb_devicesL.split()[9])
        just_device = (device_output[7:])
        download_link_without_device = "https://dl.twrp.me/"
        download_link_twrp = "https://dl.twrp.me"
        link_with_device = download_link_without_device + just_device
        
        url = download_link_without_device + just_device
        html_doc = urlopen(url)
        # defining html link (twrp...)
        soup = BeautifulSoup(html_doc, "html.parser")
        links = []
        for link in soup.find_all('a'):
            links.append((link.get('href')))

        # target strings variable will contain all the links that end with .img.html 
        target_strings =[]
        for i in links:
            if '.img.html' in i:
                target_strings.append(i)

        # and if needed in the future you can extract a single element from the list:
        first_link = target_strings[0]
        #Here we extract the first link from link list

        end_string_link = first_link.replace(".html","")
        #here we cut the "html" cause we cant just link ends with ".img"

        download_link_end = download_link_twrp + end_string_link
    
        print("Now I will download the latest twrp-recovery for your device...:\n")
        print(download_link_end)
        wget.download(download_link_end)

        time.sleep(1)

        cwd = os.getcwd()
        end_file_twrp_dir = cwd + "/twrp_files"
        print (end_file_twrp_dir)

        if any(File.startswith("twrp") and File.endswith(".img") for File in os.listdir(cwd)):
            print(bcolors.OKGREEN + "\n\nDownload successful!\n" + bcolors.ENDC)

            parent_dir = (cwd + "/twrp_files/")
            dir = just_device
            path = os.path.join(parent_dir, dir)
            os.mkdir(path)

            os.system("mv *.img ./twrp_files/" + just_device + ">/dev/null 2>&1")

            print(bcolors.OKGREEN + "You can find your file here:"+bcolors.ENDC)
            print(bcolors.BOLD + end_file_twrp_dir + end_string_link + bcolors.ENDC) 

    else:
        print(bcolors.FAIL + "I haven't found any device. Please make sure your device is connected sucessfully!" + bcolors.ENDC)