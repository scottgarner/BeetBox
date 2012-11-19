import pygame

import RPi.GPIO as GPIO
import mpr121

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()
pygame.mixer.music.set_volume(.25);

kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
openhh = pygame.mixer.Sound('open.wav')
closedhh = pygame.mixer.Sound('closed.wav')
clap = pygame.mixer.Sound('clap.wav')
cymbal = pygame.mixer.Sound('cymbal.wav')

# Track touches

touches = [0,0,0,0,0,0];

while True:

	if (GPIO.input(7)):
		pass
	else:
		touchData = mpr121.readData(0x5a)

		print bin(touchData)

		for i in range(6):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					if (i == 0):
						kick.play()
					elif (i == 1):
						snare.play()
					elif (i == 2):
						openhh.play()
					elif (i == 3):
						closedhh.play()
					elif (i == 4):
						clap.play()
					elif (i == 5):
						cymbal.play()

				touches[i] = 1;
			else:
				if (touches[i] == 1):
					pass
					#print( 'Pin ' + str(i) + ' was just released')

				touches[i] = 0;

