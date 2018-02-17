# Reddit Post Scheduler
##### by Luke Rindels
***
This is a tool to delay Reddit posts. URLs and Text posts can be submitted to any subreddit or profile at any time. It is intended to be run on an always running Raspberry Pi, but can also be set to run in the background of whatever system you're using. 

## Getting Started
___
#### PRAW
The Python Reddit API Wrapper (PRAW) is required to use the scripts, documentation can be found [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html "PRAW | Getting Started"). Once you create an app in your Reddit account settings, you can fill in the required fields in praw.ini. You will need to know the client id, client secret, username, and password of your reddit app along with creating a user agent. I recommend following praw's guidelines. For example:
```
user_agent='android:com.bot.scheduler:v1.0.3 (by /u/myusername)'
```
#### Setting Up The Scheduler
Make sure that you have installed all of the modules necessary for scheduler.py to run. Prawcore and praw were the ones that I had to install.
```
pip3 install praw
```
Replace the reddit instance name with whatever configuration name you have in praw.ini (you can leave it as the default 'bot1' if you didn't change it in praw.ini). Now is a good time to test and make sure that the program is working. Save and try running scheduler.py. Make sure that the praw.ini file is in the same directory. If it works, great! If not, check the error message and make sure that all modules have been imported and that your praw credentials don't have any typos.
#### Setting Up The Raspberry Pi
I SSH into my Raspberry Pi from my Windows machine and have it setup to run the script everytime I login. This way I don't have to worry about leaving my PC on when I have a post scheduled for days later. To do this, turn on SSH on the Pi, connect it to WiFi (or Ethernet), and make sure to change the default password. Once that's done, upload the files to the Pi however you would like. You need to upload .bash_login, login.sh, praw.ini, and scheduler.py. I used PSFTP to upload my directory:
```
open pi@10.0.0.xxx
put -r C:\PathnameToDirectory
```
In case you want to run other Reddit scripts or just don't want to worry about the praw.ini file, you can place it in the `~/.config/` directory. Place .bash_login in your home directory as well, if you already have a file by that name, just copy the following line into that file, you may need to adjust the pathname if you have your shell script in another location:
```
/home/pi/redditbot/login.sh
```
Again, you may need to adjust the path in login.sh to make sure that it points to scheduler.py. Make sure that all of your bash scripts are set to executable:
```
chmod 755 login.sh
```
login.sh uses tmux to ensure that the process stays running (and on schedule) even when your SSH session ends. When you log back on, you will see schedule information if the post is still waiting to be submitted or you will see the fresh script if the post was already submit. To test it, reboot it and SSH back in.
```
sudo reboot
```
Everything should be working now! If not, head on down to the Troubleshooting section.

## Troubleshooting 
___
##### Issues with scheduler.py:
* Make sure that your praw.ini credentials are entered correctly
* Try placing the praw.ini file in the same directory as scheduler.py
* See if you have enough Reddit Karma to post without ID verification
##### Issues with running on login:
* Make sure all scripts are executable (`chmod 755 name.ext`)
* Verify that pathnames are correct
* Try running the script regularly and see if it throws an error
##### Other issues:
* Do you have tmux, python3, and all of the python modules installed? To install, `sudo apt-get install tmux`
* Have you tried turning everything off and back on again?
* If none of the above work, email me at lukerindels983@gmail.com and I'll try to help
