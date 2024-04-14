import pyscreenshot as ImageGrab
import time

images_folder="C:\\Users\\lenovo\\Desktop\\handwritten text\\2"

for i in range(0,5):
   time.sleep(8)
   im=ImageGrab.grab(bbox=(60,170,400,550)) #x1,y1,x2,y2
   print("*****SAVED*****",i)
   im.save(images_folder+str(i)+'.png')
   print("*****RE-DRAW*****")
