import numpy as np
import cv2

""" 
Siyah bir resim oluşturup ekrana çift tıkladığımızda beyaz daire çizen kod yazdım.
daire çapı: 20
"""


""" 
Tıklama fonksiyonu
"""
""" 
cv2.EVENT_L BUTTON DOUBLE CLİCK
**a ve b EVENT_LBUTTONDBLCLK'un**
"""
def ciz(eylem,x,y,a,b): 
    if eylem == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(image,(x-50,y-50),(x+50,y+50),(255,255,255),1)
        

""" 
Zeros ile siyah bir görüntü oluşturdum.
"""
image=np.zeros((320,320),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',ciz)


while(1):
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF==32: #32 = space tuşu ASCII.
        break

cv2.destroyAllWindows()