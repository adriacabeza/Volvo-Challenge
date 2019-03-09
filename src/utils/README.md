# Driver License detection 
- To be able to detect if a driver license and not just a random ID card or a falsification; we have used Optical character recognition and a bag of words (using some tolerance of error within every word) that represent some of the words that it should contain the image. 

### Other useful functions
- A function to delete temporary folders, we will use it  whenever our customer take selfies to login. Also after confirming the driver license is fine we can delete it too.

- A function to compress a picture (we must use it if we want to use several pictures in our system). It will be used everytime a new person is registrated. 
