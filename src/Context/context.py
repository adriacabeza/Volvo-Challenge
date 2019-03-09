class Context:
  def __init__(self,parkings,cars,users):
    self.parkings = parkings
    self.users = users
    self.cars = cars

  def give_price_to_user(self,user_id):
    return 0
  
  def predict_price(self):
    return 0


class Car:
  def __init__(self,id=0,lat=0,log=0,available=True,gas=0,value=0):
    self.id = id
    self.position= {'lat':lat,'log':log}
    self.available= available
    self.gas= gas
    self.value = value #maybe depending on which type of car it is


class Parking:
  def __init__(self,id=0,freePlaces=0,totalPlaces=0,lat=None,log=None):
    self.id = id
    self.position= {'lat':lat,'log':log}
    self.freePlaces= freePlaces
    self.totalPlaces= totalPlaces

  
  
class User:
  def __init__(self,route, id=0,car=None,destination=None):
    self.id = id
    self.car = car
    self.destination = destination
    self.route = route
