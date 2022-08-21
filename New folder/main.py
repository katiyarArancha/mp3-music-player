import pygame
from pygame import mixer
from tkinter import *
import os

def playmusic():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Play")
    mixer.music.play()

def pausemusic():
    songstatus.set("Pause")
    mixer.music.pause()

def stopmusic():
    songstatus.set("Stop")
    mixer.music.stop()

def resumemusic():
    songstatus.set("Resume")
    mixer.music.unpause()    

root=Tk()
root.title('Music Player')

mixer.init()
songstatus=StringVar()
songstatus.set("choose")

# initializing playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="VioletRed",fg="black",font=('Ravie',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Arancha\Documents\New folder\song')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)



#creating buttons
playbtn=Button(root,text="Play",command=playmusic)
playbtn.config(font=('arial',20),bg="#856ff8",fg="black",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausemusic)
pausebtn.config(font=('arial',20),bg="pale violet red",fg="black",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopmusic)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="black",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumemusic)
Resumebtn.config(font=('arial',20),bg="firebrick1",fg="black",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()