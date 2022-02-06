def download_magisk_zip():

    from ast import And
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
    os.system("wget -q https://github.com/$(wget -q https://github.com/topjohnwu/Magisk/releases/latest -O - | egrep '/.*/.*/.*zip' -o) >/dev/null 2>&1")

    magisk_file = str((glob.glob("*.zip")))
    new_file_name = ("magisk_" +magisk_file)
    clip_remove = new_file_name.replace("[","").replace("]","").replace("'","")
    end_file_dir = './magisk/' + clip_remove
    os.system("mv ./*.zip ./magisk/" + clip_remove + ">/dev/null 2>&1") 

    magisk_dir = "./magisk/"
    if any(File.startswith("magisk") and File.endswith(".zip") for File in os.listdir(magisk_dir)):
        print(bcolors.OKGREEN + "Download sucessfully!\n" + bcolors.ENDC)
        print(bcolors.OKGREEN + "You can find your file here:"+bcolors.ENDC)
        print(bcolors.BOLD + end_file_dir + bcolors.ENDC)

    else:
        print(bcolors.FAIL + "Download failed. Please download magisk manually!" + bcolors.ENDC)