import RPi.GPIO as GPIO
from flask import Flask, render_template, request, url_for
import time
from flask_socketio import SocketIO
from picamera import PiCamera
from time import sleep
import cv2
import os
from keras.models import load_model
import numpy as np
import camera
import pretrainmodel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

index=1
my_camera = PiCamera()
camera.take_picture(index, my_camera)

PET_PATH='/home/pi/auto_petfeeder/static/pet.'+str(index)+'.jpg'

CONTROL_PIN = 17    
PWM_FREQ = 50


GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
     
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)

'''module'''

def my_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle
 



@app.route("/")
def main():
    global index
    img=url_for('static',filename='pet.%d.jpg'%index)
    #img=cv2.resize(img,(50,50))
    
    return render_template('main.html', img=img)

@app.route("/control")
def action():
    global index,pwm,PET_PATH,model,tex,my_camera
    
    my_model = pretrainmodel.pretrain_model('null')
    
    STEP=15
    img=url_for('static',filename='pet.%d.jpg'%index)
    PET_PATH='/home/pi/auto_petfeeder/static/pet.'+str(index)+'.jpg'
    
    m = my_model.my_predict(PET_PATH)
    
    my_list=m.tolist()
    #my_list[0][0]=1.0
    
    if my_list[0][0]==1.0:
        tex='few feed'
        pwm.start(0)
        dc=0
        for angle in range(150, -1, -STEP):
            dc = my_duty_cycle(angle)
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        
        for angle in range(0, 121, STEP):
            dc = my_duty_cycle(angle)
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.4)
    elif my_list[0][0]==0.0:# more
        tex='more feed'

    index=index+1
    camera.take_picture(index, my_camera)
    
    img=url_for('static',filename='pet.%d.jpg'%index)
    #img=cv2.resize(img,(50,50))
        
    return render_template('main.html', img=img, tex=tex)

if __name__ == "__main__" :
    socketio.run(app, host='0.0.0.0', port=5000)     
    
'''
@app.route("/<changePin>/<action>")
def action(changePin, action):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    
      
    if action == "on":
        GPIO.output(changePin, GPIO.HIGH)
        pwm.start(0)
        
        for angle in range(150, -1, -STEP):
                dc = my_duty_cycle(angle)
                pwm.ChangeDutyCycle(dc)

                time.sleep(0.1)
                    
        for angle in range(0, 121, STEP):
            dc = my_duty_cycle(angle)
            pwm.ChangeDutyCycle(dc)
                   
            time.sleep(0.4)
        time.sleep(0.5)
        message = "Turned " +deviceName+" on."
        


    
    
    if action == "off":
        GPIO.output(changePin, GPIO.LOW)
        message = "Turned" +deviceName+ " off."
        
    pwm.stop()    
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
        
    templateData = {
        'pins' : pins    
    }
    
    return render_template('main.html', **templateData)
'''

