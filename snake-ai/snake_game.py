#! /usr/bin/env python
############################################################################
# Purpose : A very small,basic and my first game
# Usages : Learning purpose
# Start date : 12/04/2011
# End date : 14/04/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Version : 0.0.1
# Modification history : No modification yet
############################################################################

#from dataaa import fileClass
import threading  
import pygame
from  pygame.locals import *
from sys import exit
from random import randint
'''
def xandy():
  threading.Timer(.000001, xandy).start()
  print(snakexy)
  with open("snakeData.txt", "a") as fil:
    fil.write(xandy())
    fil.close()
'''
while True:
 up=1
 down=2
 right=3
 left=4
 step=20
 block=[20,20]
 x=randint(1,20)
 y=randint(2,22)
 applexy=[]
 snakexy=[int(x*20),int(y*20)]
 snakelist=[[x*20,y*20],[(x-20)*20,(y*20)]]
 apple=0
 dead=0
 grow=0
 direction=right
 score=0
 start=0
 
 #xandy()
 
 pygame.init()
 screen=pygame.display.set_mode((640,480),0,24)
 caption=pygame.display.set_caption("Hungry Snake")
 f=pygame.font.SysFont("comicsansms",50)
 text1=f.render("Hungry Snake",True,(0,255,0))
 clock=pygame.time.Clock()
 start=pygame.font.SysFont("comicsansms",30)
 text2=start.render("Press s to start",True,(0,255,0))
 q=pygame.font.SysFont("comicsansms",30)
 text3=q.render("Press esc to quit",True,(0,255,0))
 s=[[300,200],[280,200],[260,200],[240,200],[220,200],[200,200],[180,200],[180,220],[160,220],[140,220],[120,220],[120,240],[100,240]]
 a=[100,240]
 pygame.draw.rect(screen,(255,0,0),Rect(a,block),0)
 screen.blit(text1,(60,60))
 screen.blit(text2,(300,300))
 screen.blit(text3,(300,350))
 for i in s:
  pygame.draw.rect(screen,(0,255,0),Rect(i,block),0)
  pygame.display.flip()
  clock.tick(10)
 pygame.display.flip()


 while True:
  for i in pygame.event.get():
   if i.type==QUIT:
    exit()
  pressed=pygame.key.get_pressed()
  if pressed[K_q]:
   exit()
  if pressed[K_s]:
   break

 while not dead:
  for i in pygame.event.get():
   if i.type==QUIT:
    exit()
    
  pressed=pygame.key.get_pressed()
  if pressed[K_LEFT] and direction!=right:
    direction=left
    '''print("Left")
    with open("snakeData.txt", "a") as fil:
      fil.write("left\n")
      fil.close()'''

  elif pressed[K_RIGHT] and direction!=left:
    direction=right
    '''print("Right")
    with open("snakeData.txt", "a") as fil:
      fil.write("right\n")
      fil.close()'''

  elif pressed[K_UP] and direction!=down:
    direction=up
    '''print("Forward")
    with open("snakeData.txt", "a") as fil:
      fil.write("forward\n")
      fil.close()'''

  elif pressed[K_DOWN] and direction!=up:
    direction=down
    '''print("Down")
    with open("snakeData.txt", "a") as fil:
      fil.write("down\n")
      fil.close()'''

  if direction==right:
   snakexy[0]=snakexy[0]+step
   if snakexy[0]>620:
    dead=1

  elif direction==left:
   snakexy[0]=snakexy[0]-step
   if snakexy[0]<20:
    dead=1

  elif direction==up:
   snakexy[1]=snakexy[1]-step
   if snakexy[1]<20:
    dead=1

  elif direction==down:
   snakexy[1]=snakexy[1]+step
   if snakexy[1]>460:
    dead=1

  # gives the positive x and negative x a variable to print and write to individual x coordinates
  snakex1 = (snakexy[0] + 1)
  snakex2 = (snakexy[0] - 1)

  #this whole bit is the data gathering code. determines which way the snake is going, prints it, converts it to string, opens the txt file writes it with a comma
  #(convienience), and then closes the file.

  if (snakexy[0] + 1) or (snakexy[0] - 1):# or (snakexy[1] + 1) or (snakexy[1] - 1):    
    print(snakex1)
    snakex1 = str(snakex1)
    with open("snakeDataX+.txt", "a") as fil:
      fil.write(snakex1)      
      fil.write(",")
      fil.close()

  if (snakexy[0] - 1):
    print(snakex2)
    snakex2 = str(snakex2)
    with open("snakeDataX-.txt", "a") as fil:
      fil.write(snakex2)
      fil.write(",")
      fil.close()

  # y values in different variables (positive and negative)
  snakey1 = (snakexy[1] + 1)
  snakey2 = (snakexy[1] - 1)

  if (snakexy[1] + 1):
    print(snakey1)
    snakey1 = str(snakey1)
    with open("snakeDataY+.txt", "a") as fil:
      fil.write(snakey1)
      fil.write(",")
      fil.close()  

  if (snakexy[1] - 1):
    print(snakey2)
    snakey2 = str(snakey2)
    with open("snakeDataY-.txt", "a") as fil:
      fil.write(snakey2)
      fil.write(",")
      fil.close()

  #does the same as above, but writes the apple's coordinates instead.
  #apple isn't in motion, so there's only 1 coordinate for every time it's eaten

  axy = str(applexy)
  #axy = str.strip(axy).strip("[]")
  print("apple: " + axy)
  with open("appleData.txt", "a") as fil:
    fil.write(" \n")
    fil.write(axy)
    fil.close()

  if snakelist.count(snakexy)>0:
   dead=1
  if apple==0:
   x1=randint(1,31)
   y1=randint(2,22)
   applexy=[int(x1*step),int(y1*step)]
   apple=1

  snakelist.insert(0,list(snakexy))
  if snakexy[0]==applexy[0] and snakexy[1]==applexy[1]:
   apple=0
   score=score+1
   print(score)
   '''with open("snakeData.txt", "a") as fil:
     fil.write("Score :" + str(score) + "\n")
     fil.close()'''
  else:
   snakelist.pop()

  screen.fill((0,0,0))
  scr=pygame.font.SysFont("comicsansms",20)
  text4=scr.render("Score : %d"%score,True,(0,255,0))
  screen.blit(text4,(500,10))
  pygame.draw.rect(screen,(255,0,0),Rect(applexy,block),0)
  for i in snakelist:
   pygame.draw.rect(screen,(0,255,0),Rect(i,block))
  pygame.display.flip()
  clock.tick(10)

 if dead==1:
  screen.fill((0,0,0))
  over=pygame.font.SysFont("comicsansms",40)
  text5=over.render("GAME OVER",True,(0,255,0))
  screen.blit(text5,(50,50))
  screen.blit(text4,(200,200))
  pygame.display.flip()
  '''with open("snakeData.txt", "a") as fil:
      fil.write("\nalive'nt\n----------------------------------------------\n")
      fil.close()'''
  while True:
   for i in pygame.event.get():
    if i.type==QUIT:
     exit()
   pressed=pygame.key.get_pressed()
   if pressed[K_ESCAPE]:
    exit()
   if pressed[K_s]:
    break

