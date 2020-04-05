from tkinter import *
from PIL import Image, ImageTk
import winsound
window = ""
fname = ""
lname = ""
scale = ""
fn = ""
ln = ""
age = ""
def click():
    global window,fn,ln,age
    fn = fname.get()
    ln = lname.get()
    age = scale.get()
    window.destroy()
    from rules import wi
    wi()
def entry_data():
    global fname,lname,scale
    global window
    window = Tk()
    window.geometry("280x300")
    window.title("Data")
    window.configure(bg="black")
    img = ImageTk.PhotoImage(Image.open("download.png"))
    Label(window, image=img, bg="black", borderwidth=0).place(x=95, y=10)
    Label(window, text="First Name ", bg="black", fg="blue", borderwidth=0).place(x=30, y=120)
    fname = Entry(window, bg="white", fg="blue", borderwidth=0)
    fname.place(x=125, y=120)
    Label(window, text="Last Name ", bg="black", fg="blue", borderwidth=0).place(x=30, y=170)
    lname = Entry(window, bg="white", fg="blue", borderwidth=0)
    lname.place(x=125, y=170)
    Label(window, text="Age ", bg="black", fg="blue", borderwidth=0).place(x=30, y=220)
    a = IntVar()
    scale = Scale(window, variable=a, from_=1, to=100, orient=HORIZONTAL, bg="black", fg="yellow", borderwidth=0,
              highlightthickness=0)
    scale.place(x=125, y=200)
    Button(window, text='Next..!!', width=10, bg='white', fg='black', command=click).place(x=95, y=270)
    winsound.PlaySound("music.wav",winsound.SND_LOOP|winsound.SND_FILENAME|winsound.SND_ASYNC)
    window.mainloop()
