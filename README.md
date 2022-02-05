# python_adb

## Disclaimer
This program/script is still in progress. You can test it out, modify it or start a pull-request.

Right now *Linux only*. <br> <br>
Tested on following OS:
   - Linux mint Cinnamon & Xfce
   - Raspberry Pi OS on Raspberry Pi 3 and 4
   - Ubuntu

Already tested on following devices:
<br>
- Xiaomi Mi 10T Lite 5G <br>
 (Android 11.0)

    [Link to device info](https://www.devicespecifications.com/en/model/28d4549c)

- Samsung Galaxy S7 Exynos <br>
 (Android 8.0)

    [Link to device info](https://www.devicespecifications.com/de/model/63063a47)

- Gigaset GS370 Plus <br>
 (Android 8.1.0)

    [Link to device info](https://www.devicespecifications.com/en/model/bdd9488c)


## Goals:
1. Implement some of those functions in a GUI
2. Add some of those functions in own modules
...

## Preparation on your Computer: 

1.  Install python if you havent already (at least Python 3.6) <br>
```bash
sudo apt-get install python3
```

<br>

2.  Then you need to install python pip  <br>
```bash
sudo apt-get install python3-pip
```
<br>

3. After this run:  <br>
```bash
sudo apt-get update && sudo apt-get upgrade
```
<br>    

4. Then install pure python:  <br>
```bash
pip3 install -U pure-python-adb
```
<br>  


5. Make sure you have adb installed  <br>
```bash
whereis adb
```
<br>

If there is no adb folder, do: <br>
```bash
sudo apt install adb
```
<br> 

## Preparation on your device

 ### Enable developer options
    1. Enter your phone settings
    2. Find phone info settings
    3. Find build number (on some devices its located under "software informations") and press ~5 times on "build number"
    4. Now you have developer options enabled. You will find this option now in your settings.
 ### Enable usb-debugging
    1. Enter developer options
    2. Enable usb-debugging
    (3.) On some devices you also need to activate "Installation over usb"

<br>

## How to run adb_python script:

1. Clone git repo to your computer.
```bash
git clone https://github.com/Frxhb/python_adb.git
```
<br>

3. Change diretory to ./python_adb
```bash
cd ./python_adb
```
<br>

4. Give python_adb.py permissions
```bash
chmod 777 python_adb.py
```
<br>

5. Run Python Program
```bash
python3 python_adb.py
```