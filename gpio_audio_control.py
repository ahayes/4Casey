#!/usr/bin/python3


import subprocess
import time
import atexit
import RPi.GPIO as GPIO

procs = []
channel0 = 11
channel1 = 13

def play_sound0(event):
	procstmp = procs
	for proc in procstmp:
		proc.terminate()
		procs.remove(proc)
	sound0 = subprocess.Popen(["/usr/bin/aplay", "piano2.wav"],shell=False,stdin=None,stdout=None,stderr=None)
	procs.append(sound0)

def play_sound1(event):
	procstmp = procs
	for proc in procstmp:
		proc.terminate()
		procs.remove(proc)
	sound1 = subprocess.Popen(["/usr/bin/aplay", "organfinale.wav"],shell=False,stdin=None,stdout=None,stderr=None)
	procs.append(sound1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(channel0, GPIO.RISING, callback=play_sound0, bouncetime=1000)
GPIO.add_event_detect(channel1, GPIO.RISING, callback=play_sound1, bouncetime=1000)

while True:
    pass

@atexit.register
def kill_subprocesses():
	for proc in procs:
		proc.kill()
	GPIO.cleanup()
	GPIO.remove_event_detect(channel0)
	GPIO.remove_event_detect(channel1)
