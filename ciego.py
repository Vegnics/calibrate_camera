import os
import sys
from CeleryPy import log
from CeleryPy import send_message
from DB import DB
from Image import Image
import json
from Parameters import Parameters
import requests
import cv2
from Capture import Capture
import numpy as np
from PlantDetection import PlantDetection
from farmware_tools import device
import CeleryPy
import time

device.set_pin_io_mode(1,4)
weeder=(20,553,-402)
dir_path='/root/farmware'
matrix=np.load(dir_path+'/'+'array.npy')
matrix2=np.load(dir_path+'/'+'array2.npy')
matrix3=np.load(dir_path+'/'+'array3.npy')
matrix4=np.load(dir_path+'/'+'array4.npy')
send_message(message='TUDO BEM', message_type='success', channel='toast')
CeleryPy.move_absolute(weeder,(0,0,0),150)
CeleryPy.move_absolute(weeder,(100,0,0),150)
CeleryPy.move_absolute(weeder,(100,0,100),150)
CeleryPy.move_absolute(weeder,(100,0,200),150)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(100)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(200)
CeleryPy.write_pin(number=4, value=1, mode=0)
  
xmat=0
ymat=0
xmatsig=0
ymatsig=0
x,y=matrix[ymat,xmat]
x=x-7
y=y+7
xsig,ysig=matrix2[ymatsig,xmatsig]
xsig=xsig-7
ysig=ysig+7
CeleryPy.move_absolute((x,y,-205),(0,0,0),100)
CeleryPy.move_absolute((x,y,-282),(0,0,0),100)
CeleryPy.wait(500)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(2000)
CeleryPy.move_absolute((x,y,-215),(0,0,0),100)
CeleryPy.wait(500)
CeleryPy.move_absolute((xsig,ysig,-200),(0,0,0),100)
CeleryPy.move_absolute((xsig,ysig,-278),(0,0,0),100)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(400)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(400)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(400)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(400)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.move_absolute((xsig,ysig,-205),(0,0,0),100)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(200)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(200)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(200)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(500)
CeleryPy.move_absolute(weeder,(120,0,200),150)
CeleryPy.move_absolute(weeder,(120,0,0),150)
CeleryPy.move_absolute(weeder,(0,0,0),150)
CeleryPy.move_absolute(weeder,(0,0,200),150)
CeleryPy.move_absolute((0,0,0),(0,0,0),250)