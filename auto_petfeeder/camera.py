from picamera import PiCamera
from time import sleep

def take_picture(index, my_camera):
    camera = my_camera
    camera.start_preview()
    camera.capture('/home/pi/auto_petfeeder/static/pet.%d.jpg' %index)
    sleep(1)
    camera.stop_preview()
