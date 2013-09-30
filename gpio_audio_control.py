#!/usr/bin/python3

import os
import subprocess
import time
import atexit
import RPi.GPIO as GPIO

devnull = open('/dev/null', 'w')
procs = []
pin11 = 11
pin13 = 13
pin15 = 15
pin16 = 16
pin22 = 22

def play_sound0(event):
	for proc in list(procs):
		proc.terminate()
		procs.remove(proc)
	sound0 = subprocess.Popen(["/usr/bin/aplay", "Rambo.wav"],shell=False,stdin=None,stdout=devnull,stderr=devnull)
	procs.append(sound0)

def play_sound1(event):
	for proc in list(procs):
		proc.terminate()
		procs.remove(proc)
	sound1 = subprocess.Popen(["/usr/bin/aplay", "runaway.wav"],shell=False,stdin=None,stdout=devnull,stderr=devnull)
	procs.append(sound1)

def play_sound2(event):
	for proc in list(procs):
		proc.terminate()
		procs.remove(proc)
	sound2 = subprocess.Popen(["/usr/bin/aplay", "Borat_Yes.wav"],shell=False,stdin=None,stdout=devnull,stderr=devnull)
	procs.append(sound2)

def play_sound3(event):
	for proc in list(procs):
		proc.terminate()
		procs.remove(proc)
	sound3 = subprocess.Popen(["/usr/bin/aplay", "Borat_No.wav"],shell=False,stdin=None,stdout=devnull,stderr=devnull)
	procs.append(sound3)

def shutdown_os(event):
	print ("Shutting down...")
	os.system("shutdown -h now &")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin11, GPIO.FALLING, callback=play_sound0, bouncetime=500)
GPIO.add_event_detect(pin13, GPIO.FALLING, callback=play_sound1, bouncetime=500)
GPIO.add_event_detect(pin15, GPIO.FALLING, callback=play_sound2, bouncetime=500)
GPIO.add_event_detect(pin16, GPIO.FALLING, callback=play_sound3, bouncetime=500)
GPIO.add_event_detect(pin22, GPIO.FALLING, callback=shutdown_os, bouncetime=2000)

while True:
    time.sleep(1)

@atexit.register
def kill_subprocesses():
	for proc in procs:
		proc.kill()
	GPIO.cleanup()
	GPIO.remove_event_detect(pin11)
	GPIO.remove_event_detect(pin13)
	GPIO.remove_event_detect(pin15)
	GPIO.remove_event_detect(pin16)
	GPIO.remove_event_detect(pin22)
