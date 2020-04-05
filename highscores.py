from tkinter import *
from store import displaydata
from tkinter.font import Font
def high():
    root = Tk()
    root.geometry("300x300")
    root.configure(bg = "black")
    fonts = Font(family="monospace", size=20)
    fonts1 = Font(family="monospace",size = 10)
    Label(root,text ="High Scores",fg = "blue" , bg = "black",font = fonts).place(x=70,y = 10)
    Label(root,text ="Played On",fg = "blue",bg = "black",font = fonts1).place(x=10,y = 50)
    Label(root,text ="Name",fg = "blue",bg = "black",font = fonts1).place(x=150,y = 50)
    Label(root,text ="Score",fg = "blue",bg = "black",font = fonts1).place(x=250,y = 50)
    x = displaydata()
    y1 = 100
    for i in range(0, len(x)):
        test = x[i]
        Label(root, text=test[4], fg="blue", bg="black", font=fonts1).place(x=10, y=y1)
        Label(root, text=test[0], fg="blue", bg="black", font=fonts1).place(x=150, y=y1)
        Label(root, text=test[3], fg="blue", bg="black", font=fonts1).place(x=250, y=y1)
        y1 +=30

    root.mainloop()