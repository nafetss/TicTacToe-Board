#import libs
import pygame
import time
import serial

#connection to the serial port
ArduinoUnoSerial = serial.Serial('COM3',9600)

#some python pygame essentials
pygame.init()
screen = pygame.display.set_mode((596, 800))
clock = pygame.time.Clock()
running = True
dt = 0

WINDOWS_BACKGROND_COLOR ="#2b2b2b" 
grid="000000000ss"
logo = pygame.image.load("images/logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption('Tic-Tac-Toe by Stefan')

def Image_Loader_Transformer(path,scale_X,scale_Y):
    image =pygame.image.load(path)
    image =pygame.transform.scale(image,(scale_X,scale_Y))
    return image

def LoadFont(path,fontSize):
    return pygame.font.Font(path,fontSize)

def Create_Text(txt,font,color,x,y):
    text = font.render(txt,True,color)
    textRect=text.get_rect()
    textRect.center = (x,y)
    return text,textRect

def Draw(sta_crtas,gde_crtas):
    screen.blit(sta_crtas,gde_crtas)

def Draw_Table(cell,X_image,O_image,startX,startY):
    for i in range(0,9):
        if(i==0 or i==3 or i==6):startX=70
        else: startX+=152
        if(grid[i] == '0'):
            Draw(cell,(startX,startY))        
        if(grid[i] == '1'):
            Draw(cell,(startX,startY)) 
            Draw(X_image,(startX+10,startY+10))
        if(grid[i] == '2'):
            Draw(cell,(startX,startY)) 
            Draw(O_image,(startX+10,startY+10))
        if(i==2 or i==5 or i==8):startY+=152

def Read_Data():
    return str(ArduinoUnoSerial.readline())[2:11],str(ArduinoUnoSerial.readline())[11:13]

def Print_Results(provera,P1text,P2text,draw,pos,drawPos):
    if(provera=="dr" or provera=="p1" or provera=="p2"):
        if(provera=="p1"):
            Draw(P1text,pos)
        if(provera=="p2"):
            Draw(P2text,pos)
        if(provera=="dr"):
            Draw(draw,drawPos)
#images
X = Image_Loader_Transformer("images/X.png",130,130)
O = Image_Loader_Transformer("images/O.png",130,130)
BG = Image_Loader_Transformer("images/background.png",480,480)
CELL = Image_Loader_Transformer("images/cell.png",150,150)
#fonts
title_Font = LoadFont('fonts/title.ttf',28)
main_Font = LoadFont('fonts/main_font.ttf',25)
#texts
naslov,naslovPos = Create_Text("Tic-Tac-Toe by Stefan",title_Font,"white",295,30)
player_1,player_1_pos = Create_Text("Player one won",title_Font,"white",295,600)
player_2,player_2_pos = Create_Text("Player two won",title_Font,"white",295,600)
nereseno,neresenoPos = Create_Text("Draw",title_Font,"white",300,600)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid,res=Read_Data()
    time.sleep(0.01)
    screen.fill(WINDOWS_BACKGROND_COLOR)

    Print_Results(res,player_1,player_2,nereseno,player_1_pos,neresenoPos)
    Draw_Table(CELL,X,O,70,70)
    Draw(BG,(55,55))
    Draw(naslov,naslovPos)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()