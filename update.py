import os
import requests
import shutil
import time
def choice():
    choose = input("Do you have git hub terminal: ")
    if choose == "yes":
        git_install()
    elif choose == "no":
        windows_updater()
    else:
        print("Invalid option")
        choice()


def windows_updater():
    time.sleep(1)
    print("Getting url")
    url = "https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe"
    requested = requests.get(url)
    contents = requested.content
    time.sleep(1)
    print("Downloading git into file")
    cwd = os.getcwd()
    os.chdir(cwd)
    os.mkdir("update files")
    os.chdir("update files")
    f = open("git.exe","wb")
    f.write(contents)
    f.close()
    print("Put contents into file")
    os.system("git.exe")
    print("Downloaded")
    print("Getting updated")
    os.system("git clone https://github.com/WHYSOEASY/instaInstaller.git")
    current = os.getcwd()
    os.chdir("update files")
    os.chdir("instaInstaller-master")
    os.system("move ak_installer.py"+' '+cwd)
    os.system("move list.txt"+' '+cwd)
    os.chdir(cwd)
    shutil.rmtree("update files")
    print("Updated")
    
    

windows_updater()
