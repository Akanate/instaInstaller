#!/bin/bash
echo "Starting complete update"
cd "$(dirname "$0")"
rm -r instaInstaller
rm -r instaInstaller-master
echo "Ignore any errors where the directory may have not been deleted"
git clone https://github.com/WHYSOEASY/instaInstaller.git
echo "Got update"
echo "Appliying update"
cd ..
echo "Done if you see nothing in your directory it is fine just do cd .. and check again."
exit


