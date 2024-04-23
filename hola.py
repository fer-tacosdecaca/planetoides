from tkinter import *
from PIL import ImageTk, Image

u =Tk()
u.geometry("500x500")
u.title("niggaballsinn")
u.configure(background="lightgreen")


E = ImageTk.PhotoImage(Image.open ("earth.jpg"))
lp = Label(u, text="Planeta:", bg="lightcoral")
lpn = Label(u, font=("cuirier",18,"bold"),bg="lightcream")
lpi = Label(u,bg="gold2")
lpgr = Label(u, font=("castellar"))
lpin = Label(u,font=("courier",10,"bold"))

u.mainloop()