#!/bin/bash
echo "Removing old files"
cd "$(dirname "$0")"
cd ..
rm -r instaInstaller
echo "Moving to directory which was created"
git clone https://github.com/WHYSOEASY/instaInstaller.git
cd instaInstaller
echo "Update complete"

