import sys, time, subprocess

time_left = int(sys.argv[1])
while time_left>0:
    print(f"Time Left : {time_left}")
    time.sleep(1)
    time_left-=1

subprocess.Popen(['start','alarm.wav'], shell=True)