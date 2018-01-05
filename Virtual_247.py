
import pygame,random, copy, sys
from pygame.locals import *

pygame.init()

def choosegame(msg):
    if msg == 1:
        game_1()
    elif msg == 2:
        game_2()
    else:
        print("Wrong choice")
def game_1():
    
    #----open game console 11
    display_width = 900
    display_height = 700
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    player1_width = 30
    player1_height = 30
    Finish_x_left = 0.116
    Finish_x_right = 0.18
    Finish_y_left = 0.10
    Finish_y_right = 0.166
    #--------colors--------
    black = (0,0,0)
    white = (255,255,255)
    grey = (100,100,100)
    red = (200,0,0)
    green = (0,200,0)
    reuven = (0,200,100)
    bright_reuven = (0,255,155)

    bright_red = (255,0,0)
    bright_green = (0,255,0)
    bright_grey = (155,155,155)
    #---------------------
    #----Title
    pygame.display.set_caption('Team no. 24 - Virtual_24/7')
    #----clock for holding
    clock = pygame.time.Clock()

    boardImg = pygame.image.load("Board.jpg")
    Player1 = pygame.image.load("1.jpg")
    Player2 = pygame.image.load("2.jpg")
    Game1 = pygame.image.load("Game1.jpg")
    Game2 = pygame.image.load("Game2.jpg")
    CubeImg1 = pygame.image.load("cube1.jpg")
    CubeImg2 = pygame.image.load("cube2.jpg")
    CubeImg3 = pygame.image.load("cube3.jpg")
    CubeImg4 = pygame.image.load("cube4.jpg")
    CubeImg5 = pygame.image.load("cube5.jpg")
    CubeImg6 = pygame.image.load("cube6.jpg")
    ExplainImg1 = pygame.image.load("explain1.jpg")
    ExplainImg2 = pygame.image.load("explain2.jpg")
    CardImg = pygame.image.load("card.jpg")
    quest1 = pygame.image.load("quest1.jpg")
    Player1Win = pygame.image.load("player1win.jpg")
    Player2Win = pygame.image.load("player2win.jpg")


    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def button(msg,x,y,w,h,ic,ac,action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf,textRect = text_objects(msg,smallText)
        
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
            textRect.center = ( (x+(w/2)) , (y+(h/2)))
            if click[0] == 1 and action != None:
                if action == "game1":
                    game1()
                elif action == "explain1":
                    explain1()
                elif action == "game2":
                    game2()
                elif action == "explain2":
                    explain2()
                elif action == "intro":
                    game_intro()
                elif action == "card":
                    card()
                elif action == "quit":
                    pygame.quit()
                    quit()
                    
        else:
            pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
            textRect.center = ( (x+(w/2)) , (y+(h/2)) )
     
        textRect.center = ( (x+(w/2)) , (y+(h/2)) )
        gameDisplay.blit(textSurf,textRect)

        
    def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',50)
            midText = pygame.font.Font('freesansbold.ttf',40)
            TextSurf, TextRect = text_objects("Welcome to Main Menu", largeText)
            TextSurf2, TextRect2 = text_objects("Choose a Game", midText)
            TextRect.center = ((display_width/2.1),(display_height/7))
            TextRect2.center = ((display_width/2),(display_height/4))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)
            button("Ladders and Snakes",100,300,300,200,green,bright_green,"explain1")
            gameDisplay.blit(Game1,(100,250))
            button("Four In Row",500,300,300,200,red,bright_red,"explain2")
            gameDisplay.blit(Game2,(500,250))
            button("QUIT",400,600,100,50,grey,bright_grey,"quit")
            
          
            pygame.display.update()
            clock.tick(100)

    def Board(x,y):
        gameDisplay.blit(boardImg,(x,y))
    def Player1_(x,y):
        gameDisplay.blit(Player1,(x,y))
    def Player2_(x,y):
        gameDisplay.blit(Player2,(x,y))
    def explainImg1(x,y):
        gameDisplay.blit(ExplainImg1,(x,y))
    def explainImg2(x,y):
        gameDisplay.blit(ExplainImg2,(x,y))
    def Cube(msg):
        x = display_width * 0.80
        y = display_width * 0.22
        if msg == 1:
            gameDisplay.blit(CubeImg1,(x,y))
        elif msg == 2:
            gameDisplay.blit(CubeImg2,(x,y))
        elif msg == 3:
            gameDisplay.blit(CubeImg3,(x,y))
        elif msg == 4:
            gameDisplay.blit(CubeImg4,(x,y))
        elif msg == 5:
            gameDisplay.blit(CubeImg5,(x,y))
        elif msg == 6:
            gameDisplay.blit(CubeImg6,(x,y))

    def card():
        cardExit = False

        while not cardExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  cardExit = True
            gameDisplay.fill(white)
            gameDisplay.blit(quest1,(200,100))
            button("1",700,550,100,100,reuven,bright_reuven)
            button("2",500,550,100,100,reuven,bright_reuven)
            button("3",300,550,100,100,reuven,bright_reuven)
            button("4",100,550,100,100,reuven,bright_reuven)
            pygame.display.update()
            clock.tick(100)
    def explain2():
        expExit = False

        while not expExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  expExit = True
            explainImg2(5,20)
            button("START GAME!",600,600,150,50,green,bright_green,"game2")
            button("<- BACK",100,600,150,50,red,bright_red,"intro")
            pygame.display.update()
            clock.tick(100)
    def explain1():
        expExit = False

        while not expExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  expExit = True
            explainImg1(5,20)
            button("START GAME!",600,600,150,50,green,bright_green,"game1")
            button("<- BACK",100,600,150,50,red,bright_red,"intro")
            pygame.display.update()
            clock.tick(100)
    def game1():
        #----position Imgs-----
        Board_x= (display_width * 0.10)
        Board_y= (display_height * 0.10)
        Player1_x= (display_width * 0.06)
        Player1_y= (display_height * 0.78)
        Player2_x= (display_width * 0.06)
        Player2_y= (display_height * 0.75)
        Cube_Number = random.randrange(1,7,1)
        #------------------------
        #----first position without moveing-----
        Player1_x_change = 0
        Player1_y_change = 0
        Player2_x_change = 0
        Player2_y_change = 0
        #------------------------
        gameExit = False

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  gameExit = True
                
         #------Player 1 movement------             
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Player1_x_change = -1
                    elif event.key == pygame.K_RIGHT:
                        Player1_x_change = 1
                    elif event.key == pygame.K_UP:
                        Player1_y_change = -1
                    elif event.key == pygame.K_DOWN:
                        Player1_y_change = 1
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        Player1_x_change =0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        Player1_y_change =0
         #------------------------------
         #------Player 2 movement------- 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        Player2_x_change = -1
                    elif event.key == pygame.K_d:
                        Player2_x_change = 1
                    elif event.key == pygame.K_w:
                        Player2_y_change = -1
                    elif event.key == pygame.K_s:
                        Player2_y_change = 1
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        Player2_x_change =0
                    elif event.key == pygame.K_s or event.key == pygame.K_w:
                        Player2_y_change =0
        #------Cube Show Random-------
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Cube_Number = random.randrange(1,7,1)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if Cube_Number == 1:
                            pygame.mixer.music.load('1.mp3')
                            pygame.mixer.music.play()    
                        elif Cube_Number == 2:
                            pygame.mixer.music.load('2.mp3')
                            pygame.mixer.music.play()    
                        elif Cube_Number == 3:
                            pygame.mixer.music.load('3.mp3')
                            pygame.mixer.music.play()    
                        elif Cube_Number == 4:
                            pygame.mixer.music.load('4.mp3')
                            pygame.mixer.music.play()    
                        elif Cube_Number == 5:
                            pygame.mixer.music.load('5.mp3')
                            pygame.mixer.music.play()    
                        elif Cube_Number == 6:
                            pygame.mixer.music.load('6.mp3')
                            pygame.mixer.music.play()
                        Cube(Cube_Number)
                        

         #------------------------------
                    
            Player1_x += Player1_x_change
            Player1_y += Player1_y_change
            Player2_x += Player2_x_change
            Player2_y += Player2_y_change
            gameDisplay.fill(white)
            Board(Board_x,Board_y)
            Player1_(Player1_x,Player1_y)
            Player2_(Player2_x,Player2_y)
            Cube(Cube_Number)
            if Player1_x > display_width - player1_width or Player1_x < 0 + player1_width:
                Player1_x = (display_width * 0.13)
                Player1_y = (display_height * 0.83)
            if Player1_x > 105 and Player1_x < 127 and Player1_y > 0.84 and Player1_y < 100:
                    gameDisplay.blit(Player1Win,(100,100))
            if Player2_x > 105 and Player2_x < 127 and Player2_y > 0.84 and Player2_y < 100:
                    gameDisplay.blit(Player2Win,(100,100))
            button("QUIT GAME",10,10,150,50,red,bright_red,"intro")
            button("",720,500,100,150,red,bright_red,"card")
            gameDisplay.blit(CardImg,(650,450))
            pygame.display.update()
            clock.tick(100)
        
    game_intro()
    pygame.quit()
    quit()

def game_2():
    pygame.init()


    #define screen Resolution and view
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Four in a Row - Virtual24')
    clock = pygame.time.Clock()
    EMPTY = None


    #GameSettings
    fps = 30
    spacesize = 50
    level = 1
    GameWidth = 7
    GameHeight = 6
    TokenSize = 50 
    Xspace = int((display_width - GameWidth*TokenSize)/2)
    Yspace = int((display_height - GameHeight*TokenSize)/2)

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    bright_red = (200,0,0)
    green = (0,255,0)
    bright_green = (0,200,0)
    blue = (0,0,255)
    bright_blue = (0,0,200)
    TextColor = green
    RedColor = 'red'
    BlackColor = 'black'
    PLAYER = 'player'
    COMPUTER = 'computer'

    #uploaded images and image settings
    Surf = pygame.display.set_mode((display_width, display_height))
    RedRect = pygame.Rect(int(spacesize / 2), display_height - int(3*spacesize/2), spacesize, spacesize)
    BlackRect = pygame.Rect(display_width - int(3 * spacesize / 2), display_height - int(3 * spacesize / 2), spacesize, spacesize)
    RedPlayer = pygame.image.load('RedPlayer.png')
    RedPlayer = pygame.transform.smoothscale(RedPlayer, (spacesize, spacesize))
    GameImage = pygame.image.load('GameBoard.png')
    GameImage = pygame.transform.smoothscale(GameImage, (spacesize, spacesize))
    WinnerHuman = pygame.image.load('WinnerHuman.JPEG')
    WinnerComputer = pygame.image.load('WinnerComputer.JPEG')
    TieGame = pygame.image.load('TieGame.JPEG')
    WinnerLocation = WinnerHuman.get_rect()
    WinnerLocation.center = (int(display_width / 2), int(display_height / 2))
    BlackPlayer = pygame.image.load('BlackPlayer.png')
    BlackPlayer = pygame.transform.smoothscale(BlackPlayer, (spacesize, spacesize))



    def GameStart():

        #Radomly decide who start the game
        if random.randint(0, 1) == 0:
            turn = COMPUTER
        else:
           turn = PLAYER
           
        #Get new Game board
        MainGame = getNewBoard()

        #Start Game
        while True:

            #Switch between turns and check who won
            if turn == PLAYER:
                getHumanMove(MainGame)
                if WhoWon(MainGame, RedColor):
                    winnerImg = WinnerHuman
                    break
                turn = COMPUTER
            else:
                col = ComputerTurn(MainGame)
                ComputerMovingAnimation(MainGame, col)
                makeMove(MainGame, BlackColor, col)
                if WhoWon(MainGame, BlackColor):
                    winnerImg = WinnerComputer
                    break
                turn = PLAYER 

            #If the Game Board is full with tokens (Tie)
            if GameBoardFull(MainGame):
                winnerImg = TieGame
                break
            
        #Second Loop To decide what happens after the game is over
        #Ways to end game: SPACE key, ESC, Click X button
        while True:
            ReplaceBoard(MainGame)
            Surf.blit(winnerImg,WinnerLocation)
            pygame.display.update()
            clock.tick()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_SPACE) or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    ChooseAlevel() #Start Game again by choosing a level


    def ReplaceBoard(board,AdditionalToken=None):
        Surf.fill(white)

        #Pick Up First Token
        spaceRect = pygame.Rect(0, 0, spacesize, spacesize)
        for x in range(GameWidth):
            for y in range(GameHeight):
                spaceRect.topleft = (Xspace + (x*spacesize), Yspace + (y*spacesize))
                if board[x][y] == RedColor:
                    Surf.blit(RedPlayer,spaceRect)
                elif board[x][y] == BlackColor:
                    Surf.blit(BlackPlayer,spaceRect)
        if AdditionalToken != None:
            if AdditionalToken['color'] == RedColor:
                Surf.blit(RedPlayer, (AdditionalToken['x'], AdditionalToken['y'], spacesize, spacesize))
            elif AdditionalToken['color'] == BlackColor:
                Surf.blit(BlackPlayer, (AdditionalToken['x'], AdditionalToken['y'], spacesize, spacesize))

        #Draw Another Layer On The Screen With New Moves
        for x in range(GameWidth):
            for y in range(GameHeight):
                spaceRect.topleft = (Xspace + (x*spacesize), Yspace + (y*spacesize))
                Surf.blit(GameImage, spaceRect)
        Surf.blit(RedPlayer, RedRect)
        Surf.blit(BlackPlayer, BlackRect)

    def makeMove(board, player, col):
        #Check if there is a free space at the bottom of the board to place token in
        ArrayBottom = GoAsDownAsPossible(board, col)
        if ArrayBottom != -1:
            board[col][ArrayBottom] = player

    def getNewBoard():
        #Create a new board sized 6*7 (our game board)
        board = []
        for x in range(GameWidth):
            board.append([EMPTY]*GameHeight)
        return board

    def getHumanMove(board):
        #wait for the player to take his turn
        GameToken = False
        xToken, yToken = None, None
        while True:
            for event in pygame.event.get():
                #End Game incase X button, ESC, SPACE
                if event.type == QUIT or (event.type == KEYUP and event.key == K_SPACE) or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    
                #Player Click on Token             
                elif event.type == MOUSEBUTTONDOWN and not GameToken and RedRect.collidepoint(event.pos):
                    GameToken = True
                    xToken, yToken = event.pos
                #Player Drag The Token                
                elif event.type == MOUSEMOTION and GameToken:
                    xToken, yToken = event.pos
                #If The Player Drop The Token               
                elif event.type == MOUSEBUTTONUP and GameToken: 
                    if yToken < Yspace and xToken > Xspace and xToken < display_width - Xspace:
                        col = int((xToken - Xspace) / spacesize)
                        if isMoveOK(board, col):
                            DropAnimation(board, col, RedColor)
                            board[col][GoAsDownAsPossible(board, col)] = RedColor
                            ReplaceBoard(board)
                            pygame.display.update()
                            return
                        
                    xToken, yToken = None, None
                    GameToken = False

                    
            if xToken != None and yToken != None:
                #Replace The Board with updated one
                ReplaceBoard(board, {'x':xToken - int(spacesize/2), 'y':yToken - int(spacesize/2), 'color':RedColor})
            else:
                #if there was no move keep the existing board
                ReplaceBoard(board)
            #update screen
            pygame.display.update()
            clock.tick()


    def DropAnimation(board,col,color):
        x = Xspace + col * spacesize
        y = Yspace - spacesize
        dropSpeed = 2.0
        lowestEmptySpace = GoAsDownAsPossible(board, col)

        while True:
            
            #Decide Were to drop the token
            y += int(dropSpeed)
            dropSpeed += 1.0
            if int((y - Yspace) / spacesize) >= lowestEmptySpace:
                return
            
            #Refill Board with new image after alteration
            ReplaceBoard(board, {'x':x, 'y':y, 'color':color})
            pygame.display.update()
            clock.tick()


    def ComputerMovingAnimation(board, col):
        #Function to decide what animation of computer move to show
        x = BlackRect.left
        y = BlackRect.top
        speed = 2.0
        while y > (Yspace - spacesize):
            y -= int(speed)
            speed += 1.0
            ReplaceBoard(board, {'x':x, 'y':y, 'color':BlackColor})
            pygame.display.update()
            clock.tick()

        # Moving the Computer Tile (BlackColor)
        y = Yspace - spacesize
        speed = 2.0
        while x > (Xspace + col * spacesize):
            x -= int(speed)
            speed += 1.0
            ReplaceBoard(board, {'x':x, 'y':y, 'color':BlackColor})
            pygame.display.update()
            clock.tick()
            
        # Drop The Computer Tile down
        DropAnimation(board, col, BlackColor)


    def ComputerTurn(board):
        PossibleMoves = getPossibleMoves(board,BlackColor,level)
        # "Think" about the best move possible for the computer to make
        FindBestMove = -1
        for i in range(GameWidth):
            if PossibleMoves[i] > FindBestMove and isMoveOK(board, i):
                FindBestMove = PossibleMoves[i]

        # Save All best moves in a list, and then randomize wich one to make
        bestMoves = []
        for i in range(len(PossibleMoves)):
            if PossibleMoves[i] == FindBestMove and isMoveOK(board, i):
                bestMoves.append(i)

        #Random func to pick a move
        return random.choice(bestMoves)


    def getPossibleMoves(board,tile,ThinkAhead):
        #This function figue out what is the best move for the computer to make
        if ThinkAhead == 0 or GameBoardFull(board):
            return [0] * GameWidth
        if tile == RedColor:
            enemyTile = BlackColor
        else:
            enemyTile = RedColor
        PossibleMoves = [0] * GameWidth
        for FirstPlay in range(GameWidth):
            BoardDP = copy.deepcopy(board)
            if not isMoveOK(BoardDP, FirstPlay):
                continue
            makeMove(BoardDP, tile, FirstPlay)
            if WhoWon(BoardDP, tile):
                PossibleMoves[FirstPlay] = 1
                break 
            else:
                if GameBoardFull(BoardDP):
                    PossibleMoves[FirstPlay] = 0
                else:
                    for counterMove in range(GameWidth):
                        BoardDP2 = copy.deepcopy(BoardDP)
                        if not isMoveOK(BoardDP2, counterMove):
                            continue
                        makeMove(BoardDP2, enemyTile, counterMove)
                        if WhoWon(BoardDP2, enemyTile):
                            PossibleMoves[FirstPlay] = -1
                            break
                        else:
                            results = getPossibleMoves(BoardDP2, tile, ThinkAhead - 1)
                            PossibleMoves[FirstPlay] += (sum(results) / GameWidth) / GameWidth
        return PossibleMoves

    def GameBoardFull(board):
        # checks if the game board is full with tokens (Tie)
        for x in range(GameWidth):
            for y in range(GameHeight):
                if board[x][y] == EMPTY:
                    return False
        return True


    def isMoveOK(board, col):
        #check if a specific move is ok to be done
        if col < 0 or col >= (GameWidth) or board[col][0] != EMPTY:
            return False
        return True


    def WhoWon(board, tile):
        # check cols
        for x in range(GameWidth - 3):
            for y in range(GameHeight):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True
        # check rows
        for x in range(GameWidth):
            for y in range(GameHeight - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True
        # check diagonal left
        for x in range(GameWidth - 3):
            for y in range(3, GameHeight):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True
        # check diagonal right
        for x in range(GameWidth - 3):
            for y in range(GameHeight - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        return False

    def GoAsDownAsPossible(board, col):
        for y in range(GameHeight-1, -1, -1):
            if board[col][y] == EMPTY:
                return y
        return -1

    def button(msg,x,y,w,h,ic,ac,action = None):
        #Display buttons on screen (Exit,Easy,Hard)
        #change game difficulty by changing level
        global level
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf,textRect = text_objects(msg,smallText)
        
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
            textRect.center = ( (x+(w/2)) , (y+(h/2)))
            if click[0] == 1 and action != None:
                if action == "Hard":
                    level = 2
                    GameStart()
                elif action == "Easy":
                    level = 1 
                    GameStart()
                elif action == "Quit Game":
                    pygame.quit()
                    quit()
                    
        else:
            pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
            textRect.center = ( (x+(w/2)) , (y+(h/2)) )
     
        textRect.center = ( (x+(w/2)) , (y+(h/2)) )
        gameDisplay.blit(textSurf,textRect)

    def ChooseAlevel():

        ExitGame = False

        while not ExitGame:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  ExitGame = True
            gameDisplay.fill(white)             
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Please Choose Difficulty Level", largeText)
            TextRect.center = ((display_width/2),(display_height/6))
            gameDisplay.blit(TextSurf, TextRect)
            button("Easy",50,240,250,200,green,bright_green,"Easy")
            button("Hard",500,240,250,200,red,bright_red,"Hard")
            button("Quit Game",335,430,130,130,blue,bright_blue,"Quit Game")
            pygame.display.update()
            clock.tick(60)

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
        
    ChooseAlevel()
GameChoice = int(input("Please enter a choice: 1- menu + ladders and snakes 2- for four in row    "))
choosegame(GameChoice)
        
