#!/bin/bash
echo "Removing old files"
cd "$(dirname "$0")"
rm -r ak_installer.py
rm -r list.txt
rm -r README.md
rm -r update.py
rm -r update_linux.sh
echo "Moving to directory which was created"
git clone https://github.com/WHYSOEASY/instaInstaller.git
cd instaInstaller
echo "Moving to repository directory"   
echo "Updated"
rm -r update_files
echo "Put new files in"
echo "Cleaning up"
echo "Update complete"

