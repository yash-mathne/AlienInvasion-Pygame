# AlienInvasion-Pygame

 This is a pygame based shooter game based on a popular arcade game built using python3.

# Getting Started : Prerequisites-

Ubuntu-
For Python3:
1. Open terminal via Ctrl+Alt+T or searching for “Terminal” from app launcher. When it opens, run command to add the PPA:

sudo add-apt-repository ppa:jonathonf/python-3.6

2. Then check updates and install Python 3.6 via commands:

sudo apt-get update
sudo apt-get install python3.6

For Pygame :

sudo apt-get install python3-setuptools
sudo easy_install3 pip
sudo pip3.5 install pygame

# GamePlay:

Run the game by typing this in the terminal:

python3 alieninvasion.py

# Game Rules:

A new alien spawns on the top of the screen every five seconds and self destructs after 4 seconds. Your objective is to hit these aliens with missiles and increase your score.

You can move the spaceship right and left on the bottom of the screen using A to move left and D to move right.

There are two types of missiles that you can fire - a primary killer missile by pressing the SPACE_BAR and a secondary low damage missile by pressing S, which moves twice as fast as the primary missile.

The primary missile immediately kills the alien and increases your score by one.

After a secondary missile hit, alien suffers partial damage and hence survives for only 2 seconds after that. Note that this does not contribute to the score.

Press Q if you want to exit the game.

# Coding Principles-

Code is modular and OOP concepts are followed.
Code is PEP8 compliant to considerable extent.

# Inspiration-

Space Invaders​ is a classic arcade video game created by Tomohiro Nishikado and released in 1978 - the port of which was also responsible for the massive popularity of gaming consoles in the 80s - and hence played a major role in pushing the gaming industry towards mainstream media.
