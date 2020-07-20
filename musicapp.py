import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3,TIT2
from tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames=[]
index = 0
v = StringVar()
songlabel = Label (root,textvariable=v,width=55)

def nextsong(event):
	global index
	index +=1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def prevsong(event):
	global index
	index -=1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def stopsong(event):
	
	pygame.mixer.music.stop()
	v.set("")

def playsong(event):
	pygame.mixer.music.play()
	updatelabel()
	
def pausesong(event):
	pygame.mixer.music.pause()
	updatelabel()
	
def resumesong(event):
	pygame.mixer.music.unpause()
	updatelabel()
	


def updatelabel():
	global index
	global songname
	v.set(listofsongs[index])
	



def directorychooser():
	
	directory = askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			# realdir = os.path.realpath(files)
			# audio = ID3(realdir)
			# realnames.append(audio["TIT2"].text[0])
			listofsongs.append(files)

			

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	#pygame.mixer.music.play()

directorychooser()

label = Label(root,text="Music Player")
label.pack()
listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
	listbox.insert(2,items)
listofsongs.reverse()

nextbutton = Button(root,text = "Next Song")
nextbutton.pack()
previousbutton = Button(root,text = "Previous Song")
previousbutton.pack()
stopbutton = Button(root,text = "Stop Song")
stopbutton.pack()
playbutton = Button(root,text = "Play Song")
playbutton.pack()
pausebutton = Button(root,text = "Pause Song")
pausebutton.pack()
resumebutton = Button(root,text = "Resume Song")
resumebutton.pack()



playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
pausebutton.bind("<Button-1>",pausesong)
resumebutton.bind("<Button-1>",resumesong)

songlabel.pack()



root.mainloop()