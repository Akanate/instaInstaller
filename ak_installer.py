import os
import requests
import time
import zipfile
import sys
def notepad_plus():
    try:
        url = "https://notepad-plus-plus.org/repository/7.x/7.6.6/npp.7.6.6.Installer.exe"
        get = requests.get(url)
        print("Getting url....")
        contents = get.content
        print("Getting url...Done")
        time.sleep(1)
        print("Opening file...")
        time.sleep(1)
        f = open("notepad++.exe", "wb")
        print("Opening file...Done")
        time.sleep(1)
        print("Writing file...")
        f.write(contents)
        time.sleep(1)
        print("Writing file...Done")
        time.sleep(1)
        print("Closing file...")
        f.close()
        print("Closing file...Done")
        time.sleep(1)
        cwd = os.getcwd()
        print("Changing to current directory...")
        time.sleep(1)
        os.chdir(cwd)
        print("Changing directory...Done")
        time.sleep(1)
        print("Starting installation...")
        os.system("notepad++.exe")
        print("Beginning installation")
    except OSError as e:
        print(e)
        print("Something went wrong")
        exit()


def sublime():
    try:
        url = "https://download.sublimetext.com/Sublime%20Text%20Build%203207%20Setup.exe"
        print("Getting url...")
        requester = requests.get(url)
        contents = request.content
        print("Getting the url...Done")
        time.sleep(1)
        print("Opening file...")
        time.sleep(1)
        f = open("sublime.exe", "wb")
        print("Opening file...Done")
        time.sleep(1)
        print("Writing into file...")
        f.write(contents)
        print("Writing into file...Done")
        time.sleep(1)
        print("Closing file...")
        f.close()
        print("Closing file...Done")
        time.sleep(1)
        print("Getting current directory...")
        cwd = os.getcwd()
        print("Getting current directory...Done")
        os.chdir(cwd)
        print("Initialzing installation...Done")
        time.sleep(1)
        os.system("sublime.exe")
        print("Install menu")
        time.sleep(30)
        exit()
    except OSError as e:
        print("Something went wrong exitting")
        print(e)
        exit()


def python3():
    try:
        url = "https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe"
        print("Getting url...")
        requested = requests.get(url)
        contents = requested.content
        print("Getting url...Done")
        time.sleep(1)
        print("Opening file...")
        time.sleep(1)
        f = open("python3.exe", "wb")
        time.sleep(1)
        print("Opening file...")
        time.sleep(1)
        print("Opening file...Done")
        time.sleep(1)
        print("Writing contents...")
        f.write(contents)
        print("Writing contents...Done")
        time.sleep(1)
        print("Closing...")
        f.close()
        time.sleep(1)
        print("Closing...Done")
        time.sleep(1)
        print("Getting current directory...")
        cwd = os.getcwd()
        print("Getting current directory...Done")
        os.chdir(cwd)
        print("Initalizing installation...")
        time.sleep(1)
        print("Initialzing installation...Done")
        os.system("python3.exe")
        print("Install menu done")
        time.sleep(30)
        exit()
    except OSError as e:
        print(e)
        print("Something went wrong exitting")
        exit()


def python2():
    try:
        url = "https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi"
        print("Getting url...")
        requested = requests.get(url)
        contents = requested.content
        print("Getting url...Done")
        time.sleep(1)
        print("Opening file...")
        time.sleep(1)
        f = open("python_2.msi", "wb")
        print("Opening file...Done")
        time.sleep(1)
        print("Writing contents...")
        f.write(contents)
        time.sleep(1)
        print("Writing contents...Done")
        time.sleep(1)
        print("Closing file...")
        f.close()
        time.sleep(1)
        cwd = os.getcwd()
        time.sleep(1)
        print("Closing file...Done")
        os.chdir(cwd)
        time.sleep(1)
        print("Initializing")
        os.system("python2.msi")
        print("Initializing...Done")
        time.sleep(30)
        exit()
    except OSError as e:
        print(e)
        print("Something went wrong exitting")
        exit()

def python2L():
    try:
        url = "https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz"
        print("Getting url...")
        requested = requests.get(url)
        contents = requested.content
        print("Getting url...Done")
        time.sleep(1)
        print("Creating file...")
        f = open("python2.tgz","wb")
        print("Creating file...Done")
        time.sleep(1)
        print("Writing contents...")
        time.sleep(1)
        f.write(contents)
        print("Writing contents...Done")
        time.sleep(1)
        print("Closing file...")
        f.close()
        time.sleep(1)
        print("Closing file...Done")
        cwd = os.getcwd()
        os.chdir(cwd)
        os.system("mv python2.tgz /opt/python2.tgz")
        print("Moving file to optional area")
        time.sleep(1)
        os.chdir("/opt")
        print("Untarring file")
        time.sleep(1)
        os.system("tar xvf python2.tgz")
        print("Untared")
        os.chdir("Python-2.7.16")
        os.system("chmod +x configure")
        print("Configuring")
        time.sleep(1)
        os.system("./configure")
        print("Initializing")
        time.sleep(30)
        exit()
    except OSError as e:
        print("Something went wrong")
        print(e)
        exit()


def python3L():
    try:
        url = "https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc1.tgz"
        requested = requests.get(url)
        print("Getting url this may take a second")
        contents = requested.content
        print("Got url")
        f = open("python3_linux.tgz", "wb")
        print("Creating file for store")
        time.sleep(1)
        f.write(contents)
        f.close()
        os.mkdir("/opt/python3")
        print("Made a directory for python3..")
        os.system("mv python3_linux.tgz /opt/python3")
        print("Moving file")
        time.sleep(1)
        os.chdir("/opt/python3")
        print("Untarring...")
        time.sleep(1)
        os.system("tar xvf python3_linux.tgz")
        print("Untared...")
        os.chdir("/opt/python3/Python-3.7.1rc1")
        os.system("chmod +x configure")
        os.system("./configure")
        print("Done")
        time.sleep(30)
        exit()
    except OSError:
        print("Something went wrong initializing")
        exit()



def Pycharm():
    try:
        url = "https://download-cf.jetbrains.com/python/pycharm-community-2019.1.1.exe"
        requested = requests.get(url)
        print("Getting url this may take a second....")
        contents = requested.content
        print("Got url...")
        time.sleep(2)
        f = open("pycharm.exe","wb")
        print("Saving file")
        time.sleep(1)
        f.write(contents)
        print("Saved contents")
        time.sleep(1)
        f.close()
        print("Closed file")
        time.sleep(1)
        cwd = os.getcwd()
        os.chdir(cwd)
        os.system("pycharm.exe")
        print("Initializing.....")
        time.sleep(30)
        exit()
    except OSError as e:
        print("Something went wrong")
        print(e)
        exit()

def PycharmL():
    try:
        url = "https://download-cf.jetbrains.com/python/pycharm-community-2019.1.1.tar.gz"
        print("Checking url")
        requested = requests.get(url)
        time.sleep(1)
        print("Getting url")
        contents = requested.content
        print("Got url")
        f = open("pycharm.tar.gz","wb")
        time.sleep(1)
        print("Writing into file")
        f.write(contents)
        f.close()
        time.sleep(1)
        print("Closing file")
        cwd = os.getcwd()
        os.chdir(cwd)
        time.sleep(1)
        print("Changed to current directory")
        time.sleep(1)
        os.system("mv pycharm.tar.gz /opt")
        time.sleep(1)
        print("Moved file to /opt")
        os.chdir("/opt")
        time.sleep(1)
        print("Changed directory to /opt")
        time.sleep(1)
        print("Starting untarring process")
        os.system("tar xvf pycharm.tar.gz")
        time.sleep(1)
        print("Untarred")
        time.sleep(1)
        print("Changing to pycharm directory")
        os.chdir("/opt/pycharm-community-2019.1.1")
        time.sleep(1)
        print("Changed directory")
        time.sleep(1)
        print("Changing to bin")
        os.chdir("/opt/pycharm-community-2019.1.1/bin")
        time.sleep(1)
        print("Making sure jdk is installed or pycharm won't work")
        time.sleep(1)
        os.system("apt-get install default-jdk")
        time.sleep(1)
        print("Starting install")
        os.system("chmod +x pycharm.sh")
        os.system("./pycharm.sh")
        print("Installing")        
        time.sleep(30)
        exit()
    except OSError as e:
        print("Something went wrong")
        print(e)
        exit()

def atom():
     try:
        print("Looking for url")
        url = "https://atom-installer.github.com/v1.36.1/atom-amd64.deb?s=1556217353&ext=.deb"
        requested = requests.get(url)
        time.sleep(1)
        print("Getting url")
        contents = requested.content
        time.sleep(1)
        print("Got url")
        time.sleep(1)
        print("Opening file")
        f = open("atom.deb","wb")
        f.write(contents)
        time.sleep(1)
        print("Wrote to file")
        f.close()
        time.sleep(1)
        print("Closed file")
        cwd = os.getcwd()
        os.chdir(cwd)
        time.sleep(1)
        print("Moving file")
        os.system("mv atom.deb /opt")
        time.sleep(1)
        print("Moved file to /opt")
        os.system("sudo dpkg -i /opt/atom.deb")
        time.sleep(1)
        print("Dpkg done")
        time.sleep(30)
        exit()
     except OSError as e:
        print("Something went wrong")
        print(e)
        exit()







def initialize(choose):
    if choose == "get notepad++ windows":
        notepad_plus()
    elif choose == "get sublime windows":
        sublime()
    elif choose == "get python3 windows":
        python3()
    elif choose == "get python2 windows":
        python2()
    elif choose == "get python3 linux":
        python3L()
    elif choose == "get python2 linux":
        python2L()
    elif choose == "get pycharm windows":
        Pycharm()
    elif choose == "get pycharm linux":
        PycharmL()
    elif choose == "get atom linux":
        atom()
    elif choose == "list":
        f = open("list.txt","r")
        contents = f.read()
        print("This list you have")
        print(contents)
        f.close()
        exit()
    elif choose == "update":
        update()
    else:
        print("""Uses
              get - Will get the program you are asking for and then put your os
              Eg get notepad++ windows
              Remember ths is in beta stages so has limited amount of options
              list-Will show you all the programs you can install at the moment
              """)
choice = ' '.join(sys.argv[1:])
initialize(choice)
