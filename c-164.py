# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:20:23 2023

@author: User
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("planet Encyclopedia")
root.geometry("500x500")
root.configure(background = "lightblue")

mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
earth = ImageTk.PhotoImage(Image.open("earth.jpg"))


label_planet = Label(root, text ="planet :", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"),bg="lightblue")
label_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue",wraplength=500)

planets = ["mercury","venus","earth"]
selectdval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectdval)
            
def planetInfo():
    planet = selectdval.get()
    if planet =="mercury":
        label_planet_name['text'] = "mercury"
        label_planet_image['image'] = mercury
        label_planet_gravity_radius['text'] = "gravity : 3.7 m/s \n radius : 2,439.7 km"
        label_planet_info['text'] = "mercury is the smallest planet in our solar system. It's just a little bigger than earth's moon"
    elif planet == "venus":
        label_planet_name['text'] = "venus"
        label_planet_image['image'] = venus
        label_planet_gravity_radius['text'] = "gravity : 8.87 m/s \n radius : 6,051.8 km"
        label_planet_info['text'] = "venus is the brightest object in the sky after the sun and the moon, and sometimes looks like a bright star in the morning or evening sky."
    elif planet == "earth":
        label_planet_name['text'] = "earth"
        label_planet_image['image'] = earth
        label_planet_gravity_radius['text'] = "gravity : 9.087 m/s \n radius : 6,371 km"
        label_planet_info['text'] = "earth is the only place in the known universe sonfirmed to host life and it's the only one known for sure to have liquid wateron it's surface"
dropdown.place(relx=0.5,rely=0.1 , anchor=CENTER)        
    
btn = Button(root, text="show planet Info", command=planetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5,rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5,rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5,rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5,rely=0.9, anchor=CENTER)

root.mainloop()
