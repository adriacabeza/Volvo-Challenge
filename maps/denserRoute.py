import json
import numpy as np

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

route = json.load(open('roadsCoordinates.json'))

route = [list(x.values()) for x in route]
route = np.array(route)

print(route[0])
print(haversine(*route[0],*route[1]))


newRoute = [route[0]]

for i in range(1,len(route)):
    c = haversine(*route[i],*route[i-1])/0.01
    c = int(c)
    for j in range(1,c):
        newRoute.append(newRoute[-1]+(route[i]-route[i-1])/c)
    newRoute.append(route[i])

newRoute = [{'lng':x[0],'lat':x[1]} for x in newRoute]

print(len(newRoute))

json.dump(newRoute, open('denseRoadsCoords.json','w'))


