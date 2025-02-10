import pygame
import BLTEST
import threading
import random
import time
import os
import tkinter
pygame.init()

width=1000
run=True
heigth=650
j=0
pygame.display.set_caption("SNAKE")
screen=pygame.display.set_mode((width, heigth))
"""os.chdir("\\")
os.chdir("Users/dell/SNAKE")"""
background_image=pygame.image.load("SNAKE.png")
background_image= pygame.transform.scale(background_image, (width, heigth))
screen.blit(background_image, (0, 0))
pygame.display.flip()
class Serpent:
        global j
        global balle
        balle=BLTEST.Balle() 
        global touche  
        def __init__(self, x, y):
            self.points=0
            self.coordonnees=[[x, y]]
            self.taille=3
            self.touche="d"
            self.color=(45, 200, 45)
            self.sizex=30
            self.sizey=30
            self.espacement=3
            self.background_image=pygame.image.load("SNAKE.png")
            self.background_image= pygame.transform.scale(self.background_image, (width, heigth))
        

        def verification_touches(self):
            global run
            try:
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            pygame.mixer.quit()
                            run=False
                            break
                        elif event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_RIGHT:
                                self.touche="d"
                                #self.espacement=random.randint(0, 0)
                            elif event.key==pygame.K_DOWN:
                                self.touche="s"
                                #self.espacement=random.randint(0, 0)
                            elif event.key==pygame.K_LEFT:
                                self.touche="q"
                                #self.espacement=random.randint(0, 0)
                            elif event.key==pygame.K_UP:
                                self.touche="z"
                                #self.espacement=random.randint(0, 0)
                            elif event.key==pygame.K_p:
                                self.touche="p"                  
            except:
                pass

        def verification_taille(self):
            try:
                if len(self.coordonnees)>self.taille:
                    #screen.fill((0, 0, 0))
                    screen.blit(self.background_image, (0, 0))
                    pygame.display.flip()  
                    self.coordonnees.pop(0)
            except:
                pass


        def verification_point(self):
            global balle
            rectangle=pygame.Rect(self.coordonnees[-1][0], self.coordonnees[-1][1], self.sizex, self.sizey)
            cercle=pygame.Rect((balle.position[0]-balle.rayon),(balle.position[1]-balle.rayon), self.sizex, self.sizey)
            if rectangle.colliderect(cercle):
                self.points=self.points+1
                balle.changement()
                self.taille=self.taille+1
                """self.sizex=self.sizex+1
                self.sizey=self.sizey+1
                balle.rayon=balle.rayon+1"""
                balle.color=(random.randint(200, 255), random.randint(100, 150), random.randint(0, 100))
                self.color=(random.randint(0, 100), random.randint(0, 255), random.randint(200, 255) )
            rectangle=pygame.Rect(self.coordonnees[-1][0], self.coordonnees[-1][1], self.sizex, self.sizey)
            cercle=pygame.Rect((balle.position[0]+balle.rayon),(balle.position[1]+balle.rayon), self.sizex, self.sizey)
            if rectangle.colliderect(cercle):
                self.points=self.points+1
                balle.changement()
                self.taille=self.taille+1
                """self.sizex=self.sizex+1
                self.sizey=self.sizey+1
                balle.rayon=balle.rayon+1"""
                balle.color=(random.randint(200, 255), random.randint(100, 150), random.randint(0, 100))
                self.color=(random.randint(0, 100), random.randint(0, 255), random.randint(200, 255) )

        def verification_sortie(self):
            global j
            global run
            if self.coordonnees[j][0]>=width:
                run=False
            elif self.coordonnees[j][1]>=heigth:
                run=False
            elif self.coordonnees[j][0]<=0:
                run=False
            if self.coordonnees[j][1]<=0:
                (self.points)
                run=False

        def verification_se_manger(self):
            global j
            global run
            if len(set(map(tuple, self.coordonnees)))!=len(self.coordonnees):
                run=False

        def move(self):
            global j
            global run
            try:

                if self.touche=="d":
                    j=0
                    while j<len(self.coordonnees):
                        
                        pygame.draw.rect(screen, self.color, (self.coordonnees[j][0], self.coordonnees[j][1], self.sizex, self.sizey))
                        balle.representation()
                        pygame.display.flip()
                        j=j+1
                    j=j-1   
                    self.coordonnees.append([self.coordonnees[j][0]+self.sizex+self.espacement, self.coordonnees[j][1]])  

                if self.touche=="s":
                    j=0
                    while j<len(self.coordonnees):
                        pygame.draw.rect(screen, self.color, (self.coordonnees[j][0], self.coordonnees[j][1], self.sizex, self.sizey))
                        balle.representation()
                        pygame.display.flip()
                        j=j+1
                    j=j-1
                    self.coordonnees.append([self.coordonnees[j][0], self.coordonnees[j][1]+self.sizey+self.espacement])
                        
                if self.touche=="q":
                    j=0
                    while j<len(self.coordonnees):        
                        pygame.draw.rect(screen, self.color, (self.coordonnees[j][0], self.coordonnees[j][1], self.sizex, self.sizey))
                        balle.representation()
                        pygame.display.flip()
                        j=j+1
                    j=j-1
                    self.coordonnees.append([self.coordonnees[j][0]-self.sizex-self.espacement, self.coordonnees[j][1]])

                if self.touche=="z":
                    j=0
                    while j<len(self.coordonnees):        
                        pygame.draw.rect(screen, self.color, (self.coordonnees[j][0], self.coordonnees[j][1], self.sizex, self.sizey))
                        balle.representation()
                        pygame.display.flip()  
                        j=j+1
                    j=j-1
                    self.coordonnees.append([self.coordonnees[j][0], self.coordonnees[j][1]-self.sizey-self.espacement])
                time.sleep(0.1)

                if self.touche=="p":
                    pass
                           
            except:
                pass             

        def game(self):
            global j
            global balle
            balle=BLTEST.Balle()
            global run
            run=True
            while run:
                th1=threading.Thread(target=self.verification_touches())
                th2=threading.Thread(target=self.verification_point())
                th3=threading.Thread(target=self.verification_taille())
                th4=threading.Thread(target=self.move())
                th5=threading.Thread(target=self.verification_sortie())
                th6=threading.Thread(target=self.verification_se_manger())
                #th7=threading.Thread(target=self.verification_pause())

                th1.start()
                th2.start()
                th3.start()
                th4.start()
                th5.start()
                th6.start()
                #th7.start()

                th1.join()
                th2.join()
                th3.join()
                th4.join()
                th5.join()
                th6.join()
                #th7.join()
                




    
    