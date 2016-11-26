import pygame
import Tkinter as tk

#A function that destroys the window when exit button is pressed and
#then changes condition to call multiplayer or single player
def deleteWnd():
    wnd.destroy()

#A function that destroys the window when 1 player button is pressed
#and then changes condition to False to call onePlayer function
def deleteWnd1():
    global condition
    wnd.destroy()
    condition=False

#A function that destroys the window when 2 players button is pressed
#and then changes condition to True to call twoPlayer function
def deleteWnd2():
    global condition
    condition=True
    wnd.destroy()

#A function that sets up the gameboard
def gameboard():
    global gameDisplay,red,beige,black,brown,neonY,redP,beigeP
    #initializing start positions of x and y coordinates
    y=-100
    x=50
    gameDisplay.fill(brown)  #setting background color
    #A for loop that repeats four times to create the eight rows
    #of the gameboard as it consists of 2 nested for loop
    for j in range(4):
        #incrementing y and reseting x everytime loop repeats
        y=y+100
        x=50
        #A nested for loop that draws the black squares and the pieces in odd rows
        #Adds all red pieces in one list and all beige pieces in another
        for i in range (4):
            pygame.draw.rect(gameDisplay,black,[x,y,50,50]) #drawing black squares
            if j==0 or j==1:
                redP.append([x,y]) #appending position of red pieces to a list
                pygame.draw.circle(gameDisplay,red,(x+25,y+25),20) #drawing red pieces on top of black squares
                
            elif j==3:
                beigeP.append([x,y]) #appending position of beige pieces to a list
                pygame.draw.circle(gameDisplay,beige,(x+25,y+25),20) #drawing beige pieces on top of black squares
            x=x+100
        #reseting x to zero    
        x=0
        #A nested for loop that draws the black squares and the pieces in even rows
        #Adds all red pieces in one list and all beige pieces in another
        for i in range (4):
            pygame.draw.rect(gameDisplay,black,[x,y+50,50,50])  #drawing black squares
            if j==0:
                redP.append([x,y+50])  #appending position of red pieces to a list
                pygame.draw.circle(gameDisplay,red,(x+25,y+75),20) #drawing red pieces on top of black squares
            elif j==2 or j==3:
                if j==2:
                    beigeP.append([x,y+50]) #appending position of beige pieces to a list
                elif j==3:
                    beigeP.append([x,y+50])  #appending position of beige pieces to a list
                pygame.draw.circle(gameDisplay,beige,(x+25,y+75),20) #drawing beige pieces on top of black squares
            x=x+100
        #As red always starts, it highlights all red pieces with yellow outline at the start of the game
        for i in range (len(redP)):
            pygame.draw.rect(gameDisplay,neonY,[redP[i][0],redP[i][1],50,50],2)

#A function that takes current position and were mouse was clicked as input
#then it creates crowned pieces when one player's piece reaches the opponents' side
#It appends the crowned pieces in a different list
#This function also checks if piece moved was crowned or not and appends the applicable list accordingly 
def crowned(current,move):
    global gameDisplay, redP,redC, beigeC, beigeP, player, black
    xMove=move[0] #x coordinate of position were player clicked
    yMove=move[1] #y coordinate of position were player clicked
    if (player==0):
        if (yMove==350) or (current in redC): #checks if red reached beige side or if piece was crowned already
            pygame.draw.circle(gameDisplay,black,(xMove+25,yMove+25),15,5) #drawing another circle on top of original if piece got crowned
            redC.append([xMove,yMove]) #adding crowned piece to a different list or changing its position if already there
        if (yMove != 350) and (current not in redC): #checks if piece is not crowned
            redP.append([xMove,yMove]) #appending it to normal pieces list
        if current in redP: 
            redP.remove(current) #removing initial piece position from list
        if current in redC:
            redC.remove(current)#removing initial piece position from list
    if (player==1):
        if (yMove==0) or (current in beigeC):#checks if beige reached red side or if piece was crowned already
            pygame.draw.circle(gameDisplay,black,(xMove+25,yMove+25),15,5)#drawing another circle on top of original if piece got crowned
            beigeC.append([xMove,yMove]) #adding crowned piece to a different list or changing its position if already there
        if (yMove !=0) and (current not in beigeC): #checks if piece is not crowned
            beigeP.append([xMove,yMove])#appending it to normal pieces list
        if current in beigeP:
            beigeP.remove(current)#removing initial piece position from list
        if current in beigeC:
            beigeC.remove(current) #removing initial piece position from list

#A function that takes the current position of a piece and the mouse position as inputs
#it then goes through several valid condition and returns true if it meets any of them
def isValid(current,move):
    global redP,beigeP,redC,beigeC,player,s0, s1, firstMove, notCross, gameDisplay, black

    #player 0 validity check
    if (s1==1) and (player==0) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #moving one space diagonally forward if no piece was at mouse click
        if move[1]==current[1]+50:
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0            #reseting state 1 to zero, which indicates that no more mouse selections can be done
                notCross=True   #indicates that first move was not a jump, so it prevents multiple jumps
                return True
        #moving one space diagonally backward iif piece was crowned and if no piece was at mouse click  
        if (current in redC) and (move[1]==current[1]-50):
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0            #reseting state 1 to zero, which indicates that no more mouse selections can be done
                notCross=True   #indicates that first move was not a jump, so it prevents multiple jumps
                return True
    if (player==0) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #making a jump forward if there was a beige piece followed by an empty space, where mouse was clicked
        if move[1]==current[1]+100:
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50]) #removing beige piece that red jumped over from board
                beigeP.remove([current[0]+50,current[1]+50])                            #removing beige piece that red jumped over from list
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50])  #removing beige piece that red jumped over from board
                beigeC.remove([current[0]+50,current[1]+50])                             #removing beige piece that red jumped over from list
                return True                                  
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])  #removing beige piece that red jumped over from board
                beigeP.remove([current[0]-50,current[1]+50])                             #removing beige piece that red jumped over from list
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])  #removing beige piece that red jumped over from board
                beigeC.remove([current[0]-50,current[1]+50])                             #removing beige piece that red jumped over from list
                return True
        #making a jump backward if piece was crowned and if there was a beige piece followed by an empty space, where mouse was clicked
        if (current in redC) and (move[1]==current[1]-100):
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing beige piece that red jumped over from board
                beigeP.remove([current[0]+50,current[1]-50])                            #removing beige piece that red jumped over from list
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing beige piece that red jumped over from board
                beigeC.remove([current[0]+50,current[1]-50])                            #removing beige piece that red jumped over from list
                return True                           
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing beige piece that red jumped over from board
                beigeP.remove([current[0]-50,current[1]-50])                            #removing beige piece that red jumped over from list
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing beige piece that red jumped over from board
                beigeC.remove([current[0]-50,current[1]-50])                            #removing beige piece that red jumped over from list
                return True

    #player 1 validity check       
    if (s1==1) and  (player==1) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #moving one space diagonally backward if no piece was at mouse click
        if move[1]==current[1]-50:
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0              #reseting state 1 to zero, which indicates that no more mouse selections can be done
                notCross=True     #indicates that first move was not a jump, so it prevents multiple jumps
                return True
        #moving one space diagonally forward if piece was crowned and if no piece was at mouse click 
        if (current in beigeC) and (move[1]==current[1]+50):
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0              #reseting state 1 to zero, which indicates that no more mouse selections can be done
                notCross=True     #indicates that first move was not a jump, so it prevents multiple jumps
                return True
    if (player==1) and  (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #making a jump backward if there was a beige red followed by an empty space, where mouse was clicked
        if move[1]==current[1]-100:
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
                redP.remove([current[0]+50,current[1]-50])                              #removing red piece that beige jumped over from list
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing red piece that red jumped over from board
                redC.remove([current[0]+50,current[1]-50])                              #removing red piece that beige jumped over from list
                return True 
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
                redP.remove([current[0]-50,current[1]-50])                              #removing red piece that beige jumped over from list
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
                redC.remove([current[0]-50,current[1]-50])                              #removing red piece that beige jumped over from list
                return True
        #making a jump forward if piece was crowned and if there was a red piece followed by an empty space, where mouse was clicked
        if (current in beigeC) and (move[1]==current[1]+100):
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
                redP.remove([current[0]+50,current[1]+50])                              #removing red piece that beige jumped over from list
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
                redC.remove([current[0]+50,current[1]+50])                              #removing red piece that beige jumped over from list
                return True 
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
                redP.remove([current[0]-50,current[1]+50])                              #removing red piece that beige jumped over from list
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
                redC.remove([current[0]-50,current[1]+50])                              #removing red piece that beige jumped over from list
                return True

#A function that takes the first mouse position as input and highlights the piece selected           
def mouseClicked(mx,my):
    global gameDisplay, redP,redC,beigeC, beigeP,neonY, neonG, player, s0, s1,current

    #loops that go through all lists of red and beige pieces and removes highlight from all pieces once mouse clikcked on one
    for i in range (len(beigeP)):
                pygame.draw.rect(gameDisplay,black,[beigeP[i][0],beigeP[i][1],50,50],2)
    for i in range (len(redP)):
                pygame.draw.rect(gameDisplay,black,[redP[i][0],redP[i][1],50,50],2)
    for i in range (len(redC)):
                pygame.draw.rect(gameDisplay,black,[redC[i][0],redC[i][1],50,50],2)
    for i in range (len(beigeC)):
                pygame.draw.rect(gameDisplay,black,[beigeC[i][0],beigeC[i][1],50,50],2)
    #Modifying the mouse position gotten from event loop to get equivalent x and y coordinates on board
    mx = mx/50
    my = my/50
    position = [mx*50,my*50]
    initialx=position[0]
    initialy=position[1]
    
    #Checking if there is a red piece in the position where the mouse
    #was first clicked if player was 0 and highlighting it if there was one
    if (player == 0) and ((position in redP) or (position in redC)):
        current=[initialx,initialy] #if piece was there, setting this as the current piece that needs to be moved
        s0 = 1                      #setting state 0 to one, that indicates that current piece was found 
        s1 = 1                      #setting state 1 to one, that indicates that first mouse click was valid  
        pygame.draw.rect(gameDisplay, neonY, [initialx,initialy,50,50], 2)
    #Checking if there is a beige piece in the position where the mouse
    #was first clicked if player was 1 and highlighting it if there was one
    elif (player == 1) and ((position in beigeP) or (position in beigeC)):
        current=[initialx,initialy] #if piece was there, setting this as the current piece that needs to be moved
        s0 = 1                      #setting state 0 to one, that indicates that current piece was found 
        s1 = 1                      #setting state 1 to one, that indicates that first mouse click was valid 
        pygame.draw.rect(gameDisplay, neonG, [initialx,initialy,50,50], 2)
                                                
#A function that takes the second mouse position as input and calls isValid to check if move was valid
#if it was it then deletes the piece and draws it in its new position
def mouseClick2(mx,my):
    global gameDisplay, redP,redC,beigeC, beigeP,neonY,twoPlayers,nJumps
    global neonG, player, s0, s1, current, firstMove, switch

    #Modifying the mouse position gotten from event loop to get equivalent x and y coordinates on board
    mx = mx/50
    my = my/50
    position = [mx*50,my*50]
    initialx=position[0]
    initialy=position[1]
    #conditions for player 0
    if (player==0):
        if isValid(current,[initialx,initialy]):
            firstMove=True                                                       #if move was valid, setting first move to true to indicate that one move has been made
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50])  #removing red piece from board at current position
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50],2)#removing highlight around the piece
            pygame.draw.circle(gameDisplay,red,(initialx+25,initialy+25),20)     #drawing a new red piece at valid move position clicked
            crowned(current,[initialx,initialy])                                 #calling crowned function to check if move makes piece crowned and to delete beige pieces jumped over
            current=[initialx,initialy]                                          #setting current position to where piece was moved to check if multiple jumps are possible
            switchPlayer(current)                                                #calling switch player function to check if there are still possible moves or player will be switched
            #if there were still possible jumps, highlight piece 
            if switch==False:
                pygame.draw.rect(gameDisplay, neonY, [current[0],current[1],50,50],2)
            #if AI was used, allows max of 2 jumps only
            if (switch==False) and (twoPlayers==False) and (nJumps<2):
                pygame.draw.rect(gameDisplay, neonY, [current[0],current[1],50,50],2)
                nJumps=nJumps+1
                
        #if first move was invalid it sets state 0 and state 1 to zero which indicate that current piece and mouse position are not applicable
        #which allows player to play again by selecting a new piece or a different position to move same piece where it will be valid
        if firstMove==False:
            s0=0
            s1=0
    #conditions for player 1       
    if (player==1):
        if isValid(current,[initialx,initialy]):
            firstMove=True                                                       #if move was valid, setting first move to true to indicate that one move has been made
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50])  #removing beige piece from board at current position
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50],2)#removing highlight around the piece
            pygame.draw.circle(gameDisplay,beige,(initialx+25,initialy+25),20)   #drawing a new beige piece at valid move position clicked
            crowned(current,[initialx,initialy])                                 #calling crowned function to check if move makes piece crowned and to delete red pieces jumped over
            current=[initialx,initialy]                                          #setting current position to where piece was moved to check if multiple jumps are possible
            switchPlayer(current)                                                #calling switch player function to check if there are still possible moves or player will be switched
            #if there were still possible jumps, highlight piece 
            if switch==False:
                pygame.draw.rect(gameDisplay, neonG, [current[0],current[1],50,50],2)

        #if first move was invalid it sets state 0 and state 1 to zero which indicate that current piece and mouse position are not applicable
        #which allows player to play again by selecting a new piece or a different position to move same piece where it will be valid      
        if firstMove==False:
            s0=0
            s1=0

#A function that is called by switchPlayer function if player will switch from 0 to 1
def switchCode0():
    global gameDisplay, beigeC, beigeP,neonY, neonG, player, s0, s1, firstMove, notCross, switch
    global Valid, Jump, twoPlayers,nJumps
    player=1         #setting player to 1 when player 0 has no more valid moves
    s0=0             #reseting state 0 to zero which allows for a new piece to be selected 
    s1=0             #reseting state 1 to zero which indicates that new mouse clicks can be made 
    nJumps=0         #reseting no of jumps made to zero unless next turn
    firstMove=False  #reseting no first move to False unless first move is made 
    notCross=False   #reseting no jump variable to zero
    switch=True      #setting switch to True which means one of the conditions was met
    Valid=[]         #emptying list of valid moves for next player
    Jump=False       #reseting jump variable to zero
    #when player is switched to player 1 two loops iterate over the pieces of beige player
    #crowned and uncorwned and highlights them to indicate its beige turn
    if twoPlayers==True:
        for i in range (len(beigeP)):
            pygame.draw.rect(gameDisplay,neonG,[beigeP[i][0],beigeP[i][1],50,50],2)
        for i in range (len(beigeC)):
          pygame.draw.rect(gameDisplay,neonG,[beigeC[i][0],beigeC[i][1],50,50],2)
          
#A function that is called by switchPlayer function if player will switch from 1 to 0      
def switchCode1():
    global gameDisplay, redP, redC,neonY, neonY, player, s0, s1, firstMove, notCross, switch
    global Valid, Jump
    player=0        #setting player to 0 when player 1 has no more valid moves
    s0=0            #reseting state 0 to zero which allows for a new piece to be selected 
    s1=0            #reseting state 1 to zero which indicates that new mouse clicks can be made 
    firstMove=False #reseting no first move to False unless first move is made
    notCross=False  #reseting no jump variable to zero
    switch=True     #setting switch to True which means one of the conditions was met
    Valid=[]        #emptying list of valid moves for next player
    Jump=False      #reseting jump variable to zero
    #when player is switched to player 0 two loops iterate over the pieces of red player
    #crowned and uncorwned and highlights them to indicate its red turn
    for i in range(len(redP)):
        pygame.draw.rect(gameDisplay,neonY,[redP[i][0],redP[i][1],50,50],2)
    for i in range (len(redC)):
        pygame.draw.rect(gameDisplay,neonY,[redC[i][0],redC[i][1],50,50],2)
    
#A function that takes move mad as input and is called after it is made to
#check ifthere are further possible moves, if not, it switches the player      
def switchPlayer(position):
    global gameDisplay, redP, beigeP,redC, beigeC, neonY, neonG, player, s0
    global switch, notCross, firstMove, black, s1,nJumps,twoPlayers
    all= redP + redC + beigeP + beigeC   #list of all pieces
    allRed =redP + redC                  #list of all red pieces
    allBeige =beigeP + beigeC            #list of all beige pieces
    x=position[0]                        #x position of move made kept in a variable
    y=position[1]                        #y position of move made kept in a variable
    switch=False                         #setting switch to False unless one of the conditions is met
    if (player==0):
        #if first move was made and it was not a jump, calls switch player
        if firstMove==True and notCross==True:
            switchCode0()
        #if piece is crowned call crowned switch function
        elif position in redC:
            switchPlayerCrown(position)
        else:
            #if there are no possible jumps calls switch player
            if ([x+50,y+50] not in allBeige) and ([x-50,y+50] not in allBeige):
                 switchCode0()        
            elif ([x+50,y+50] in allBeige) and ([x-50,y+50] not in allBeige):
                  if ([x+100,y+100] in all) or ((x+100)>350) or ((y+100)>350):
                     switchCode0()
            elif ([x-50,y+50] in allBeige) and ([x+50,y+50] not in allBeige):
                   if ([x-100,y+100] in all) or (x-100<0) or (y+100>350):
                     switchCode0()
            elif ([x-50,y+50] in allBeige) and ([x+50,y+50] in allBeige):
                if ([x+100,y+100] in all) or ((x+100)>350) or ((y+100)>350):
                    if ([x-100,y+100] in all) or (x-100<0) or (y+100>350):
                         switchCode0()
            #for AI only, switches after two jumps are made
            if (nJumps>=1) and (twoPlayers==False):     
                switchCode0()
            
    elif (player==1):
        #if first move was made and it was not a jump, calls switch player
        if firstMove==True and notCross==True:
             switchCode1()
        #if piece is crowned call crowned switch function
        elif position in beigeC:
            switchPlayerCrown(position)
        else:
            #if there are no possible jumps calls switch player
            if ([x+50,y-50] not in allRed) and ([x-50,y-50] not in allRed):
                 switchCode1()
            elif ([x+50,y-50] in allRed) and ([x-50,y-50] not in allRed):
                if ([x+100,y-100] in all) or (x+100>350) or (y-100<0):
                     switchCode1()      
            elif ([x-50,y-50] in allRed) and ([x+50,y-50] not in allRed):
                 if ([x-100,y-100] in all) or (x-100<0) or (y-100<0):
                     switchCode1()          
            elif  ([x-50,y-50] in allRed) and ([x+50,y-50] in allRed):
                if ([x+100,y-100] in all) or (x+100>350) or (y-100<0):
                    if ([x-100,y-100] in all) or (x-100<0) or (y-100<0):
                         switchCode1()
                         
def switchPlayerCrown(position):
    global gameDisplay, redP, beigeP,redC, beigeC, neonY, neonG, player, s0
    global switch, notCross, firstMove, black, s1,nJumps,twoPlayers
    all= redP + redC + beigeP + beigeC  #Adding all pieces in one list
    allRed =redP + redC                 #Adding all red pieces in a list
    allBeige =beigeP + beigeC           #Adding all beige pieces in a list
    x=position[0]                       #saving x position of move made in a variable
    y=position[1]                       #saving y position of move made in a variable
    switch=False                        #setting switch variable to False unless one of the conditions is met
    chance=False                        #setting chance variable to False unless a valid move was found
    if (player==0):
        #if no jumps can be made, switch player
        if ([x+50,y+50] not in allBeige) and ([x-50,y+50] not in allBeige):
            if ([x+50,y-50] not in allBeige) and ([x-50,y-50] not in allBeige):
                switchCode0()
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x+50,y+50] in allBeige):
              if ([x+100,y+100] not in all) and ((x+100)<=350) and ((y+100)<=350):
                  chance=True
                  nJumps=nJumps+1 #if one move is valid, no of jumps is incremented by 1 for AI
        #if a move can be made, chance is set to True which mean no switch yet
        if  ([x+50,y-50] in allBeige):
            if ([x+100,y-100] not in all) and ((x+100)<=350) and ((y-100)>=0):
                chance=True
                nJumps=nJumps+1 #if one move is valid, no of jumps is incremented by 1 for AI
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x-50,y+50] in allBeige):
            if ([x-100,y+100] not in all) and ((x-100)>=0) and ((y+100)<=350):
                chance=True
                nJumps=nJumps+1 #if one move is valid, no of jumps is incremented by 1 for AI
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x-50,y-50] in allBeige):
            if ([x-100,y-100] not in all) and ((x-100)>=0) and ((y-100)>=0):
                chance=True
                nJumps=nJumps+1 #if one move is valid, no of jumps is incremented by 1 for AI
        #if chance is equal to False (no valid move was found) calls switch player
        if chance==False:
            switchCode0()
        #for AI only, switch player after 2 jumps max
        if twoPlayers==False and nJumps>=2 :
            switchCode0() 
    elif (player==1):
        #if no jumps can be made, switch player
        if ([x+50,y+50] not in allRed) and ([x-50,y+50] not in allRed):
            if ([x+50,y-50] not in allRed) and ([x-50,y-50] not in allRed):
                switchCode1()
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x+50,y+50] in allRed):
            if ([x+100,y+100] not in all) and ((x+100)<=350) and ((y+100)<=350):
                chance=True
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x+50,y-50] in allRed):
            if ([x+100,y-100] not in all) and ((x+100)<=350) and ((y-100)>=0):
                chance=True
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x-50,y+50] in allRed):
            if ([x-100,y+100] not in all) and ((x-100)>=0) and ((y+100)<=350):
                chance=True
        #if a move can be made, chance is set to True which mean no switch yet
        if ([x-50,y-50] in allRed):
            if ([x-100,y-100] not in all) and ((x-100)>=0) and ((y-100)>=0):
                chance=True
        #if chance is equal to False (no valid move was found) calls switch player
        if chance==False:
            switchCode1()

#A function that is called after a move is made and it checks the board situation
#looking for a winning condition, it then displays a message and exits the game if a player won
def winning():
    global redP, beigeP,redC, beigeC
    allRed =redP + redC       #adding all red pieces in one list
    allBeige =beigeP + beigeC #adding all beige pieces in one list
    all= allRed + allBeige    #adding all pieces in one list
    f1=[]                     #A list that keeps all stuck uncrowned beige moves
    f2=[]                     #A list that keeps all stuck crowned beige moves
    f3=[]                     #A list that keeps all stuck uncrowned red moves
    f4=[]                     #A list that keeps all stuck crowned red moves
    closeWin1=False           #A variable that is set to true if all uncrowned beige pieces were stuck  
    closeWin2=False           #A variable that is set to true if all uncrowned red pieces were stuck 
    #if no red pieces are left, beige wins
    if len(redP) + len(redC)==0:
        display_box(gameDisplay,"WHITE WON!",beige,112)
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won
        pygame.quit()
        quit()
    #if no beige pieces are left, red wins
    if len(beigeP) + len(beigeC)==0:
        display_box(gameDisplay,"RED WON!",red,130)
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won
        pygame.quit()
        quit()
    
    #A for loop that iterates over uncrowned beige pieces and checks if they were stuck and had no possible moves
    for i in range (len(beigeP)):
        x=beigeP[i][0]
        y=beigeP[i][1]
        if ([x+50,y-50] in all) or ((x+50)>350) or ((y-50)<0):
            if ([x-50,y-50] in all) or ((x-50)<0) or ((y-50)<0):
                f1=f1+[1]
    #if number of stuck pieces is the same as number of beige pieces closeWin1 is set to True
    #and red doesnt win until crowned pieces are all stuck as well
    if len(f1)==len(beigeP):
        closeWin1=True
    #A for loop that iterates over crowned beige pieces and checks if they were stuck and had no possible moves
    for i in range (len(beigeC)):
        x=beigeC[i][0]
        y=beigeC[i][1]
        if ([x+50,y+50] in all) or ((x+50)>350) or ((y+50)>350):
            if ([x-50,y+50] in all) or ((x-50)<0) or ((y+50)>350):
                if ([x+50,y-50] in all) or ((x+50)>350) or ((y-50)<0):
                    if ([x-50,y-50] in all) or ((x-50)<0) or ((y-50)<0):
                        f2=f2+[1]
    #if number of stuck pieces is the same as number of crowned beige and closeWin1 is True
    #red wins as all beige pieces have no possible moves
    if len(f2)==len(beigeC) and closeWin1==True:
        display_box(gameDisplay,"RED WON!",red,130)
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won
        pygame.quit()
        quit()
    
    #A for loop that iterates over uncrowned red pieces and checks if they were stuck and had no possible moves
    for i in range (len(redP)):
        x=redP[i][0]
        y=redP[i][1]
        if ([x+50,y+50] in all) or ((x+50)>350) or ((y+50)>350):
            if ([x-50,y+50] in all) or ((x-50)<0) or ((y+50)>350):
                f3=f3+[1]
    #if number of stuck pieces is the same as number of red pieces closeWin2 is set to True
    #and beige doesnt win until crowned pieces are all stuck as well
    if len(f3)==len(redP):
        closeWin2=True
    #A for loop that iterates over crowned red pieces and checks if they were stuck and had no possible moves
    for i in range (len(redC)):
        x=redC[i][0]
        y=redC[i][1]
        if ([x+50,y+50] in all)or ((x+50)>350) or ((y+50)>350):
            if ([x-50,y+50] in all) or ((x-50)<0) or ((y+50)>350):
                if ([x+50,y-50] in all) or ((x+50)>350) or ((y-50)<0):
                    if ([x-50,y-50] in all) or ((x-50)<0) or ((y-50)<0):
                        f4=f4+[1]
    #if number of stuck pieces is the same as number of crowned red and closeWin2 is True
    #beige wins as all red pieces have no possible moves
    if len(f4)==len(redC) and closeWin2==True:
        display_box(gameDisplay,"WHITE WON!",beige,112)
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won 
        pygame.quit()
        quit()
    #if one piece left for red and three or more pieces are left for beige, beige wins
    if (len(allRed)==1) and (len(allBeige)>=3):
        display_box(gameDisplay,"WHITE WON!",beige,112) 
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won
        pygame.quit()
        quit()
    #if one piece left for beige and three or more pieces are left for red, red wins
    if (len(allBeige)==1) and (len(allRed)>=3):
        display_box(gameDisplay,"RED WON!",red,130)
        pygame.time.delay(3000) #waits three seconds after message is displayed before closing game
        #Quitting the game if a player won
        pygame.quit()
        quit()

    
#A function that takes the game board and a message to be displayed, the 
#color of player who won and x position of where text stats as inputs
#It is called by the winning function to display a message of who won
def display_box(screen, message,color,x):
  global black,red,beige
  #Print a message in a box in the middle of the screen
  fontobject = pygame.font.Font(None,40)
  pygame.draw.rect(screen, color,[100,150,200,100])
  pygame.draw.rect(screen, black,[100,150,200,100], 4)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, black),[x,185,200,100])
  pygame.display.flip()

#A function that takes current move and previous move as input and checks if there is a
#possibility of a single or double jump , if so it adds them to the list of valid moves
def makeJump(current,previous):
    global redP,beigeP,beigeC,redC,player,gameDisplay,Valid,AI,tempBeigeP,tempRedP,Jumped,tempBeigeC,tempRedC,tempRed,tempBeige
    all= tempRed + tempBeige
    Jumped=False   #Assuming jump is false until one of the jumping conditions are met
    #function is used when computer is playing only
    if player==1:   
        #AI is 0 it means its the player not computer, so it gets valid moves for red 
        if AI==0:
            #making a jump forward if there was a beige piece followed by an empty space
            if ([current[0]+100,current[1]+100] not in all) and (current[0]+100<=350) and (current[1]+100<=350) and ([current[0]+50,current[1]+50] in tempBeige):
                Valid+=[[[current[0]+100,current[1]+100],1]] #Appending valid jump to list and making count 1
                Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
            elif ([current[0]-100,current[1]+100] not in all) and (current[0]-100>=0) and (current[1]+100<=350) and ([current[0]-50,current[1]+50] in tempBeige):
                Valid+=[[[current[0]-100,current[1]+100],1]]    #Appending valid jump to list and making count 1
                Jumped=True                                     #Setting Jumped to true of conditions were met, indicating that a jump was made
            #making a jump backward if piece was crowned and there was a beige piece followed by an empty space
            if (current in tempRedC) or (previous in tempRedC):
                if ([current[0]+100,current[1]-100] not in all) and (current[0]+100<=350) and (current[1]-100>=0) and ([current[0]+50,current[1]-50] in tempBeige):
                    Valid+=[[[current[0]+100,current[1]-100],1]] #Appending valid jump to list and making count 1
                    Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
                elif ([current[0]-100,current[1]-100] not in all) and (current[0]-100>=0) and (current[1]-100>=0) and ([current[0]-50,current[1]-50] in tempBeige):
                    Valid+=[[[current[0]-100,current[1]-100],1]] #Appending valid jump to list and making count 1
                    Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
        #AI is 1 it means its the computer, so it gets valid moves for beige
        if AI==1:
            #making a jump backward if there was a red piece followed by an empty space 
            if ([current[0]+100,current[1]-100] not in all) and (current[0]+100<=350) and (current[1]-100>=0) and ([current[0]+50,current[1]-50] in tempRed): 
                Valid+=[[[current[0]+100,current[1]-100],1]] #Appending valid jump to list and making count 1
                Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
            elif ([current[0]-100,current[1]-100] not in all) and (current[0]-100>=0) and (current[1]-100>=0) and ([current[0]-50,current[1]-50] in tempRed):
                Valid+=[[[current[0]-100,current[1]-100],1]] #Appending valid jump to list and making count 1
                Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
            #making a jump forward if piece was crowned and if there was a red piece followed by an empty space
            if (current in tempBeigeC) or (previous in tempBeigeC):
                if ([current[0]+100,current[1]+100] not in all) and (current[0]+100<=350) and (current[1]+100<=350) and ([current[0]+50,current[1]+50] in tempRed):
                    Valid+=[[[current[0]+100,current[1]+100],1]] #Appending valid jump to list and making count 1
                    Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made
                elif ([current[0]-100,current[1]+100] not in all) and (current[0]-100>=0) and (current[1]+100<=350) and ([current[0]-50,current[1]+50] in tempRed):
                    Valid+=[[[current[0]-100,current[1]+100],1]] #Appending valid jump to list and making count 1
                    Jumped=True                                  #Setting Jumped to true of conditions were met, indicating that a jump was made

#A funtion that is called by AI only and takes the current position of a piece as an input and returns a list of all valid movements
def getValid(current):
    global redP,beigeP,beigeC,redC,player,gameDisplay,Valid,AI,tempBeigeP,tempRedP,Jumped,tempBeigeC,tempRedC,tempRed,tempBeige, doubleJump,allRed
    all= tempRed + tempBeige #Adding all pieces together in one list
    #function is used when computer is playing only 
    if player==1:
        #AI is 0 it means its the player not computer, so it gets valid moves for red 
        if AI==0: 
            makeJump(current,0)   #calling makeJump function to check if there's a possible jump, with no preivous condition 
            #A loop that iterates over the list of valid moves calling the makeJump function to check if double jumps are possible
            for i in range (len(Valid)):
                makeJump(Valid[i][0],current)
                if Jumped==True:
                    Valid[i+1][1]=2    #making the count 2 if a second jump can be made
            #moving one space diagonally forward
            if ([current[0]+50,current[1]+50] not in all) and (current[0]+50<=350) and (current[1]+50<=350): 
                Valid+=[[[current[0]+50,current[1]+50],0]] #Appending valid move to list and making count 0
            if ([current[0]-50,current[1]+50] not in all) and (current[0]-50>=0) and (current[1]+50<=350):
                 Valid+=[[[current[0]-50,current[1]+50],0]] #Appending valid move to list and making count 0
            #moving one space diagonally backward if crowned
            if current in tempRedC:
                if ([current[0]+50,current[1]-50] not in all) and (current[0]+50<=350) and (current[1]-50>=0):
                    Valid+=[[[current[0]+50,current[1]-50],0]] #Appending valid move to list and making count 0
                if ([current[0]-50,current[1]-50] not in all) and (current[0]-50>=0) and (current[1]-50>=0): 
                    Valid+=[[[current[0]-50,current[1]-50],0]] #Appending valid move to list and making count 0     
        #AI is 1 it means its the computer, so it gets valid moves for beige
        if AI==1:
            makeJump(current,0)   #calling makeJump function to check if there's a possible jump, with no privous condition 
            #A loop that iterates over the list of valid moves calling the makeJump function to check if double jumps are possible
            for i in range (len(Valid)):
                makeJump(Valid[i][0],current)
                if Jumped==True:
                    doubleJump=doubleJump+[[Valid[i],Valid[i+1]]] #A list of valid first jump and second jump to allow deleting red pieces in between
                    Valid[i+1][1]=2    #making the count 2 if a second jump can be made
            #moving one space diagonally backward
            if ([current[0]+50,current[1]-50] not in all) and (current[0]+50<=350) and (current[1]-50>=0):
                Valid+=[[[current[0]+50,current[1]-50],0]] #Appending valid move to list and making count 0
            if ([current[0]-50,current[1]-50] not in all) and (current[0]-50>=0) and (current[1]-50>=0): 
                Valid+=[[[current[0]-50,current[1]-50],0]] #Appending valid move to list and making count 0
            #moving one space diagonally forward if crowned
            if current in tempBeigeC:
                if ([current[0]+50,current[1]+50] not in all) and (current[0]+50<=350) and (current[1]+50<=350):
                    Valid+=[[[current[0]+50,current[1]+50],0]] #Appending valid move to list and making count 0
                if ([current[0]-50,current[1]+50] not in all) and (current[0]-50>=0) and (current[1]+50<=350):
                    Valid+=[[[current[0]-50,current[1]+50],0]] #Appending valid move to list and making count 0
    return Valid

#A function that takes initial position, current position and move
#as input and removes the red pieces that have been jumped over
def deletingRed(initial,current,move):
    global redP,redC,beigeC,gameDisplay
    #removing red pieces if jump made backward
    if move[1]==current[1]-100:
        if (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redP):
            pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
            redP.remove([current[0]+50,current[1]-50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redC):
            pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
            redC.remove([current[0]+50,current[1]-50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redP):
            pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
            redP.remove([current[0]-50,current[1]-50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redC):
            pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50]) #removing red piece that beige jumped over from board
            redC.remove([current[0]-50,current[1]-50])                              #removing red piece that beige jumped over from list
    #removing red pieces if piece was crowned and jump was made forward
    if ((current in beigeC) or (initial in beigeC)) and (move[1]==current[1]+100):
        if (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redP):
            pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
            redP.remove([current[0]+50,current[1]+50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redC):
            pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
            redC.remove([current[0]+50,current[1]+50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redP):
            pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
            redP.remove([current[0]-50,current[1]+50])                              #removing red piece that beige jumped over from list
        elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redC):
            pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50]) #removing red piece that beige jumped over from board
            redC.remove([current[0]-50,current[1]+50])                              #removing red piece that beige jumped over from list
    
#A function with the best counter moves for the first red move made
def bestFirstMoves():
    global redP,redC
    allRed=redP+redC
    #checks for first red move made and specifies the best counter moves accordingly
    if ([250,100] not in allRed) and ([200,150] in allRed):
        finalMove=[[100,250],[50,200]]
    if ([50,100] not in allRed) and ([100,150] in allRed):
         finalMove=[[100,250],[150,200]]
    if ([250,100] not in allRed) and ([300,150] in allRed):
        finalMove=[[200,250],[150,200]]
    if ([150,100] not in allRed) and ([200,150] in allRed):
        finalMove=[[0,250],[50,200]]
    if ([150,100] not in allRed) and ([100,150] in allRed):
        finalMove=[[300,250],[250,200]]
    if ([350,100] not in allRed) and ([300,150] in allRed):
        finalMove=[[300,250],[350,200]]
    if ([50,100] not in allRed) and ([0,150] in allRed):
        finalMove=[[100,250],[150,200]]
    return finalMove

#A function that is called when it is the computer's turn to get valid move and make it and then switch to other player
def AIMove():
    global redP,beigeP,beigeC,redC,player,s0, s1, firstMove, notCross, gameDisplay,tempBeigeC, firstMve, doubleJump
    global countR, countB, black,switch,Valid,oppValid,AI,tempBeigeP, tempRedP,tempRedC,tempRed, tempBeige
    allBeige=beigeP+beigeC          #A list of all beige pieces
    allRed=redP+redC                #A list of all red pieces
    tempRedP=redP[:]                #A copy of red pieces for temporary moves             
    tempRedC=redC[:]                #A copy of crowned red pieces for temporary moves
    tempRed=tempRedP+tempRedC       #A list of all temporary red pieces
    tempBeigeP=beigeP[:]            #A copy of beige pieces for temporary moves  
    tempBeigeC=beigeC[:]            #A copy of crowned beige pieces for temporary moves
    tempBeige=tempBeigeP+tempBeigeC #A list of all temporary beige pieces
    allMoves=[] #empty list to append all possible moves and there corresponding count 

    #calls function with best counter moves only for first move
    if firstMve==False:
        finalMove=bestFirstMoves()
        firstMve=True
    else:
        #A for loop that iteraties over all beige pieces and gets all possible valid moves for each piece
        for i in range(len(allBeige)):
            #reseting the temporary lists back to original lists for next piece
            allBeige=beigeP+beigeC
            allRed=redP+redC
            tempRedP=redP[:]                 
            tempRedC=redC[:]
            tempRed=tempRedP+tempRedC
            tempBeigeP=beigeP[:]
            tempBeigeC=beigeC[:]
            tempBeige=tempBeigeP+tempBeigeC
            AI=1     #setting AI to 1 to get Valid moves for AI
            Valid=[] #Emptying valid moves list for every iteration
            ValidB1=getValid(allBeige[i])  #getting all possible moves for each beige piece

            #A for loop that iterates over list of valid moves for
            #each beige piece and makes that move one at a time
            for j in range(len(ValidB1)):
                #reseting the temporary lists back to original lists for next piece
                allBeige=beigeP+beigeC
                allRed=redP+redC
                tempRedP=redP[:]                 
                tempRedC=redC[:]
                tempRed=tempRedP+tempRedC
                tempBeigeP=beigeP[:]
                tempBeigeC=beigeC[:]
                tempBeige=tempBeigeP+tempBeigeC
                AI=0                           #Setting AI to zero to get player valid moves
                countR=ValidB1[j][1]           #keeping the count of red pieces deleted

                #making that first valid move by removing piece from the 
                #appropriate temporary list and adding new position in the same list
                if allBeige[i] in tempBeigeP:
                    tempBeigeP=tempBeigeP+[ValidB1[j][0]]
                    tempBeigeP.remove(allBeige[i]) 
                elif allBeige[i] in tempBeigeC:
                    tempBeigeC=tempBeigeC+[ValidB1[j][0]]
                    tempBeigeC.remove(allBeige[i])
                tempBeige=tempBeigeP+tempBeigeC    #updating the temporary list after move had been made
                #print "temp after", tempBeige
                redMoves=[] #An empty list to keep possible red moves for each valid beige move made

                #A for loop that gets all possible red moves if that valid biege move was made
                for w in range(len(allRed)):
                    Valid=[]                       #emptying valid list to get new valid moves
                    oppValid=getValid(allRed[w])   #Calling get valid function
                    max=-1
                    #A for loop that iterates over all valid red moves and 
                    #appends all moves with corresponding count to a list
                    for k in range(len(oppValid)):
                        countB=oppValid[k][1]   #number of beige pieces removed
                        count=countR-countB     #number of red pieces removed - number of beige pieces removed
                        #list that contains the beige piece, its valid move and the count of pieces removed 
                        allMoves=allMoves+[[allBeige[i],ValidB1[j][0],count]]
        #A for loop that repeats 3 times and iterates over the
        #all moves to remove repeated moves with same count values
        for i in range(3):
            for v in range(len(allMoves)):
                if v+1<len(allMoves):
                    #checks if it is the current move is exactly the same as the next move
                    if (allMoves[v][0]==allMoves[v+1][0]) and (allMoves[v][1]==allMoves[v+1][1]):
                        #keeps the one with greater count
                        if allMoves[v][2]>=allMoves[v+1][2]:
                            allMoves.remove(allMoves[v+1])
                        else:
                            allMoves.remove(allMoves[v])                  
        max=-1
        #A for loop that iterates over all possible moves and their corresponding 
        #count, it then stores the move with max count in finalMove
        for u in range(len(allMoves)):
            if allMoves[u][2]>max:
                max=allMoves[u][2]
                finalMove=allMoves[u]
        #checks if all moves had no jumps
        if finalMove[2]==0:
            #a for loop that iterates over all moves and checks if a piece could be crowned
            for z in range(len(allMoves)):
                if allMoves[z][0] not in beigeC:
                    if allMoves[z][1][1]==0:
                        finalMove=allMoves[z]   #makes the piece that could be crowned the final move
        finalMove=finalMove[:2]                 #removing count from final move, making it a list of current position and valid move only
    initial=finalMove[0]                        #saving current position in a variable
    final=finalMove[1]                          #saving move position in a variable

    #checks if a double jump is going to be made
    if doubleJump:
        if final in doubleJump[0][1]:
            #calls delete red function twice to remove both red pieces it jumped over
            deletingRed(0,initial,doubleJump[0][0][0])     
            deletingRed(initial,doubleJump[0][0][0],final)
            doubleJump=[]   #reseting double jumps back to an empty list for next move
    pygame.draw.rect(gameDisplay, black, [initial[0],initial[1],50,50])   #removing beige piece from board at current position
    pygame.draw.rect(gameDisplay, black, [initial[0],initial[1],50,50],2) #removing highlight around the piece
    pygame.draw.circle(gameDisplay,beige,(final[0]+25,final[1]+25),20)    #drawing a new beige piece at valid move position clicked
    deletingRed(0,initial,final)                                          #calls delete red function to remove red piece it jumped over
    crowned(initial,final)                                                #calling crowned function to check if move makes piece crowned and to delete red pieces jumped over
    switchCode1()                                                         #switching back to player 0 


#A function that is called when twoPlayers button is clicked on main menu and sets the whole game for two players
def twoPlayer():
    global gameDisplay,twoPlayers,wnd
    twoPlayers=True                   #setting twoPlayers variable to true to allow it to access certain parts of code
    #Initializing pygame
    pygame.init()
    #Creating the canvas
    gameDisplay = pygame.display.set_mode((400,400))
    #Display name of game
    pygame.display.set_caption("Checkers")
    gameExit = False
    gameboard()                      #Calling gameboard function to set up the board
    pygame.display.update()          #updates canvas after board has been set
                                                
    #setting the game loop
    while not gameExit:
        #event handling loop
        for event in pygame.event.get():
            #Quitting game if quit button pressed
            if event.type == pygame.QUIT:
                gameExit = True
            #If mouse was clicked for the first time, calls mouseClick function 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s0==0:
                    mx , my = pygame.mouse.get_pos() #getting x and y position where mouse was clicked
                    mouseClicked(mx,my)              #calling mouseClicked function to handle where mouse was clicked for first time     
                    winning()                        #calling winning function to check if after mouse click a player could win
                #If nit first mouse clicks, calls mouseClick2 function 
                elif s0==1:
                    mx , my = pygame.mouse.get_pos() #getting x and y position where mouse was clicked
                    mouseClick2(mx,my)               #calling mouseClicked function to handle where mouse was clicked 
                    winning()                        #calling winning function to check if after mouse click a player could win
            pygame.display.update()                  #updating the gameboard at all times
    #Quitting the game if the game loop is exited
    pygame.quit()
    quit()
    
#A function that is called when onePlayer button is clicked on main menu and sets the whole game for one players
def onePlayer():
    global gameDisplay,wnd,twoPlayers
    twoPlayers=False      #setting twoPlayers variable to false to prevent from accessing certain parts of code
    #Initializing pygame
    pygame.init()
    #Creating the canvas
    gameDisplay = pygame.display.set_mode((400,400))
    #Display name of game
    pygame.display.set_caption("Checkers")
    gameExit = False
    gameboard()             #Calling gameboard function to set up the board
    pygame.display.update() #updates canvas after board has been set
    
    #setting the game loop
    while not gameExit:
        #if player is 0, it handle different events and gets mouse clicks
        if player==0:
            #event handling loop
            for event in pygame.event.get():
                #Quitting game if quit button pressed
                if event.type == pygame.QUIT:
                    gameExit = True
                #If mouse was clicked for the first time, calls mouseClick function 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if s0==0:
                        mx , my = pygame.mouse.get_pos() #getting x and y position where mouse was clicked
                        mouseClicked(mx,my)              #calling mouseClicked function to handle where mouse was clicked for first time  
                        winning()                        #calling winning function to check if after mouse click a player could win
                    elif s0==1:
                        mx , my = pygame.mouse.get_pos() #getting x and y position where mouse was clicked
                        mouseClick2(mx,my)               #calling mouseClicked function to handle where mouse was clicked 
                        winning()                        #calling winning function to check if after mouse click a player could win
        #if player is 1, then it calls AIMove as the computer handles the moves by itself
        elif player==1:
            AIMove()
            winning()           #calling winning function to check if after mouse click a player could win
        pygame.display.update() #updating the gameboard at all times
    #Quitting the game if the game loop is exited
    pygame.quit()
    quit()

#Initializing condition 
condition=None    #A variable that is set to False when one player is chosen and True when 2 players are chosen from main menu

#Creating a window for main menu
wnd = tk.Tk()
wnd.title("CHECKERS")
#saving all images paths
background="/Users/mennaelgendy/Desktop/Python/Final_project/Mainmenu.gif"
player="/Users/mennaelgendy/Desktop/Python/Final_project/PLAYER.gif"
players="/Users/mennaelgendy/Desktop/Python/Final_project/PLAYERS.gif"
Exit="/Users/mennaelgendy/Desktop/Python/Final_project/EXIT.gif"
#loading all images
background_pic=tk.PhotoImage(file=background)
player_pic=tk.PhotoImage(file=player)
players_pic=tk.PhotoImage(file=players)
Exit_pic=tk.PhotoImage(file=Exit)
#creating a canvas where background picture is loaded
c=tk.Canvas(wnd,width=390,height=390)
c.pack()
c.create_image(0,0,anchor="nw",image=background_pic)
#Adding button 1
b1=tk.Button(wnd,width=73,height=10,image=player_pic, command=deleteWnd1)
#creating a window within the main window for the button image to be clickable
b1_wnd=c.create_window(105,200,anchor="n",window=b1)
#Adding button 2
b2=tk.Button(wnd,width=80,height=10,image=players_pic, command=deleteWnd2)
#creating a window within the main window for the button image to be clickable
b2_wnd=c.create_window(300,200,anchor="n",window=b2)
#Adding button 3
b3=tk.Button(wnd,width=55,height=10,image=Exit_pic, command=deleteWnd)
#creating a window within the main window for the button image to be clickable
b3_wnd=c.create_window(50,360,anchor="n",window=b3)
# start the event loop
wnd.mainloop()

#Initializing some global variables
redC=[]      #empty list for crowned red pieces
beigeC=[]    #empty list for crowned beige pieces
redP=[]      #empty list for red pieces
beigeP=[]    #empty list for crowned beige pieces
player = 0   #starting with player 0
s0 = 0       #first state of mouse click is 0 until first mouse click was valid
s1 = 0       #second state of mouse click is 0 until second mouse click was valid
current = [] #empty list that holds position of current piece
firstMove = False #A variable that changes when player makes his first move
firstMve = False  #Changes to True after first move for AI
notCross = False  #A variable that changes when player makes a jump 
switch=False      #A variable that changes when players are switched
AI=-1             #A variable for AI if it was 1 then its AI if 0 then its the player
Jumped=False      #A variable set to determine if a jump is made or not
doubleJump=[]     #A list that holds a valid single and double jumps
Valid=[]          #An empty list for all valid moves of current piece
twoPlayers=False  #Setting a variable to determine if AI or 2 players, set to true if 2 players
tempBeigeP=[]     #A list that hold all beige pieces and a temporary possible move for AI
tempRedP=[]       #A list that hold all red pieces and a temporary possible move for AI
tempBeigeC=[]     #A list that hold all king beige pieces and a temporary possible move for AI
tempRedC=[]       #A list that hold all king red pieces and a temporary possible move for AI
nJumps=0          #A variable that limits the number of jumps to 2 when AI is used
#Defining colors
beige=(245,245,220)
red=(165,42,42)
black=(0,0,0)
brown=(222,184,135)
neonY=(243,243,21)
neonG=(131,245,44)


#Code that works after window has been destroyed
# if condition was false it means he chose one player and it calls the function
#if condition was True this means he chose 2 players and it calls the function
if condition==False:
    onePlayer()
elif condition==True:
    twoPlayer()
