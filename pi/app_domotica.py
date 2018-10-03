import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil
import cgi
from pygame import mixer

serviceAccountKey = '../../labo-2-domotica-nickboone-firebase-adminsdk-avj62-b1ad077764.json'
databaseURL = 'https://labo-2-domotica-nickboone.firebaseio.com/'


try:
    # Fetch the service account key JSON file contents
    firebase_cred = credentials.Certificate(serviceAccountKey)

    # Initalize the app with a service account; granting admin privileges
    firebase_admin.initialize_app(firebase_cred, {
    'databaseURL': databaseURL
    })

    # As an admin, the app has access to read and write all data
except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# get random arcade matrix
def get_matrix():
    
    Y = [255, 255, 0]  # Yellow
    O = [0, 0, 0]  # Black
    Z = [0,255,0]
    F = [255,0,0]
    B = [0,0,255]

    question_mark = [
    O, O, Y, O, O, Y, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    B, O, O, O, O, O, O, B,
    O, O, Y, O, O, Y, O, O,
    Z, O, O, O, O, O, O, F,
    Z, O, O, O, O, O, O, F,
    Z, O, O, B, B, O, O, F
    ]

    return(question_mark)

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    while True:
        matrix = get_matrix();
        sense_hat.set_pixels(matrix)
        sleep(3)
        
        for event in sense_hat.stick.get_events():
            if format(event.action) == "pressed":

                mixer.init()
                bel = mixer.Sound("music/sound.wav")
                bel.play()
            
            
            
       
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sense_hat.clear()
        sys.exit(0)