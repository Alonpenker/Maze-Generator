import pygame
import random
import os
pygame.init()
screenWidth = 1000
screenHeight = 800
display = (screenWidth, screenHeight)
win = pygame.display.set_mode(display)
pygame.display.set_caption("Maze Generator")
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (0,255,255)
white = (255,255,255)
black = (0,0,0)
font1 = pygame.font.SysFont(pygame.font.get_fonts()[2],21)
options = font1.render("Options: Press 'G' to generate a maze, press 'S' to solve the maze and press 'R' to reset.", 1, white)
options2 = font1.render("Click any of the buttons below to resize the maze.", 1, white)
bg = pygame.image.load(os.path.join('Images','Bg.png'))
title = pygame.image.load(os.path.join('Images','title.png'))
icon = pygame.image.load(os.path.join('Images','icon.png'))
buttons1 =[pygame.image.load(os.path.join('Images','button4.1.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button8.1.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button16.1.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button32.1.png')).convert_alpha()]
buttons2 =[pygame.image.load(os.path.join('Images','button4.2.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button8.2.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button16.2.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button32.2.png')).convert_alpha()]
buttons3 =[pygame.image.load(os.path.join('Images','button1.png')).convert_alpha(),pygame.image.load(os.path.join('Images','button2.png')).convert_alpha()]
pygame.display.set_icon(icon)
class square():
    def __init__(self,n,row,col,dir,color):
        self.n = n
        self.row = row
        self.col = col
        self.dir = dir
        self.lines = ["u","r","d","l"]
        self.color = color
        self.width = 800 / self.n
        self.height = 640/self.n
        self.x = (self.col-1)*self.width+100
        self.y = (self.row-1)*self.height+80
        self.midX = int((self.col-1)*self.width+100+0.5*self.width)
        self.midY = int((self.row-1)*self.height+80+0.5*self.height)
        self.isVisited = False
    def checkDirections(self,matrix):
        self.dir.clear()
        if self.row>1:
            if matrix[self.row - 2][self.col - 1].isVisited == False:  # up
                self.dir.append("up")
        if self.col<n:
            if matrix[self.row - 1][self.col].isVisited == False:  # right
                self.dir.append("right")
        if self.row<self.n:
            if matrix[self.row][self.col - 1].isVisited == False:  # down
                self.dir.append("down")
        if self.col>1:
            if matrix[self.row - 1][self.col - 2].isVisited == False:  # left
                self.dir.append("left")
        if self.row==n and self.col==n:
            self.dir.clear()
    def draw(self,win):
        if self.row==n and self.col==n:
            self.color=green
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        if "u" in self.lines:
            pygame.draw.line(win, (0,0,0), (self.x, self.y), (self.x+self.width, self.y), 2)
        if "d" in self.lines:
            pygame.draw.line(win, (0,0,0), (self.x, self.y+self.height), (self.x+self.width,self.y+self.height), 2)
        if "l" in self.lines:
            pygame.draw.line(win, (0,0,0), (self.x, self.y), (self.x, self.y+self.height), 2)
        if "r" in self.lines:
            pygame.draw.line(win, (0,0,0), (self.x+self.width, self.y), (self.x+self.width, self.y+self.height), 2)
n = 4
w ,h = n, n
matrix = [[0 for x in range(w)] for y in range(h)] #matrix[row][col]
for i in range(1,n+1,1):
   for f in range(1,n+1,1):
       matrix[i-1][f-1] = square(n,i,f,["up","right","down","left"],blue)
matrix[0][0].color=red
matrix[0][0].isVisited=True
matrix[n-1][n-1].color=green
path=[matrix[0][0]]
solvePath=[matrix[0][0]]
blackList = [matrix[0][0]]
start = False
solve = False
run = True
mode = "Opening Screen"
def check():
    for i in range(1, n + 1, 1):
        for f in range(1, n + 1, 1):
            if matrix[i - 1][f - 1].isVisited==False:
                return False
    return True
def reset():
    global matrix,path,start ,solvePath, blackList, solve,x,y
    del matrix
    w, h = n, n
    matrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(1, n + 1, 1):
        for f in range(1, n + 1, 1):
            matrix[i - 1][f - 1] = square(n, i, f, ["up", "right", "down", "left"], blue)
    matrix[0][0].color = red
    matrix[0][0].isVisited = True
    matrix[n - 1][n - 1].color = green
    path = [matrix[0][0]]
    solvePath = [matrix[0][0]]
    blackList = [matrix[0][0]]
    start = False
    solve = False
while run:
    if mode == "Opening Screen":
        win.blit(bg, (0, 0))
        pygame.time.delay(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (400 + 200 > mouse[0] > 400) and (600 + 75 > mouse[1] > 600):
                    mode="Game"
        if (400 + 200 > mouse[0] > 400) and (600 + 75 > mouse[1] > 600):
            win.blit(buttons3[1], (400, 600))
        else:
            win.blit(buttons3[0], (400, 600))
        win.blit(title, (250, 200))
    if mode == "Game":
        win.fill((0, 0, 0))
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    start = True
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_s:
                    if check() == True:
                        solve = True
                        #print("now solving")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for m in range(0, 4, 1):
                    if (300 + m * 100 + 80 > mouse[0] > 300 + m * 100) and (
                            screenHeight - 10 > mouse[1] > screenHeight - 60):
                        n = 2 ** (m + 2)
                        reset()
        mouse = pygame.mouse.get_pos()
        for t in range(0, 4, 1):
            if (300 + t * 100 + 80 > mouse[0] > 300 + t * 100) and (screenHeight - 10 > mouse[1] > screenHeight - 60):
                win.blit(buttons2[t], (300 + t * 100, screenHeight - 60))
            else:
                win.blit(buttons1[t], (300 + t * 100, screenHeight - 60))
        win.blit(options,(100,20))
        win.blit(options2, (100, 50))
        if start == True and check() == False: #draw maze
            path[len(path) - 1].checkDirections(matrix)
            if path[len(path) - 1].dir:
                choice = random.choice(path[len(path) - 1].dir)
                #print("col:", path[len(path) - 1].col, "  row:", path[len(path) - 1].row, "  direction:", choice)
                if choice == "up":
                    if ("u" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("u")
                    path.append(matrix[path[len(path) - 1].row - 2][path[len(path) - 1].col - 1])
                    path[len(path) - 1].isVisited = True
                    path[len(path) - 1].color = white
                    if ("d" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("d")
                if choice == "right":
                    if ("r" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("r")
                    path.append(matrix[path[len(path) - 1].row - 1][path[len(path) - 1].col])
                    path[len(path) - 1].isVisited = True
                    path[len(path) - 1].color = white
                    if ("l" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("l")
                if choice == "down":
                    if ("d" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("d")
                    path.append(matrix[path[len(path) - 1].row][path[len(path) - 1].col - 1])
                    path[len(path) - 1].isVisited = True
                    path[len(path) - 1].color = white
                    if ("u" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("u")
                if choice == "left":
                    if ("l" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("l")
                    path.append(matrix[path[len(path) - 1].row - 1][path[len(path) - 1].col - 2])
                    path[len(path) - 1].isVisited = True
                    path[len(path) - 1].color = white
                    if ("r" in path[len(path) - 1].lines):
                        path[len(path) - 1].lines.remove("r")
            else:
                #print("delete")
                del path[-1]
        if start == True and check() == True and solve == True and solvePath[len(solvePath) - 1].color != green: #draw path
            if ('l' in solvePath[len(solvePath) - 1].lines) == False and (matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col - 2] in blackList) == False and (matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col - 2] in solvePath) == False and solvePath[len(solvePath) - 1].col > 1:
                solvePath.append(matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col - 2])
                #print("try left")
            elif ('u' in solvePath[len(solvePath) - 1].lines) == False and (matrix[solvePath[len(solvePath) - 1].row - 2][solvePath[len(solvePath) - 1].col - 1] in blackList) == False and (matrix[solvePath[len(solvePath) - 1].row - 2][solvePath[len(solvePath) - 1].col - 1] in solvePath) == False and solvePath[len(solvePath) - 1].row > 1:
                solvePath.append(matrix[solvePath[len(solvePath) - 1].row - 2][solvePath[len(solvePath) - 1].col - 1])
                #print("try up")
            elif ('r' in solvePath[len(solvePath) - 1].lines) == False and (matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col] in blackList) == False and (matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col] in solvePath) == False and solvePath[len(solvePath) - 1].col < n:
                solvePath.append(matrix[solvePath[len(solvePath) - 1].row - 1][solvePath[len(solvePath) - 1].col])
                #print("try right")
            elif ('d' in solvePath[len(solvePath) - 1].lines) == False and (matrix[solvePath[len(solvePath) - 1].row][solvePath[len(solvePath) - 1].col - 1] in blackList) == False and (matrix[solvePath[len(solvePath) - 1].row][ solvePath[len(solvePath) - 1].col - 1] in solvePath) == False and solvePath[len(solvePath) - 1].row < n:
                solvePath.append(matrix[solvePath[len(solvePath) - 1].row][solvePath[len(solvePath) - 1].col - 1])
                #print("try down")
            else:
                #print("deleting", " col:", solvePath[len(solvePath) - 1].col, "  row:",solvePath[len(solvePath) - 1].row)
                blackList.append(solvePath[len(solvePath) - 1])
                solvePath.remove(solvePath[len(solvePath) - 1])
        for i in range(1, n + 1, 1):
            for f in range(1, n + 1, 1):
                matrix[i - 1][f - 1].draw(win)
        for k in range(0, len(solvePath) - 1, 1):
            pygame.draw.circle(win, blue, (int(solvePath[0].midX), int(solvePath[0].midY)), int((1 / n) * 224))
            if len(solvePath) > 1:
                # pygame.draw.circle(win, blue, (int(solvePath[k+1].midX), int(solvePath[k+1].midY)), int((1/n)*112))
                pygame.draw.line(win, blue, (int(solvePath[k].midX), int(solvePath[k].midY)),(int(solvePath[k + 1].midX), int(solvePath[k + 1].midY)), int((1 / n) * 128))
            if solvePath[len(solvePath) - 1].color == green:
                pygame.draw.circle(win, blue,
                                   (int(solvePath[len(solvePath) - 1].midX), int(solvePath[len(solvePath) - 1].midY)),
                                   int((1 / n) * 224))
    pygame.display.update()
pygame.quit()