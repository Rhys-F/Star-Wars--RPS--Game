#Rock, Paper, Scissors Star Wars edition

from tkinter import *
import random
import pygame
from pygame.locals import *
pygame.init()
#add music to the background and program
pygame.mixer.music.load("Star Wars Theme Song By John Williams.mp3")
pygame.mixer.music.play(-1,0.0)




weapons = ("Luke SkyWalker", "Darth Vader", "Obi Wan")
#class application (processing)
class Application(Frame):
    #creating screen, functions and text
    def __init__(self, master):


        fname = Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Choose your character!\n"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Characters:"
              ).grid(row = 1, column = 0, sticky = W)
        Label(self,
              text = "Battle!"
              ).grid(row = 0, column = 3, sticky = W)
        self.weapon = StringVar()
        column = 1

        #set character choices
        Radiobutton(self,
                    text = "Luke SkyWalker",
                    variable = self.weapon,
                    value = "Luke SkyWalker"
                    ).grid(row = 1, column = column, sticky = W)
        Radiobutton(self,
                    text = "Darth Vader",
                    variable = self.weapon,
                    value = "Darth Vader"
                    ).grid(row = 2, column =+ 1, sticky = W)
        Radiobutton(self,
                    text = "Obi Wan",
                    variable = self.weapon,
                    value = "Obi Wan"
                    ).grid(row = 3, column =+ 1, sticky = W)
        #Button to activate processing
        Button(self,
               text = "Choose your weapon!", image = photo1,
               command = self.fight,
               ).grid(row = 1, column = 3, columnspan = 4, rowspan = 3, sticky = W)
         

        self.outcome_txt = Text(self, width = 50, height = 2, wrap = WORD)
        self.outcome_txt.grid(row = 7, column = 0, columnspan = 4)
    #computer randomizing choice(processing)

    def comp_choice(self):
        comp_throw = random.randrange(len(weapons))
        opponent = weapons[comp_throw]  #index for the random #
        return opponent #need to return opponent
    def fight(self):
        weapon = self.weapon.get()
        op = self.comp_choice()
        #user input/processing/output result of the game
        if weapon == op:
            outcome = "The computer chose: " + op + " - You tied, play again!"
        elif weapon == "Darth Vader" and op == "Obi Wan" or \
             weapon == "Luke SkyWalker" and op == "Darth Vader" or \
             weapon == "Obi Wan" and op == "Luke SkyWalker":
            outcome = "The computer chose: " + op + " - You won!"
        elif weapon == "Luke SkyWalker" and op == "Obi Wan" or \
             weapon == "Obi Wan" and op == "Darth Vader" or \
             weapon == "Darth Vader" and op == "Luke SkyWalker":
            outcome = "The computer chose: " + op + " - You lose! :("
        else: outcome = "You didn't chose a character!"
        self.outcome_txt.delete(0.0, END)
        self.outcome_txt.insert(0.0, outcome)
#output title/processing reruning the game
root = Tk()
root.title("Rock, Paper, Star Wars! Feat: Luke, Vader, Obi Wan")
#add photos input
photo = PhotoImage(file="star-wars-animated-gif-32.gif")
label = Label(root, image=photo)
label.grid(row = 6, column = 0, columnspan = 2)
photo1 = PhotoImage(file="output_r5sGEC.gif", height = 100, width = 130)
#output excute program
app = Application(root)
root.mainloop()
