import os
import face_recognition


def load_and_encode(namefile):
  picture_of_user = face_recognition.load_image_file(namefile)
  #encode into a feature vector
  face_encoding = face_recognition.face_encodings(picture_of_user)
  if len(face_encoding) > 0:
    return face_encoding[0]
  else: 
    raise NameError('No face was found')


def registerUser(ID1='obama', ID2='trump'):
  folderFaces = os.getcwd()+'/faceLogin/'
  biden_encodingID1 = load_and_encode(folderFaces + 'Temp/%s_temp.jpg' % ID1)
  biden_encodingID2 = load_and_encode(folderFaces + 'Temp/%s_temp.jpg' % ID2)

  if comparePeople(biden_encodingID1,biden_encodingID2):
    return True
  else:
    return False

def detectUser(ID='obama'):
  folderFaceLogin = os.getcwd()+'/faceLogin/'
  biden_encoding = load_and_encode(folderFaceLogin + 'Temp/%s_temp.jpg' % ID)
  facesDir = folderFaceLogin+'Faces'

  for image in os.listdir(facesDir):
    biden_encodingID= load_and_encode(facesDir+'/'+image)
    if comparePeople(biden_encoding, biden_encodingID):
      print('Face found on '+ image)
      return True
  print('Face not found')
  return False

def comparePeople(biden_encoding, biden_encodingID):
  results = face_recognition.compare_faces([biden_encoding], biden_encodingID)
  return results[0]

