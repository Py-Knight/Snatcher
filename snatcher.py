
'''Download videos from youtube.'''
# Author: Stephen J Smith.
# pyknight.com
# 2021.
# To install youtube-dl visit https://youtube-dl.org/
# To upgrade. pip3 install --upgrade youtube-dl

# HOW TO USE THIS SCRIPT.
# 1st: Edit 'path' to a directory on your system.
# 2nd: Cd into the directory where this script is located.
# 3rd: Run the following command  python3 snatcher.py


import os

# location to store download.
path = '/ENTER/YOUR/DIRECTORY/HERE'

# cd into the above directory.
os.chdir(path)

# confirm your in the correct directory.
print(os.getcwd()) 

# copy and paste the share link from youtube. 
playList = input('Enter playlist: ')

# retrieve a list of available downloads.
os.system('youtube-dl -F ' + (playList))

# select the video quality.
number = input('Enter number: ')

# download.
os.system('youtube-dl -f ' + (number) + ' ' + (playList))

