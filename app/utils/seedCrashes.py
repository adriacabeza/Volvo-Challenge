from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os

data =[
{"impactAngle":-341.54339233899367,"offsetMaximumForce":20175},
{"impactAngle":-32.74137379765352,"offsetMaximumForce":1171, "user": "Robert", "date": "27/05/2018", "car": "Volvo V40"},
{"impactAngle":-308.3000606298933,"offsetMaximumForce":20387, "user": "Michelle", "date": "04/11/2017", "car": "Volvo XC40"},
{"impactAngle":-84.77214151730084,"offsetMaximumForce":20209, "user": "John", "date": "31/07/2017", "car": "Volvo XC90"},
{"impactAngle":-159.1955345095375,"offsetMaximumForce":1690, "user": "Johnny", "date": "1/02/2016", "car": "Volvo V90"},
{"impactAngle":-8.4255066323192,"offsetMaximumForce":5558, "user": "Robert", "date": "30/10/2015", "car": "Volvo S90"},
{"impactAngle":294.56235398164944,"offsetMaximumForce":20358, "user": "Johnny", "date": "15/10/2015", "car": "Volvo XC60"},
{"impactAngle":-260.5895797216587,"offsetMaximumForce":5512, "user": "Michelle", "date": "23/08/2015", "car": "Volvo S60"}
]


def main(isOwner):
    # Connect to the DB
    mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

    client = MongoClient(mongo_uri)
    db = client['heroku_xv3vfwld']
    collection = db['crashes']

    # Ask for data to store
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        collection.insert({"_id": user, "password": pass_hash, "owner": isOwner})
        print ("User created.")
    except DuplicateKeyError:
        print ("User already present in DB.")


if __name__ == '__main__':
    ans = input('Introduce owners? y|n').lower()
    isOwner = ans == 'y' or ans == 'yes'
    while True:
        main(isOwner)