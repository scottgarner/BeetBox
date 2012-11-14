import pygame
from pygame.locals import *
import time
import curses

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

up = pygame.mixer.Sound('up.wav')
down = pygame.mixer.Sound('down.wav')
left = pygame.mixer.Sound('left.wav')
right = pygame.mixer.Sound('right.wav')

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
	screen.addstr(1, 0, "Ready to accept up, down, left or right to play sounds or q to quit!")
	screen.addstr(2, 0, "To get to a new console press Alt-F2")

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == ord('1'):	
		screen.addstr(3,0,"wat")
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
	elif event == curses.KEY_UP:
		screen.addstr(0, 0, "You pressed up!")
		up.play()
	elif event == curses.KEY_DOWN:
		screen.clear()
		screen.addstr(0, 0, "You pressed down!")
		down.play()
	elif event == curses.KEY_LEFT:
		screen.clear()
		screen.addstr(0, 0, "You pressed left!")
		left.play()
	elif event == curses.KEY_RIGHT:
		screen.clear()
		screen.addstr(0, 0, "You pressed right!")
		right.play()
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")

curses.endwin()
