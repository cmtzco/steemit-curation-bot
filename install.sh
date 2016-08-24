#! /bin/bash 
wget -O assets/Anaconda3-4.1.1-Linux-x86_64.sh https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh
bash assets/Anaconda3-4.1.1-Linux-x86_64.sh
sudo apt-get install python3-pip
pip3 install virtualenv
virtualenv -p python3 upvotebot
source upvotebot/bin/activate
pip3 install -r requirements.txt

