#!/bin/bash 
mkdir /root/update_files
cd /root
echo "Making directory for store"
cd update_files
echo "Moving to directory which was created"
git clone https://github.com/WHYSOEASY/instaInstaller.git
cd instaInstaller
echo "Moving to repository directory"   
echo "Updated"
cd ..
cd ..
mv /root/update_files/instaInstaller/ak_installer.py "$(dirname "$0")"
mv /root/update_files/instaInstaller/list.txt
rm -r update_files
echo "Cleaning up"
echo "Update complete"

