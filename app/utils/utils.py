import shutil
from PIL import Image
import re
import cv2
import pytesseract


#DELETE A TEMPORARY FOLDER
def deleteTempFile(folder='/faceLogin/Temp'):
  shutil.rmtree('..'+folder)
#OPTIMIZE AN IMAGE
def optimizeImage(ImageName, option='faceLogin/Faces'):
  route = ('../'+option+'/'+ImageName)
  foo = Image.open(route)
  foo.resize((160,300),Image.ANTIALIAS)
  foo.save(route,optimize=True,quality=95)



#OCR STUFF

keywords = ['Permis','conduire','Licenza','condurre','Fiihrerausweis','Permisdeconduire',
'Licenzadicondurre','Permissda','conesdicondurts','Fuhrerausweis','Driving', 'License','Permiss',
'manischar','Fohreraumwets-Perwes','Fuhrerausweis-Permis','Licence','Permiss','roanischar']
#OCR is not that good in all kinds of images so I have put some of the inputs that I get with real values

def check_if_driver_license(ImageName):
  image = cv2.imread(r'../DriverLicense/'+ImageName)
  text = pytesseract.image_to_string(Image.fromarray(image))
  text = text.replace(" ","")
 # print(text)
  if len(text) > 0 and any(x in text for x in keywords):
    print('IT IS A DRIVING LICENSE BRO')
    return True
  else :
    print('WHAT IS THIS')
    return False



def tests():
  check_if_driver_license('license4.jpg')
  check_if_driver_license('license2.jpg')
  check_if_driver_license('license3.jpg')
  check_if_driver_license('notalicense.jpg')
  check_if_driver_license('license6.jpg')
  check_if_driver_license('notalicense2.jpg')
  check_if_driver_license('prueba.jpg')


