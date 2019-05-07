#!/bin/bash
echo "Removing old files"
cd "$(dirname "$0")"
rm -r ak_installer.py
rm -r list.txt
mkdir update_files
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
echo "Put new files in"
echo "Cleaning up"
echo "Update complete"

