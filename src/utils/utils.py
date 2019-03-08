import shutil

def deleteTempFile(folder='Temp'):
  shutil.rmtree('../faceRecognition/'+folder)

