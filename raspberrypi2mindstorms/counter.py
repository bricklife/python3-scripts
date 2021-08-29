import RPi.GPIO as GPIO
import subprocess
import time

pin = 35
i = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

subprocess.run("hcitool -i hci0 cmd 0x08 0x0006 50 00 50 00 02 00 00 00 00 00 00 00 00 07 00", shell=True)

while True:
    if GPIO.input(pin) == False:
        subprocess.run("hcitool -i hci0 cmd 0x08 0x0008 09 ff 03 97 {:02x} 48 03 83 a3 {:02x}".format(i % 255, ord(str(i % 10))), shell=True)
        subprocess.run("hcitool -i hci0 cmd 0x08 0x000a 01", shell=True)
        time.sleep(0.2)
        subprocess.run("hcitool -i hci0 cmd 0x08 0x000a 00", shell=True)
        i += 1
    time.sleep(0.1)

GPIO.cleanup()
