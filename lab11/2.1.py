import math

def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    R = 6371.032
    distance = R * math.acos(math.sin(lat1) * math.sin(lat2) + 
                             math.cos(lat1) * math.cos(lat2) * 
                             math.cos(lon1 - lon2))
    return distance

lat1 = 39.9075000  
lon1 = 116.3972300
lat2 = 50.4546600
lon2 = 30.5238000

distance = distance(lat1, lon1, lat2, lon2)
print(f"Відстань між Пекіном і Києвом: {distance:.2f} км")
