import cv2
import numpy as np
import math

#leyendo la imagen 
image=cv2.imread("./img.jpg")

#convertir a HSV
imageHSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


#filtrado

minH=np.array([0,0,0])
maxH=np.array([4,255,255])
binaryImage=cv2.inRange(imageHSV,minH,maxH)

cv2.imwrite("img_binary.png",binaryImage)

cv2.imshow("binary",cv2.resize(binaryImage,(800,800)))


#Calculo de los momentos
moments=cv2.moments(binaryImage,True);


#El area de la imagen 
areaObject=moments['m00']
print("El area del objeto es:",areaObject)

#area del frame
areaImage=binaryImage.shape[0]*binaryImage.shape[1]

print("El area del frame es:", areaImage)

#posicion centro de masa
xcenter=moments['m10']/moments['m00']
ycenter=moments['m01']/moments['m00']

print("Area normalizada:",areaObject/areaImage)

#Posiciones normalizadas:
xnorm = xcenter/binaryImage.shape[0]
ynorm = ycenter/binaryImage.shape[1]
print("POSICION DEL CENTRO DE MASA (x,y):", xcenter/binaryImage.shape[0],ycenter/binaryImage.shape[1])


#Para calcular la matriz de covarianza para PCA:
data_points = []
threshold = 0
H = binaryImage.shape[0]
W = binaryImage.shape[1]

for i in range(H):
    for j in range(W):
        if binaryImage[i, j] > threshold:
            data_points.append([i, j])
data_points = np.asarray(data_points)
cov_mat = np.cov(data_points.T)

#Eigenvectors y eigenvalues de la matriz de covarianza

eig_val, eig_vec = np.linalg.eig(cov_mat)
#eig_val es un vector de los eigenvalues
#eig_vect es una matriz cuyas columnas son los eigenvectores

#print ("eigenvector", eig_vec)
#print (eig_val)
#print(eig_val.max())

#Posicion del mayor eigenvalue
pos= np.where(eig_val==max(eig_val))[0]
print(pos)

#El componente principal será el eigenvector que corresponde al mayor eigenvalue,
PC1=eig_vec[:,pos] #Componente principal, vector normalizado
print("Componente Principal:", PC1)
 #

#Para hallar al angulo que forma con el eje x:
angulo = math.atan((PC1[1]/PC1[0]))
angulo = angulo*180/np.pi

print("EL ANGULO ES", angulo )

key=cv2.waitKey(0)
cv2.destroyAllWindows();
