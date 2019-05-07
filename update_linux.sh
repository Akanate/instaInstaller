#!/bin/bash 
mkdir update_files
echo $PWD
echo "Making directory for store"
cd update_files
echo "Moving to directory which was created"
git clone https://github.com/WHYSOEASY/instaInstaller.git
cd instaInstaller
echo "Moving to repository directory"   
echo "Updated"
mv ak_installer.py "$(dirname "$0")"
mv list.txt "$(dirname "$0")"
rm -r update_files
echo "Cleaning up"
echo "Update complete"

