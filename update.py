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

def git_install():
    cwd = os.getcwd()
    os.mkdir("update files")
    print("Making directory for store")
    os.chdir("update files")
    os.system("git clone https://github.com/WHYSOEASY/instaInstaller.git")
    os.chdir("instaInstaller")
    print("Changing directory")
    os.system("move ak_installer.py"+' '+cwd)
    os.system("move list.txt"+' '+cwd)
    os.chdir(cwd)
    os.system("rmdir update files /s /q")
    print("Done")
    exit()

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
    os.chdir("instaInstaller")
    os.system("move ak_installer.py"+' '+cwd)
    os.system("move list.txt"+' '+cwd)
    os.chdir(cwd)
    os.system("rmdir update files /s /q")
    print("Updated")
    
    
choice()
