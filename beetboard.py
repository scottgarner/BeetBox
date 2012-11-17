import pygame
from pygame.locals import *
import time
import curses

#import mpr121

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

#mpr121.setup(0x5a)

kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
openhh = pygame.mixer.Sound('open.wav')
closedhh = pygame.mixer.Sound('closed.wav')
clap = pygame.mixer.Sound('clap.wav')
cymbal = pygame.mixer.Sound('cymbal.wav')

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()

while True:

	#touchData = mpr121.readData(0x5a)

	#for i in range(6):
	#	touchValue = touchData & (1<<i)
	#	screen.addstr(i+1, 0, str(touchValue))

	#screen.addstr(0, 0, str(touchData))

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == ord('1'):	
		kick.play();
	elif event == ord('2'):	
		snare.play();
	elif event == ord('3'):	
		openhh.play();
	elif event == ord('4'):	
		closedhh.play();
	elif event == ord('5'):	
		clap.play();
	elif event == ord('6'):	
		cymbal.play();										
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")


curses.endwin()
