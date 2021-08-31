from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

p1 = StringVar()
p2 = StringVar()
p1.set(0)
p2.set(0)
ptr1=0
ptr2=0

bclick = True
flag = 1

move=StringVar()
move.set("X's turn - Tap to play")
def playe1Move():
	move.set("X's turn - Tap to play")
def playe2Move():
	move.set("O's turn - Tap to play")
	
label = Label( tk, textvariable=move, font='Times 13 bold', bg='white', fg='black')
label.grid(row=3, column=0,columnspan=3)

def activeButton():
    global flag
    flag=1
    button1.configure(state=ACTIVE,text=" ")
    button2.configure(state=ACTIVE,text=" ")
    button3.configure(state=ACTIVE,text=" ")
    button4.configure(state=ACTIVE,text=" ")
    button5.configure(state=ACTIVE,text=" ")
    button6.configure(state=ACTIVE,text=" ")
    button7.configure(state=ACTIVE,text=" ")
    button8.configure(state=ACTIVE,text=" ")
    button9.configure(state=ACTIVE,text=" ")

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


#def clearButton():
#
#    activeButton()
#    button1["text"]=" "
#    button2["text"]=" "
#    button3["text"]=" "
#    button4["text"]=" "
#    button5["text"]=" "
#    button6["text"]=" "
#    button7["text"]=" "
#    button8["text"]=" "
#    button9["text"]=" "

def btnClick(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick == True:
        playe2Move()
        buttons["text"] = "X"
        bclick = False
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        playe1Move()
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    global ptr1,ptr2,flag
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 1 win!")
        ptr1+=1
        p1.set(ptr1)
        flag=0
        disableButton()
      

    elif(flag == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        flag=0
        disableButton()
       

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 2 win!")
        ptr2+=1
        p2.set(ptr2)
        flag=0
        disableButton()

label = Label( tk, text="Player 1:", font='Times 21 bold', bg='white', fg='black')
label.grid(row=1, column=0,columnspan=2)


label = Label( tk, text="Player 2:", font='Times 21 bold', bg='white', fg='black')
label.grid(row=2, column=0,columnspan=2)
#
player1_name = Entry(tk, textvariable=p1,width=5,font=("arial",15,"italic"),state=DISABLED)
player1_name.grid(row=1, column=2)
player2_name = Entry(tk, textvariable=p2, width=5,font=("arial",15,"italic"),state=DISABLED)
player2_name.grid(row=2, column=2)


button1 = Button(tk, text=" ", font='Times 9 bold', bg='red', fg='white', height=4, width=5, bd=10,command=lambda: btnClick(button1))
button1.grid(row=4, column=0)

button2 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button2))
button2.grid(row=4, column=1)

button3 = Button(tk, text=' ',font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button3))
button3.grid(row=4, column=2)

button4 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button4))
button4.grid(row=5, column=0)

button5 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button5))
button5.grid(row=5, column=1)

button6 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button6))
button6.grid(row=5, column=2)

button7 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button7))
button7.grid(row=6, column=0)

button8 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button8))
button8.grid(row=6, column=1)

button9 = Button(tk, text=' ', font='Times 9 bold', bg='red', fg='white', height=4, width=5,bd=10, command=lambda: btnClick(button9))
button9.grid(row=6, column=2)

button=Button(tk, text="New Game",width=10,height=2,bg='blue', fg="white",command=lambda: activeButton())
button.grid(row=7,column=0,columnspan=3)

tk.mainloop()