import os
import requests
def windows_updater():
    time.sleep(1)
    print("Getting url")
    url = "https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe"
    requested = request.get(url)
    contents = request.content
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
    os.chdir("instaInstaller")
    os.system("move ak_installer.py"+' '+cwd)
    print("Updated")

windows_updater()
