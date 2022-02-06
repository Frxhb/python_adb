
def download_magisk_zip():
    import os
    import os.path
    import glob

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


    print("Downloading latest magisk zip....\n")
    os.system("wget -q https://github.com/$(wget -q https://github.com/topjohnwu/Magisk/releases/latest -O - | egrep '/.*/.*/.*apk' -o) >/dev/null 2>&1")

    cwd = os.getcwd()

    if any(File.startswith("Magisk") and File.endswith(".apk") for File in os.listdir(cwd)):
        print(bcolors.OKGREEN + "Download successful!\n" + bcolors.ENDC)
        print(bcolors.OKGREEN + "You can find your file here:"+bcolors.ENDC)

        apk_files = glob.glob('*.apk')
        magisk_files_first = apk_files[0]
        clip_remove = magisk_files_first.replace("[","").replace("]","").replace("'","")

        print(bcolors.BOLD + cwd + "/magisk/" + clip_remove + bcolors.ENDC)

        os.system("mv ./*.apk ./magisk/")
         
    else:
        print(bcolors.FAIL + "Download failed. Please download magisk manually!\nYou can find more infos here:\nhttps://github.com/topjohnwu/Magisk" + bcolors.ENDC)