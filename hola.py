from tkinter import *
#from PIL import ImageTk, Image
from tkinter import ttk

u =Tk()
u.geometry("500x500")
u.title("niggaballsinn")
u.configure(background="lightgreen")
#mp = ImageTk.PhotoImage(Image.open("mercury.jpg"))
#vp = ImageTk.PhotoImage(Image.open("venus.jpg"))
#ep = ImageTk.PhotoImage(Image.open("earth.jpg"))

#E = ImageTk.PhotoImage(Image.open ("earth.jpg"))
lp = Label(u, text="Planeta:", bg="lightcoral")
lpn = Label(u, font=("cuirier",18,"bold"),bg="green")
lpi = Label(u,bg="gold2")
lpgr = Label(u, font=("castellar"))
lpin = Label(u,font=("courier",10,"bold"))

pl = ["mercurio","venus","tierra"]
selv = StringVar()
dropdown = ttk.Combobox(u, values = pl, textvariable=selv)


lp.place(relx=0.5, rely=0.2, anchor=CENTER)
lpn.place(relx=0.5, rely=0.3, anchor=CENTER)
lpi.place(relx=0.5, rely=0.4, anchor=CENTER)
lpgr.place(relx=0.5, rely=0.5, anchor=CENTER)
lpin.place(relx=0.5, rely=0.6, anchor=CENTER)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
u.mainloop()