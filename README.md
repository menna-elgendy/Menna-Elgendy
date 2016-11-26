#How to run the file 
#The final project file is called FinalCheckersProject.py. There are extra 4 image files that have to be downloaded. 
#1) PLAYER.gif 2) EXIT.gif 3)PLAYERS.gif 4)Mainmenu.gif
#The path for the 4 images will have to be modfied for the main menu to show up -Lines 922 to 925-.
#Libraries used were Tkinter and pygame.

#Some Rules:
#Red always starts first and that is why the gameboard starts up with all red pieces highlighted
#In 1 Player, you are only allowed to be red, and you always start first
#In 2 players, you can make as many jumps as you want as long as they are all valid
#In 1 Player; however, you can make a maximum of 2 jumps, as that is the maximum jumps the computer is programmed to make
#King pieces will have a smaller black circle inside the original piece and they can move forwards and backwards

#Winning conditions assumed
#1) The obvious one, no pieces left for that player
#2) If one piece is left for one player and the other has three pieces or more left, the one with the three pieces or more wins
   as it might take so long to just try to excape and in the end its most likely that this piece will be removed
#3) If all pieces of one player are stuck and he has no valid moves, the other player wins

#In case of winning a message shows up for three seconds saying who won and then the game quits

 
