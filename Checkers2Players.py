import pygame

#Setting board
def gameboard():
    global red,beige,black,brown, gameDisplay, redP, beigeP
    #Empty list for red and beige pieces
    y=-100
    x=50
    gameDisplay.fill(brown)
    for j in range(4):
        y=y+100
        x=50
        for i in range (4):
            pygame.draw.rect(gameDisplay,black,[x,y,50,50])
            if j==0 or j==1:
                redP.append([x,y])
                pygame.draw.circle(gameDisplay,red,(x+25,y+25),20)
                
            elif j==3:
                beigeP.append([x,y])
                pygame.draw.circle(gameDisplay,beige,(x+25,y+25),20)
            x=x+100
            
        x=0
        for i in range (4):
            pygame.draw.rect(gameDisplay,black,[x,y+50,50,50])
            if j==0:
                redP.append([x,y+50])
                pygame.draw.circle(gameDisplay,red,(x+25,y+75),20)
            elif j==2 or j==3:
                if j==2:
                    beigeP.append([x,y+50])
                elif j==3:
                    beigeP.append([x,y+50])
                pygame.draw.circle(gameDisplay,beige,(x+25,y+75),20)
            x=x+100
def crowned(current,move):
    global gameDisplay, redP,redC, beigeC, beigeP, player, black
    initialx=move[0]
    initialy=move[1]
    
    if (player==0):
        if (initialy==350) or (current in redC):
            pygame.draw.circle(gameDisplay,black,(initialx+25,initialy+25),15,5)
            redC.append([initialx,initialy])
        if (initialy != 350) and (current not in redC):
            redP.append([initialx,initialy])
        if current in redP:
            redP.remove(current)
        if current in redC:
            redC.remove(current)
    if (player==1):
        if (initialy==0) or (current in beigeC):
            pygame.draw.circle(gameDisplay,black,(initialx+25,initialy+25),15,5)
            beigeC.append([initialx,initialy])
        if (initialy !=0) and (current not in beigeC):
            beigeP.append([initialx,initialy])
        if current in beigeP:
            beigeP.remove(current)
        if current in beigeC:
            beigeC.remove(current)
            
def isValid(current,move):
    global redP,beigeP,redC,beigeC,player,s0, s1, firstMove, notCross, gameDisplay, black
    if (s1==1) and (player==0) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #moving one space diagonally forward
        if move[1]==current[1]+50:
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0
                notCross=True
                return True
        #moving one space diagonally backward
        if (current in redC) and (move[1]==current[1]-50):
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0
                notCross=True
                return True
    if (player==0) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #making a jump forward
        if move[1]==current[1]+100:
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50])
                beigeP.remove([current[0]+50,current[1]+50])
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50])
                beigeC.remove([current[0]+50,current[1]+50])
                return True                                  
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])
                beigeP.remove([current[0]-50,current[1]+50])
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])
                beigeC.remove([current[0]-50,current[1]+50])
                return True
        #making a jump backward
        if (current in redC) and (move[1]==current[1]-100):
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50])
                beigeP.remove([current[0]+50,current[1]-50])
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50])
                beigeC.remove([current[0]+50,current[1]-50])
                return True                           
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in beigeP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50])
                beigeP.remove([current[0]-50,current[1]-50])
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in beigeC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50])
                beigeC.remove([current[0]-50,current[1]-50])
                return True
    #player 1 validity check       
    if (s1==1) and  (player==1) and (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #moving one space diagonally backward
        if move[1]==current[1]-50:
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0
                notCross=True
                return True
        #moving one space diagonally forward
        if (current in beigeC) and (move[1]==current[1]+50):
            if (move[0]==current[0]+50) or (move[0]==current[0]-50):
                s1=0
                notCross=True
                return True
    if (player==1) and  (move not in redP) and (move not in beigeP) and (move not in redC) and (move not in beigeC):
        #making a jump backward
        if move[1]==current[1]-100:
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50])
                redP.remove([current[0]+50,current[1]-50])
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]-50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]-50,50,50])
                redC.remove([current[0]+50,current[1]-50])
                return True 
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50])
                redP.remove([current[0]-50,current[1]-50])
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]-50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]-50,50,50])
                redC.remove([current[0]-50,current[1]-50])
                return True
        #making a jump forward
        if (current in beigeC) and (move[1]==current[1]+100):
            if (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50])
                redP.remove([current[0]+50,current[1]+50])
                return True
            elif (move[0]==current[0]+100) and ([current[0]+50,current[1]+50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]+50,current[1]+50,50,50])
                redC.remove([current[0]+50,current[1]+50])
                return True 
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redP):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])
                redP.remove([current[0]-50,current[1]+50])
                return True
            elif (move[0]==current[0]-100) and ([current[0]-50,current[1]+50] in redC):
                pygame.draw.rect(gameDisplay,black,[current[0]-50,current[1]+50,50,50])
                redC.remove([current[0]-50,current[1]+50])
                return True
            
def mouseClicked(mx,my):
    global gameDisplay, redP,redC,beigeC, beigeP,neonY, neonG, player, s0, s1,current
    #removing highlight from all pieces once mouse clikcked on one
    for i in range (len(beigeP)):
                pygame.draw.rect(gameDisplay,black,[beigeP[i][0],beigeP[i][1],50,50],2)
    for i in range (len(redP)):
                pygame.draw.rect(gameDisplay,black,[redP[i][0],redP[i][1],50,50],2)
    for i in range (len(redC)):
                pygame.draw.rect(gameDisplay,black,[redC[i][0],redC[i][1],50,50],2)
    for i in range (len(beigeC)):
                pygame.draw.rect(gameDisplay,black,[beigeC[i][0],beigeC[i][1],50,50],2)
    mx = mx/50
    my = my/50
    position = [mx*50,my*50]
    initialx=position[0]
    initialy=position[1]
    #First mouse click
    #Checking if there is a piece in the position where the mouse
    #was first clicked and highlighting it if there were one
    if (player == 0) and ((position in redP) or (position in redC)):
        current=[initialx,initialy]
        s0 = 1
        s1 = 1
        pygame.draw.rect(gameDisplay, neonY, [initialx,initialy,50,50], 2)
    elif (player == 1) and ((position in beigeP) or (position in beigeC)) :
        current=[initialx,initialy]
        s0 = 1
        s1 = 1
        pygame.draw.rect(gameDisplay, neonG, [initialx,initialy,50,50], 2)
                                                
#second mouse click
def mouseClick2(mx,my):
    global gameDisplay, redP,redC,beigeC, beigeP,neonY, neonG, player, s0, s1, current, firstMove, switch
    mx = mx/50
    my = my/50
    position = [mx*50,my*50]
    initialx=position[0]
    initialy=position[1]
    if (player==0):
        if isValid(current,[initialx,initialy]):
            firstMove=True
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50])
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50],2)
            pygame.draw.circle(gameDisplay,red,(initialx+25,initialy+25),20)
            crowned(current,[initialx,initialy])
            current=[initialx,initialy]
            switchPlayer(current)
            if switch==False:
                pygame.draw.rect(gameDisplay, neonY, [current[0],current[1],50,50],2)
                
        #playing again if first movve was invalid
        if firstMove==False:
            s0=0
            s1=0
            
    if (player==1):
        if isValid(current,[initialx,initialy]):
            firstMove=True
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50])
            pygame.draw.rect(gameDisplay, black, [current[0],current[1],50,50],2)
            pygame.draw.circle(gameDisplay,beige,(initialx+25,initialy+25),20)
            crowned(current,[initialx,initialy])
            current=[initialx,initialy]
            switchPlayer(current)
            if switch==False:
                pygame.draw.rect(gameDisplay, neonG, [current[0],current[1],50,50],2)
                
        if firstMove==False:
            s0=0
            s1=0
def switchCode0():
    global gameDisplay, beigeC, beigeP,neonY, neonG, player, s0, s1, firstMove, notCross, switch
    player=1
    s0=0
    s1=0
    firstMove=False
    notCross=False
    switch=True
    print "player",player
    #highlighting the pieces of beige player, crowned and uncorwned
    for i in range (len(beigeP)):
        pygame.draw.rect(gameDisplay,neonG,[beigeP[i][0],beigeP[i][1],50,50],2)
    for i in range (len(beigeC)):
      pygame.draw.rect(gameDisplay,neonG,[beigeC[i][0],beigeC[i][1],50,50],2)
def switchCode1():
    global gameDisplay, redP, redC,neonY, neonY, player, s0, s1, firstMove, notCross, switch
    player=0     
    s0=0
    s1=0
    firstMove=False
    notCross=False
    switch=True
    print "player",player
    for i in range(len(redP)):
        pygame.draw.rect(gameDisplay,neonY,[redP[i][0],redP[i][1],50,50],2)
    for i in range (len(redC)):
        pygame.draw.rect(gameDisplay,neonY,[redC[i][0],redC[i][1],50,50],2)
    
        
def switchPlayer(position):
    global gameDisplay, redP, beigeP,redC, beigeC, neonY, neonG, player, s0, s1, black, firstMove, notCross, switch
    x=position[0]
    y=position[1]
    switch=False
    if (player==0):
        if firstMove==True and notCross==True:
            switchCode0()
        elif position in redC:
            print "gena redC"
            switchPlayerCrown(position)
        else:
            #if there are no possible jumps
            print "e7na hena?"
            if ([x+50,y+50] not in beigeP) and ([x+50,y+50] not in beigeC) and ([x-50,y+50] not in beigeP) and ([x-50,y+50] not in beigeC):
                 switchCode0()
                    
            elif ([x+50,y+50] in beigeP or [x+50,y+50] in beigeC) and ([x-50,y+50] not in beigeP or [x-50,y+50] not in beigeC):
                  if ([x+100,y+100] in beigeP) or ([x+100,y+100] in beigeC) or ([x+100,y+100] in redP) or ([x+100,y+100] in redC) or ((x+100)>350) or ((y+100)>350):
                     switchCode0()
            elif ([x-50,y+50] in beigeP or [x-50,y+50] in beigeC) and ([x+50,y+50] not in beigeP or [x+50,y+50] not in beigeC):
                   if ([x-100,y+100] in beigeP) or ([x-100,y+100] in beigeC) or ([x-100,y+100] in redP) or ([x-100,y+100] in redC) or (x-100<0) or (y+100>350):
                     switchCode0()
            elif ([x-50,y+50] in beigeP or [x-50,y+50] in beigeC) and ([x+50,y+50] in beigeP or [x+50,y+50] in beigeC):
                if (([x+100,y+100] in beigeP or [x+100,y+100] in beigeC) or ([x+100,y+100] in redP or [x+100,y+100] in redC) or ((x+100)>350) or ((y+100)>350)):
                    if (([x-100,y+100] in beigeP or [x-100,y+100] in beigeC) or ([x-100,y+100] in redP or [x-100,y+100] in redC) or (x-100<0) or (y+100>350)):
                         switchCode0()
    elif (player==1):
        if firstMove==True and notCross==True:
             switchCode1()
        elif position in beigeC:
            print "gena beigeC"
            switchPlayerCrown(position)
        else:
            if ([x+50,y-50] not in redP or [x+50,y-50] not in redC) and ([x-50,y-50] not in redP or [x-50,y-50] not in redC):
                 switchCode1()
                    
            elif ([x+50,y-50] in redP or [x+50,y-50] in redC) and ([x-50,y-50] not in redP or [x-50,y-50] not in redC):
                if ([x+100,y-100] in beigeP or [x+100,y-100] in beigeC) or ([x+100,y-100] in redP or [x+100,y-100] in redC) or (x+100>350) or (y-100<0):
                     switchCode1()
                        
            elif ([x-50,y-50] in redP or [x-50,y-50] in redC) and ([x+50,y-50] not in redP or [x+50,y-50] not in redC):
                 if ([x-100,y-100] in beigeP or [x-100,y-100] in beigeC) or ([x-100,y-100] in redP or [x-100,y-100] in redC) or (x-100<0) or (y-100<0):
                     switchCode1()
                        
            elif  ([x-50,y-50] in redP or [x-50,y-50] in redC) and ([x+50,y-50] in redP or [x+50,y-50] in redC):
                if (([x+100,y-100] in beigeP or [x+100,y-100] in beigeC) or ([x+100,y-100] in redP or [x+100,y-100] in redC) or (x+100>350) or (y-100<0)):
                    if (([x-100,y-100] in beigeP or [x-100,y-100] in beigeC) or ([x-100,y-100] in redP or [x-100,y-100] in redC) or (x-100<0) or (y-100<0)):
                         switchCode1()
                         
def switchPlayerCrown(position):
    global gameDisplay, redP, beigeP,redC, beigeC, neonY, neonG, player, s0, s1, black, switch
    x=position[0]
    y=position[1]
    switch=False
    chance=False
    print "x,y" , [x,y]
    print "redP",redP
    print "redC",redC
    print "beigeP" , beigeP
    print "beigeC",beigeC
    if (player==0):
        print "x+50,y-50" ,[x+50,y-50] in beigeP
        if ([x+50,y+50] not in beigeP) and ([x+50,y+50] not in beigeC) and ([x-50,y+50] not in beigeP) and ([x-50,y+50] not in beigeC):
            if ([x+50,y-50] not in beigeP) and ([x+50,y-50] not in beigeC) and ([x-50,y-50] not in beigeP) and ([x-50,y-50] not in beigeC):
                print "mafish move?"
                switchCode0()
        if ([x+50,y+50] in beigeP or [x+50,y+50] in beigeC):
              if ([x+100,y+100] not in beigeP) and ([x+100,y+100] not in beigeC) and ([x+100,y+100] not in redP) and ([x+100,y+100] not in redC) and ((x+100)<=350) and ((y+100)<=350):
                  print "hena 1"
                  chance=True
        if  ([x+50,y-50] in beigeP or [x+50,y-50] in beigeC):
            if ([x+100,y-100] not in beigeP) and ([x+100,y-100] not in beigeC) and ([x+100,y-100] not in redP) and ([x+100,y-100] not in redC) and ((x+100)<=350) and ((y-100)>=0):
                print "mafrod ygi hena"
                chance=True
        if ([x-50,y+50] in beigeP or [x-50,y+50] in beigeC):
            if ([x-100,y+100] not in beigeP and [x-100,y+100] not in beigeC and [x-100,y+100] not in redP and [x-100,y+100] not in redC and (x-100)>=0 and (y+100)<=350):
                print "hena 2"
                chance=True
        if ([x-50,y-50] in beigeP or [x-50,y-50] in beigeC):
            if ([x-100,y-100] not in beigeP) and ([x-100,y-100] not in beigeC) and ([x-100,y-100] not in redP) and ([x-100,y-100] not in redC) and ((x-100)>=0) and ((y-100)>=0):
                print "hena 3"
                chance=True
        print "chance f red" , chance
        if chance==False:
            print "lw hena moshkela"
            switchCode0()
            
    elif (player==1):
        print "x,y" , [x+50,y+50]
        if ([x+50,y+50] not in redP) and ([x+50,y+50] not in redC) and ([x-50,y+50] not in redP) and ([x-50,y+50] not in redC):
            if ([x+50,y-50] not in redP) and ([x+50,y-50] not in redC) and ([x-50,y-50] not in redP) and ([x-50,y-50] not in redC):
                print "mafish move?"
                switchCode1()
        if ([x+50,y+50] in redP or [x+50,y+50] in redC):
            if ([x+100,y+100] not in redP) and ([x+100,y+100] not in redC) and ([x+100,y+100] not in beigeP) and ([x+100,y+100] not in beigeC) and ((x+100)<=350) and ((y+100)<=350):
                print "hena 1"
                chance=True
        if ([x+50,y-50] in redP or [x+50,y-50] in redC):
            if ([x+100,y-100] not in redP) and ([x+100,y-100] not in redC) and ([x+100,y-100] not in beigeP) and ([x+100,y-100] not in beigeC) and ((x+100)<=350) and ((y-100)>=0):
                print "mafrod ygi hena"
                chance=True     
        if ([x-50,y+50] in redP or [x-50,y+50] in redC):
            if ([x-100,y+100] not in redP) and ([x-100,y+100] not in redC) and ([x-100,y+100] not in beigeP) and ([x-100,y+100] not in beigeC) and ((x-100)>=0) and ((y+100)<=350):
                print "hena 2"
                chance=True
        if ([x-50,y-50] in redP or [x-50,y-50] in redC):
            if ([x-100,y-100] not in redP) and ([x-100,y-100] not in redC) and ([x-100,y-100] not in beigeP) and ([x-100,y-100] not in beigeC) and ((x-100)>=0) and ((y-100)>=0):
                print "hena 3"
                chance=True
        print "chance f beige" , chance
        if chance==False:
            print "lw hena moshkela"
            switchCode1()
            
def winning():
    global redP, beigeP,redC, beigeC
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    closeWin1=False
    closeWin2=False
    if len(redP) + len(redC)==0:
        print "player 1 won"
    if len(beigeP) + len(beigeC)==0:
        print "player 0 won"
    
    #checking if player 1 had no possible moves
    for i in range (len(beigeP)):
        x=beigeP[i][0]
        y=beigeP[i][1]
        if (([x+50,y-50] in redP) or ([x+50,y-50] in redC) or ([x+50,y-50] in beigeP) or ([x+50,y-50] in beigeC) or ((x+50)>350) or ((y-50)<0)):
            if (([x-50,y-50] in redP) or ([x-50,y-50] in redC) or ([x-50,y-50] in beigeP) or ([x-50,y-50] in beigeC) or ((x-50)<0) or ((y-50)<0)):
                f1=f1+[1]
    if len(f1)==len(beigeP):
        closeWin1=True
    for i in range (len(beigeC)):
        x=beigeC[i][0]
        y=beigeC[i][1]
        if ([x+50,y+50] in redP or [x+50,y+50] in redC or [x+50,y+50] in beigeP or [x+50,y+50] in beigeC or ((x+50)>350) or ((y+50)>350)):
            if ([x-50,y+50] in redP or [x-50,y+50] in redC or [x-50,y+50] in beigeP or [x-50,y+50] in beigeC or ((x-50)<0) or ((y+50)>350)):
                if ([x+50,y-50] in redP or ([x+50,y-50] in redC or [x+50,y-50] in beigeP or ([x+50,y-50] in beigeC or ((x+50)>350) or ((y-50)<0)))):
                    if (([x-50,y-50] in redP) or([x-50,y-50] in redC) or ([x-50,y-50] in beigeP) or([x-50,y-50] in beigeC) or ((x-50)<0) or ((y-50)<0)):
                        f2=f2+[1]
    if len(f2)==len(beigeC) and closeWin1==True:
        print "player 0 won"
        
    #checking if player 0 had no possible moves
    for i in range (len(redP)):
        x=redP[i][0]
        y=redP[i][1]
        if (([x+50,y+50] in beigeP) or ([x+50,y+50] in beigeC) or ([x+50,y+50] in redP) or ([x+50,y+50] in redC) or ((x+50)>350) or ((y+50)>350)):
            if (([x-50,y+50] in beigeP) or([x-50,y+50] in beigeC) or ((x-50)<0) or ([x-50,y+50] in redP) or([x-50,y+50] in redC) or ((x-50)<0) or ((y+50)>350)):
                f3=f3+[1]
    if len(f3)==len(redP):
        closeWin2=True
    for i in range (len(redC)):
        x=redC[i][0]
        y=redC[i][1]
        if ([x+50,y+50] in redP or [x+50,y+50] in redC or [x+50,y+50] in beigeP or [x+50,y+50] in beigeC or ((x+50)>350) or ((y+50)>350)):
            if ([x-50,y+50] in redP or [x-50,y+50] in redC or [x-50,y+50] in beigeP or [x-50,y+50] in beigeC or ((x-50)<0) or ((y+50)>350)):
                if ([x+50,y-50] in redP or ([x+50,y-50] in redC or [x+50,y-50] in beigeP or ([x+50,y-50] in beigeC or ((x+50)>350) or ((y-50)<0)))):
                    if (([x-50,y-50] in redP) or([x-50,y-50] in redC) or ([x-50,y-50] in beigeP) or([x-50,y-50] in beigeC) or ((x-50)<0) or ((y-50)<0)):
                        f4=f4+[1]
    if len(f4)==len(redC) and closeWin2==True:
        print "player 1 won"
                      
#Initializing some global variables
redC=[]
beigeC=[]
redP=[]
beigeP=[]
player = 0
s0 = 0
s1 = 0
current = []
firstMove = False
notCross = False
switch=False
#Defining colors
beige=(245,245,220)
red=(165,42,42)
black=(0,0,0)
brown=(222,184,135)
neonY=(243,243,21)
neonG=(131,245,44)

#Initializing pygame
pygame.init()
#Creating the canvas
gameDisplay = pygame.display.set_mode((400,400))
#Display name of game
pygame.display.set_caption("Checkers")
gameExit = False
gameboard()
pygame.display.update()
                                                
#setting the game loop
while not gameExit:
    #event handling loop
    for event in pygame.event.get():
        #Quitting game if quit button pressed
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if s0==0:
                mx , my = pygame.mouse.get_pos()
                mouseClicked(mx,my)
                winning()
            elif s0==1:
                mx , my = pygame.mouse.get_pos()
                mouseClick2(mx,my)
                print winning()
        pygame.display.update()

#Quitting the game if the game loop is exited
pygame.quit()
quit()
