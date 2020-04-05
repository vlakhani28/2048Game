from tkinter import *
from tkinter.font import Font
import winsound
window =""
def click():
    global window
    winsound.PlaySound(None,winsound.SND_FILENAME)
    winsound.PlaySound("start.wav", winsound.SND_FILENAME)
    window.destroy()
    from maingame import main
    main()

def wi():
    global window
    window = Tk()
    window.geometry("280x300")
    window.title("Data")
    window.configure(bg="black")
    fonts = Font(family = "monospace",size = 20)
    Label(window, text="Instructions  ", bg="black", fg="blue", borderwidth=0,font = fonts).place(x=75, y=10)
    Label(window, text="1) Use Arrow Keys to move ", bg="black", fg="white", borderwidth=0).place(x=30, y=50)
    Label(window, text="2) Press R to Restart the Game ", bg="black", fg="white", borderwidth=0).place(x=30, y=80)
    Label(window, text="3) Press S to Save the Game ", bg="black", fg="white", borderwidth=0).place(x=30, y=120)
    Label(window, text="4) Press Q to Quit  the Game ", bg="black", fg="white", borderwidth=0).place(x=30, y=160)
    Label(window, text="5) Press L to Load the Game ", bg="black", fg="white", borderwidth=0).place(x=30, y=200)
    Label(window, text="6) Press U to Undo a Move ", bg="black", fg="white", borderwidth=0).place(x=30, y=240)
    Button(window, text='Lets Play..!!', width=10, bg='white', fg='black', command=click).place(x=95, y=270)
    winsound.PlaySound("music.wav",winsound.SND_LOOP|winsound.SND_FILENAME|winsound.SND_ASYNC)
    window.mainloop()