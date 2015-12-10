import subprocess
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

call = "sudo python py/synchronized_lights.py --file="
songs = ["py/crazyinlove.mp3", "py/sorry.mp3", "py/eyeofthetiger.mp3"]
songnames ["Crazy in Love by Beyonce ft. Jay-Z", "Sorry by Justin Bieber", "Eye of the Tiger by Survivor"]

print "Press button to start playing music! Press again to stop the song, and again to start a new song"

while True:
	input_state = GPIO.input(5)
	if input_state == False:
		i = random.randint(0,2)
		print "Now playing: " + songnames[i] + "\n"
		command = call + songs[i]
		subprocess.call(command, shell=True)
		time.sleep(0,2)
