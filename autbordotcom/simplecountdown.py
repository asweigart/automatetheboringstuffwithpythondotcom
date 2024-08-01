# https://autbor.com/simplecountdown.py - A simple countdown script.

import time, subprocess

timeLeft = 2
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.run(['start', 'alarm.wav'], shell=True)  # Windows
#subprocess.run(['open', 'alarm.wav'])  # macOS & Linux
