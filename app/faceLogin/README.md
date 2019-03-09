# FaceLogin 

For this approach we have used the smartphone app to be able to use the client's face to identificate. 

We have used an already trained model based on Deep Learning: a Convolutional Neural Network that is capable tble to discriminate diferent faces with just one picture (the one that the client updates when he registers). The model that we peaked is one that has reached an accuracy of 99.38% using the Labeled Faces in the Wild benchmark ( http://vis-www.cs.umass.edu/lfw/)

### FaceLogin Process

The way it works is the following:

-  We upload the picture to our storage server in the registration process.
- Whenever the user wants to login to our app, he takes a selfie that is stored temporarly . Then we extract the features for the selfie using the model and we start looking for those features in our database pictures. 
- If we find any match we give the user the authentification to take the car, if not, an alert box will alert him about it and he will be able to take another picture.

