#Ce fichier contient un jeu fait entierement en python
# Le joueur doit se servir des touches "DOWN" "LEFT" "RIGHT" "UP" pour diriger un serpent dan le but de manger la pomme

import SPTEST
import pygame
from tkinter import *
import threading
import os

pygame.init()
pygame.mixer.init()
width=1000
heigth=650
global jeu
pygame.display.set_caption("SNAKE")
screen=pygame.display.set_mode((width, heigth))

"""os.chdir("\\")
os.chdir("Users/dell/SNAKE")"""
background_image=pygame.image.load("SNAKE.png")
background_image= pygame.transform.scale(background_image, (width, heigth))
screen.blit(background_image, (0, 0))
pygame.display.flip()
pygame.mixer.music.load("MUZIQUE_SNAKE.mp3")
pygame.mixer.music.play(-1)
if "RECORD.txt" in os.listdir():
    with open("RECORD.txt", "r") as fic:
        record=fic.read()
else:
    with open("RECORD.txt", "w") as fic:
        fic.write("0")


run=True
while run:
    global jeu
    jeu=True
    if jeu==True:
        serpent=SPTEST.Serpent(30, 30)
        serpent.game()
        fenetre=Tk()
        fenetre.title("SNAKE")
        fenetre.config(bg="black")
        fenetre.geometry("1080x720")
        fenetre.minsize(1080,720)
        fenetre.maxsize(1080,720)
        if int(record)>=serpent.points:
            score="SCORE : "+str(serpent.points)
        else:
            score="NOUVEAU RECORD : "+str(serpent.points)
            with open("RECORD.txt", "w") as  fic:
                fic.write(str(serpent.points))          
        lancement=Label(fenetre, text=score, font=("Courrier",30), bg="black", fg="green")
        lancement.pack(expand=YES)
        fenetre.mainloop()
    
    try:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                pygame.quit()
                pygame.mixer.quit()         
    except:
        run=False  
    

