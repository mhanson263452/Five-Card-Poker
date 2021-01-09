# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:00:37 2021

@author: Michael Hanson
"""

import random as rand
import tkinter as ttk
from PIL import ImageTk, Image
from tkinter import font
    
#Creation of Deck
deck = []
suits = ["H","S","C","D"]
cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for y in suits:
    for x in cards:
        deck.append(x+y)

deckDict = {"AH" : "cards/PNG/AH.png", "AS" : "cards/PNG/AS.png", "AC" : "cards/PNG/AC.png",
            "AD" : "cards/PNG/AD.png", "2H" : "cards/PNG/2H.png", "2S" : "cards/PNG/2S.png",
            "2C" : "cards/PNG/2C.png", "2D" : "cards/PNG/2D.png", "3H" : "cards/PNG/3H.png",
            "3S" : "cards/PNG/3S.png", "3C" : "cards/PNG/3C.png", "3D" : "cards/PNG/3D.png",
            "4H" : "cards/PNG/4H.png", "4S" : "cards/PNG/4S.png", "4C" : "cards/PNG/4C.png",
            "4D" : "cards/PNG/4D.png", "5H" : "cards/PNG/5H.png", "5S" : "cards/PNG/5S.png",
            "5C" : "cards/PNG/5C.png", "5D" : "cards/PNG/5D.png", "6H" : "cards/PNG/6H.png",
            "6S" : "cards/PNG/6S.png", "6C" : "cards/PNG/6C.png", "6D" : "cards/PNG/6D.png",
            "7H" : "cards/PNG/7H.png", "7S" : "cards/PNG/7S.png", "7C" : "cards/PNG/7C.png",
            "7D" : "cards/PNG/7D.png", "8H" : "cards/PNG/8H.png", "8S" : "cards/PNG/8S.png",
            "8C" : "cards/PNG/8C.png", "8D" : "cards/PNG/8D.png", "9H" : "cards/PNG/9H.png",
            "9S" : "cards/PNG/9S.png", "9C" : "cards/PNG/9C.png", "9D" : "cards/PNG/9D.png",
            "10H": "cards/PNG/10H.png","10S":"cards/PNG/10S.png","10C": "cards/PNG/10C.png",
            "10D": "cards/PNG/10D.png", "JH" :"cards/PNG/JH.png", "JS" : "cards/PNG/JS.png",
            "JC" : "cards/PNG/JC.png", "JD" : "cards/PNG/JD.png", "QH" : "cards/PNG/QH.png",
            "QS" : "cards/PNG/QS.png", "QC" : "cards/PNG/QC.png", "QD" : "cards/PNG/QD.png",
            "KH" : "cards/PNG/KH.png", "KS" : "cards/PNG/KS.png", "KC" : "cards/PNG/KC.png",
            "KD" : "cards/PNG/KD.png", "backCard" : "cards/PNG/blue_back.png"}

creds = 100
playerChoice = "deal"

class fiveCardPoker:
    
    global deckDict
    global creds
    global deck
    global suits
    global cards
    global deadCards
    global hand
    global firstCards
    global firstHand
    global secondCardList
    global newPhoto
    global win
    global restart
    
    def __init__(self, root):
        
        root.title("Poker - Jacks High")
        
        self.mainframe = ttk.Frame(root, borderwidth = 5, padx = 12, pady = 12)
        self.mainframe.grid(column = 0, row = 0, sticky = (ttk.N, ttk.W, ttk.S, ttk.E))
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)
        
        self.newButton = []
        self.secondCardList = []
        self.creds = 100
        
        self.cardIm1 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardIm2 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardIm3 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardIm4 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardIm5 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        
        self.cardLabel1 = ttk.Label(self.mainframe, image = self.cardIm1)
        self.cardLabel1.grid(column = 1, row = 2, padx = 12)
        self.cardLabel2 = ttk.Label(self.mainframe, image = self.cardIm2)
        self.cardLabel2.grid(column = 2, row = 2, padx = 12)
        self.cardLabel3 = ttk.Label(self.mainframe, image = self.cardIm3)
        self.cardLabel3.grid(column = 3, row = 2, padx = 12)
        self.cardLabel4 = ttk.Label(self.mainframe, image = self.cardIm4)
        self.cardLabel4.grid(column = 4, row = 2, padx = 12)
        self.cardLabel5 = ttk.Label(self.mainframe, image = self.cardIm5)
        self.cardLabel5.grid(column = 5, row = 2, padx = 12)
        
        self.dealFont = font.Font(size = 14)
        self.dealButton1 = ttk.Button(self.mainframe, text = 'DEAL', font = self.dealFont, command = lambda: self.dealBut1(), width = 11, height = 2)
        self.dealButton1.grid(column = 5, row = 5, sticky = ttk.N)
         
        self.replaceButton1 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm1)
        self.replaceButton1.grid(column = 1, row = 3, sticky = ttk.N, pady = 4)
        self.replaceButton1_2 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm1_2)
        self.replaceButton1_2.grid_forget()
        self.replaceButton1['state'] = 'disabled'
        self.replaceButton1_2['state'] = 'disabled'
        
        self.replaceButton2 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm2)
        self.replaceButton2.grid(column = 2, row = 3, sticky = ttk.N, pady = 4)
        self.replaceButton2_2 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm2_2)
        self.replaceButton2_2.grid_forget()
        self.replaceButton2['state'] = 'disabled'
        self.replaceButton2_2['state'] = 'disabled'
        
        self.replaceButton3 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm3)
        self.replaceButton3.grid(column = 3, row = 3, sticky = ttk.N, pady = 4)
        self.replaceButton3_2 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm3_2)
        self.replaceButton3_2.grid_forget()
        self.replaceButton3['state'] = 'disabled'
        self.replaceButton3_2['state'] = 'disabled'
        
        self.replaceButton4 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm4)
        self.replaceButton4.grid(column = 4, row = 3, sticky = ttk.N, pady = 4)
        self.replaceButton4_2 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm4_2)
        self.replaceButton4_2.grid_forget()
        self.replaceButton4['state'] = 'disabled'
        self.replaceButton4_2['state'] = 'disabled'
        
        self.replaceButton5 = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm5)
        self.replaceButton5.grid(column = 5, row = 3, sticky = ttk.N, pady = 4)
        self.replaceButton5_2  = ttk.Button(self.mainframe, text = "Replace", width = 10, command = self.replaceComm5_2)
        self.replaceButton5_2.grid_forget()
        self.replaceButton5['state'] = 'disabled'
        self.replaceButton5_2['state'] = 'disabled'
        
        winningFont = font.Font(size = 18, weight = 'bold')
        self.winningLabel = ttk.Label(self.mainframe, text = "Press 'Deal' to Start", font = winningFont)
        self.winningLabel.grid(column = 3, row = 4, sticky = ttk.N, pady = 10)
        moneyFont = font.Font(size = 13)
        ttk.Label(self.mainframe, text = "Bet: 5", font = moneyFont).grid(column = 1, row = 4, sticky = (ttk.SW))
        self.credLabel = ttk.Label(self.mainframe, text = "Credits: " + str(self.creds), font = moneyFont)
        self.credLabel.grid(column = 1, row = 5, sticky = ttk.NW)
        
    def winningHand(self, hand, money):
        suit = []
        number = []
        win = "Sorry! Try Again."
        for i in hand:
            suit.append(i[-1])
            if len(i) == 3:
                number.append(i[0:2])
            else:
                number.append(i[0])
        for j in range(len(number)):
            if number[j] == 'J':
                number[j] = '11'
            if number[j] == "Q":
                number[j] = "12"
            if number[j] == "K":
                number[j] = '13'
            if number[j] == "A":
                number[j] = "14"
        for k in range(len(number)):
            number[k] = int(number[k])
        number.sort()
        
        #Royal Flush
        flushCount = 0
        if number == [10,11,12,13,14]:
            for a in range(len(suit)):
                if suit[0] == suit[a]:
                    flushCount = flushCount + 1
            if flushCount == 5:
                money = money + 4000
                win = "ROYAL FLUSH!!"
                
        #Straight Flush
        flushCount = 0
        straightCount = 0
        if win != "ROYAL FLUSH!!":
            for a in range(len(suit)):
                if suit[0] == suit[a]:
                    flushCount = flushCount + 1
            if flushCount == 5:
                if number == [2,3,4,5,14]:
                    money = money + 250
                    win = "Straight Flush!"
                else:
                    for b in range(len(number) - 1):
                        if (number[b+1]-number[b]) == 1:
                            straightCount = straightCount + 1
                    if straightCount == 4:
                        money = money + 250
                        win = "Straight Flush!"
        
        #4-of-a-Kind
        kindCount = 0
        n1 = number[0]
        for a in range(len(number)-1):
            if number[a+1] == n1:
                kindCount = kindCount + 1
            elif kindCount != 3:
                n1 = number[a+1]
                kindCount = 0
        if kindCount == 3:
            money = money + 125
            win = "4-of-a-Kind!"
            
        #Full House
        kindCount1 = 0
        kindCount2 = 0
        c1 = number[0]
        c2 = 0
        for a in range(len(number)-1):
            if number[a+1] == c1:
                kindCount1 = kindCount1 + 1
            else:
                c2 = number[a]
                if number[a+1] == c2:
                    kindCount2 = kindCount2 + 1
        if kindCount1 + kindCount2 == 3:
            if kindCount1 != 0 and kindCount2 != 0:
                money = money + 45
                win = "Full House!"
            
        #Flush
        flushCount = 0
        if win != "Straight Flush!":
            if win != "ROYAL FLUSH!!":
                for a in range(len(suit)):
                    if suit[0] == suit[a]:
                        flushCount = flushCount + 1
                if flushCount == 5:
                    money = money + 30
                    win = "Flush!"
            
        #Straight
        straightCount = 0
        if win != "Straight Flush!":
            if win != "ROYAL FLUSH!!":
                if number == [2,3,4,5,14]:
                    money = money + 20
                    win = "Straight!"
                else:
                    for a in range(len(number) - 1):
                        if (number[a+1]-number[a]) == 1:
                            straightCount = straightCount + 1
                    if straightCount == 4:
                        money = money + 20
                        win = "Straight!"
    
        #3-of-a-Kind
        kindCount = 0
        if win != "4-of-a-Kind!":
            if win != "Full House!":
                n2 = number[0]
                for b in range(len(number)-1):
                    if number[b+1] == n2:
                        kindCount = kindCount + 1
                    elif kindCount != 2:
                        n2 = number[b+1]
                        kindCount = 0
                if kindCount == 2:
                    money = money + 15
                    win = "3-of-a-Kind!"
                    
        #Two Pair
        kindCount3 = 0
        for c in range(len(number)-1):
            for d in range((len(number)-1)-c):
                if number[c] == number[d+c+1]:
                    kindCount3 = kindCount3 + 1
        if kindCount3 == 2:
            money = money + 10
            win = "Two Pair!"
            
        #Pair (Jack High)
        kindCount4 = 0
        if win != "Two Pair!":
            if win != "Full House!":
                if win != "3-of-a-Kind!":
                    if win != "4-of-a-Kind!":
                        for e in range(len(number)-1):
                            if number[e] > 10:
                                for f in range((len(number)-1)-e):
                                    if number[e] == number[f+e+1]:
                                        kindCount4 = kindCount4 + 1
                                    if kindCount4 == 1:
                                        money = money + 5
                                        win = "Jack High Pair!"
                        
        return win, money 
    
    def replaceComm1(self, *args):
        self.replaceCard1 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel1.configure(image = self.replaceCard1)
        self.secondCardList.append(0)
        self.replaceButton1.grid_forget()
        self.replaceButton1_2.grid(column = 1, row = 3, sticky = ttk.N, pady = 4)
       
        
    def replaceComm1_2(self, *args):
        self.replaceCard1_2 = ImageTk.PhotoImage(Image.open(deckDict[self.firstHand[0]]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel1.configure(image = self.replaceCard1_2)
        self.secondCardList.remove(0)
        self.replaceButton1_2.grid_forget()
        self.replaceButton1.grid(column = 1, row = 3, sticky = ttk.N, pady = 4)
        
    def replaceComm2(self, *args):
        self.replaceCard2 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel2.configure(image = self.replaceCard2)
        self.secondCardList.append(1)
        self.replaceButton2.grid_forget()
        self.replaceButton2_2.grid(column = 2, row = 3, sticky = ttk.N, pady = 4)
        
    def replaceComm2_2(self, *args):
        self.replaceCard2_2 = ImageTk.PhotoImage(Image.open(deckDict[self.firstHand[1]]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel2.configure(image = self.replaceCard2_2)
        self.secondCardList.remove(1)
        self.replaceButton2_2.grid_forget()
        self.replaceButton2.grid(column = 2, row = 3, sticky = ttk.N, pady = 4)
           
    def replaceComm3(self, *args):
        self.replaceCard3 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel3.configure(image = self.replaceCard3)
        self.secondCardList.append(2)
        self.replaceButton3.grid_forget()
        self.replaceButton3_2.grid(column = 3, row = 3, sticky = ttk.N, pady = 4)
        
    def replaceComm3_2(self, *args):
        self.replaceCard3_2 = ImageTk.PhotoImage(Image.open(deckDict[self.firstHand[2]]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel3.configure(image = self.replaceCard3_2)
        self.secondCardList.remove(2)
        self.replaceButton3_2.grid_forget()
        self.replaceButton3.grid(column = 3, row = 3, sticky = ttk.N, pady = 4)
            
    def replaceComm4(self, *args):
        self.replaceCard4 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel4.configure(image = self.replaceCard4)
        self.secondCardList.append(3)
        self.replaceButton4.grid_forget()
        self.replaceButton4_2.grid(column = 4, row = 3, sticky = ttk.N, pady = 4)
        
    def replaceComm4_2(self, *args):
        self.replaceCard4_2 = ImageTk.PhotoImage(Image.open(deckDict[self.firstHand[3]]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel4.configure(image = self.replaceCard4_2)
        self.secondCardList.remove(3)
        self.replaceButton4_2.grid_forget()
        self.replaceButton4.grid(column = 4, row = 3, sticky = ttk.N, pady = 4)
            
    def replaceComm5(self, *args):
        self.replaceCard5 = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel5.configure(image = self.replaceCard5)
        self.secondCardList.append(4)
        self.replaceButton5.grid_forget()
        self.replaceButton5_2.grid(column = 5, row = 3, sticky = ttk.N, pady = 4)
        
    def replaceComm5_2(self, *args):
        self.replaceCard5_2 = ImageTk.PhotoImage(Image.open(deckDict[self.firstHand[4]]).resize((230,352), Image.ANTIALIAS))
        self.cardLabel5.configure(image = self.replaceCard5_2)
        self.secondCardList.remove(4)
        self.replaceButton5_2.grid_forget()
        self.replaceButton5.grid(column = 5, row = 3, sticky = ttk.N, pady = 4)
        
    def firstDeal(self, *args):
        self.creds = self.creds - 5
        self.firstHand = rand.sample(deck, 5)
        card1 = self.firstHand[0]
        card2 = self.firstHand[1]
        card3 = self.firstHand[2]
        card4 = self.firstHand[3]
        card5 = self.firstHand[4]
        self.deadCards = [card1,card2,card3,card4,card5]
        self.cardFirst1 = ImageTk.PhotoImage(Image.open(deckDict[card1]).resize((230,352), Image.ANTIALIAS))
        self.cardFirst2 = ImageTk.PhotoImage(Image.open(deckDict[card2]).resize((230,352), Image.ANTIALIAS))
        self.cardFirst3 = ImageTk.PhotoImage(Image.open(deckDict[card3]).resize((230,352), Image.ANTIALIAS))
        self.cardFirst4 = ImageTk.PhotoImage(Image.open(deckDict[card4]).resize((230,352), Image.ANTIALIAS))
        self.cardFirst5 = ImageTk.PhotoImage(Image.open(deckDict[card5]).resize((230,352), Image.ANTIALIAS))
        return self.cardFirst1, self.cardFirst2, self.cardFirst3, self.cardFirst4, self.cardFirst5
    
    def dealBut1(self, *args):
        global newButton
        self.hand = self.firstDeal()
        self.cardLabel1.configure(image = self.hand[0])
        self.cardLabel2.configure(image = self.hand[1])
        self.cardLabel3.configure(image = self.hand[2])
        self.cardLabel4.configure(image = self.hand[3])
        self.cardLabel5.configure(image = self.hand[4])
        self.winningLabel.configure(text = "")
        self.firstCards = [self.cardLabel1, self.cardLabel2, self.cardLabel3, self.cardLabel4, self.cardLabel5]
       
        self.replaceButton1['state'] = 'normal'
        self.replaceButton2['state'] = 'normal'
        self.replaceButton3['state'] = 'normal'
        self.replaceButton4['state'] = 'normal'
        self.replaceButton5['state'] = 'normal'
        self.replaceButton1_2['state'] = 'normal'
        self.replaceButton2_2['state'] = 'normal'
        self.replaceButton3_2['state'] = 'normal'
        self.replaceButton4_2['state'] = 'normal'
        self.replaceButton5_2['state'] = 'normal'
        
        self.credLabel.configure(text = "Credits: " + str(self.creds))
        
        self.dealButton1.destroy()
        self.newButton.append([ttk.Button(self.mainframe, text = 'DEAL', font = self.dealFont, command = lambda: self.dealBut2(), width = 11, height = 2).grid(column = 5, row = 5, sticky = ttk.N)])
        
    def dealBut2(self, *args):
        self.newButton = []
        for a in range(len(self.secondCardList)):
            newCard = rand.choice([i for i in deck if i not in self.deadCards])
            self.firstHand[self.secondCardList[a]] = newCard
            self.newPhoto = ImageTk.PhotoImage(Image.open(deckDict[newCard]).resize((230,352), Image.ANTIALIAS))
            self.firstCards[self.secondCardList[a]].image = self.newPhoto
            self.firstCards[self.secondCardList[a]].configure(image = self.newPhoto)
            self.deadCards.append(newCard)
             
        self.replaceButton1['state'] = 'disabled'
        self.replaceButton2['state'] = 'disabled'
        self.replaceButton3['state'] = 'disabled'
        self.replaceButton4['state'] = 'disabled'
        self.replaceButton5['state'] = 'disabled'
        self.replaceButton1_2['state'] = 'disabled'
        self.replaceButton2_2['state'] = 'disabled'
        self.replaceButton3_2['state'] = 'disabled'
        self.replaceButton4_2['state'] = 'disabled'
        self.replaceButton5_2['state'] = 'disabled'
            
        self.end = self.winningHand(self.firstHand, self.creds)
        self.win = self.end[0]
        self.winningLabel.configure(text = self.win)
        self.creds = self.end[1]
        self.credLabel.configure(text = "Credits: " + str(self.creds))
        self.betButton = ttk.Button(self.mainframe, text = 'BET', font = self.dealFont, command = lambda: self.dealBut3(), width = 11, height = 2)
        self.betButton.grid(column = 5, row = 5, sticky = ttk.N)
        
        if self.creds == 0:
            self.winningLabel.configure(text = "Game Over")
            self.betButton['state'] = 'disabled'

        
        
    def dealBut3(self, *args):
        self.cardRestart = ImageTk.PhotoImage(Image.open(deckDict["backCard"]).resize((230,352), Image.ANTIALIAS))

        for i in range(5):
            self.firstCards[i].image = self.cardRestart
            self.firstCards[i].configure(image = self.cardRestart)
            
        self.winningLabel.configure(text = "")
        self.deadCards = []
        self.newButton.append([ttk.Button(self.mainframe, text = 'DEAL', font = self.dealFont, command = lambda: self.dealBut1(), width = 11, height = 2).grid(column = 5, row = 5, sticky = ttk.N)])
        self.secondCardList = []
        
        self.replaceButton1_2.grid_forget()
        self.replaceButton1.grid(column = 1, row = 3, sticky = ttk.N, pady = 4)
        
        self.replaceButton2_2.grid_forget()
        self.replaceButton2.grid(column = 2, row = 3, sticky = ttk.N, pady = 4)
        
        self.replaceButton3_2.grid_forget()
        self.replaceButton3.grid(column = 3, row = 3, sticky = ttk.N, pady = 4)
        
        self.replaceButton4_2.grid_forget()
        self.replaceButton4.grid(column = 4, row = 3, sticky = ttk.N, pady = 4)
        
        self.replaceButton5_2.grid_forget()
        self.replaceButton5.grid(column = 5, row = 3, sticky = ttk.N, pady = 4)

      
root = ttk.Tk()
fiveCardPoker(root)
root.mainloop()


"""
    #Selecting cards to keep
    print("Credits: " + str(creds))
    cardsKeep = "NA"
    cardsKeep = input("Enter Cards Replace (Leave blank to replace none): ")
    end = 0
    while True:
        correctionList = []
        for a in range(len(cardsKeep)):
            correctionList.append(cardsKeep[a])
        if all(x in ["1","2","3","4","5"] for x in correctionList) == False:
            cardsKeep = input("Please only type 1 through 5 with no spaces: ")
        else:
            break
    
            MONUMENT TO FAILURE
            for b in range(len(correctionList)):
                if cardsKeep[a].isnumeric() == True:
                    newCard = int(cardsKeep[a])
                    if newCard != 1:
                        print("Logic Error 1!" + " " + str(a+1))
                        cardsKeep = input("Please only type 1 through 5 with no spaces: ")
                    elif newCard != 2:
                        print("Logic Error 2!" + " " + str(a+1))
                        cardsKeep = input("Please only type 1 through 5 with no spaces: ")
                    elif newCard != 3:
                        print("Logic Error 3!" + " " + str(a+1))
                        cardsKeep = input("Please only type 1 through 5 with no spaces: ")
                    elif newCard != 4:
                        print("Logic Error 4!" + " " + str(a+1))
                        cardsKeep = input("Please only type 1 through 5 with no spaces: ")
                    elif newCard != 5:
                        print("Logic Error 5!" + " " + str(a+1))
                        cardsKeep = input("Please only type 1 through 5 with no spaces: ")
                    else:
                        end = end + 1
            else:
                print("It's the int statement!")
                cardsKeep = input("Please only type 1 through 5 with no spaces: ")
"""





