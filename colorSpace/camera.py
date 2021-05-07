import cv2
import numpy as np 

cv2.namedWindow("main")


def callback(x):
    pass


#video capture args 
#Si es un numerico 0,1,2 lee las camaras fisicas conectadas a la pc, 
# siendo 0 la primera camara (Generalmente la integrada) y n la enesima camara 
#Si es una url lee el buffer de video
cam=cv2.VideoCapture(0)

while(cam.isOpened()):
    r,frame=cam.read()
    cv2.imshow("original",frame)
    #waitkey devuelve el asci de la tecla oprimida
    key=cv2.waitKey(1)
    if(key==ord("q")):
        break

cv2.destroyAllWindows();




