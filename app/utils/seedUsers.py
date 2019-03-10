from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os


def main(isOwner):
    # Connect to the DB
    mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

    client = MongoClient(mongo_uri)
    db = client['heroku_xv3vfwld']
    collection = db['users']

    # Ask for data to store
    user = input("Enter your username: ")
    password = input("Enter your password: ")
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