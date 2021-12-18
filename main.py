import tkinter as tk
temp=[]
l=[100,100]
from random import randrange
p1,p2=0,0
played=1
while played!=6:
	r1=randrange(100)
	l[1]-=r1
	r2=randrange(100)
	l[0]-=r2
	if(l[0]<1):
       		p2+=1
       		l=[100,100]
       		played+=1
       		temp.append([p1,p2])
	elif(l[1]<1):
        		p1+=1
        		l=[100,100]
        		played+=1
        		temp.append([p1,p2])
	if(p1>2):
        		break
	elif(p2>2):
        		break
class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        self.textfinal = tk.StringVar()
        self.textfinal1 = tk.StringVar()
        self.textfinal2 = tk.StringVar()
        self.label = tk.Label(self.root, textvariable=self.text)
        self.label1 = tk.Label(self.root, textvariable=self.text1)
        self.label2 = tk.Label(self.root, textvariable=self.text2)
        self.label3 = tk.Label(self.root, textvariable=self.text3)
        self.label4 = tk.Label(self.root, textvariable=self.text4)
        self.labelfinal = tk.Label(self.root, textvariable=self.textfinal)
        self.labelfinal1 = tk.Label(self.root, textvariable=self.textfinal1)
        self.labelfinal2 = tk.Label(self.root, textvariable=self.textfinal2)
        self.text.set("game 1 -player 1- Won 0 Player 2 won: 0")

        self.button = tk.Button(self.root,
                                text="Game1",
                                command=self.changeText)

        self.text1.set("game 2 -player 1- Won 0 Player 2 won: 0")

        self.button1 = tk.Button(self.root,
                                text="Game2",
                                command=self.changeText1)

        self.text2.set("game 3 -player 1- Won 0 Player 2 won: 0")   
        self.textfinal.set("")
        self.button2 = tk.Button(self.root,
                                text="Game3",
                                command=self.changeText2)

        self.text3.set("game 4 -player 1- Won 0 Player 2 won: 0")
        self.textfinal1.set("")
        self.button3 = tk.Button(self.root,
                                text="Game4",
                                command=self.changeText3)

        self.text4.set("game 5 -player 1- Won 0 Player 2 won: 0")
        self.textfinal2.set("")
        self.button4 = tk.Button(self.root,
                                text="Game5",
                                command=self.changeText4)
        self.button.pack()
        self.label.pack()
        self.button1.pack()
        self.label1.pack()
        self.button2.pack()
        self.label2.pack()
        self.labelfinal.pack()
        self.button3.pack()
        self.label3.pack()
        self.labelfinal1.pack()
        self.button4.pack()
        self.label4.pack()
        self.labelfinal2.pack()
        self.root.mainloop()

    def changeText(self):
        	self.text.set("game 1 -player 1- Won %d Player 2 won: %d"%(temp[0][0],temp[0][1]))
    def changeText1(self):
        self.text1.set("game 2 -player 1- Won %d Player 2 won: %d"%(temp[1][0],temp[1][1]))
    def changeText2(self):
        self.text2.set("game 3 -player 1- Won %d Player 2 won: %d"%(temp[2][0],temp[2][1]))
        if(temp[2][0]==3):
            self.textfinal.set("Player 1 won the match!")
        elif(temp[2][1]==3):
            self.textfinal.set("Player 2 won the match!")
    def changeText3(self):
        self.text3.set("game 4 -player 1- Won %d Player 2 won: %d"%(temp[3][0],temp[3][1]))
        if(temp[3][0]==3):
            self.textfinal1.set("Player 1 won the match!")
        elif(temp[3][1]==3):
            self.textfinal1.set("Player 2 won the match!")
    def changeText4(self):
        self.text4.set("game 5 -player 1- Won %d Player 2 won: %d"%(temp[4][0],temp[4][1]))
        if(temp[4][0]==3):
            self.textfinal2.set("Player 1 won the match!")
        elif(temp[4][1]==3):
            self.textfinal2.set("Player 2 won the match!")
app=Test()
