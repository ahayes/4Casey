#!/usr/bin/python3


import pifacedigitalio as piface
import subprocess
import time
import atexit

piface.init()
pfd = piface.PiFaceDigital()

procs = []

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

listener = piface.InputEventListener()
pfd.leds[7].turn_on()
listener.register(0, piface.IODIR_ON, play_sound0)
listener.register(1, piface.IODIR_ON, play_sound1)
listener.activate()

@atexit.register
def kill_subprocesses():
	for proc in procs:
		proc.kill()
	pfd.leds[7].turn_off()
