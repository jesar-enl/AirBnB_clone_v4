#!/usr/bin/python3
from models import *
from models.base_model import BaseModel, Base
from models.place import Place
from models.city import City
from models.user import User

place1 = Place()
place1.city_id = '521a55f4-7d82-47d9-b54c-a76916479545'
place1.user_id = '8cf6d6ad-3f77-4d9b-b841-166a2e08e62c'
place1.name = 'Beautiful Studio - Waikiki'
place1.description = 'Luxurious room to stay for a fortnight'
place1.number_rooms = 3
place1.number_bathrooms = 1
place1.max_guest = 6
place1.price_by_night = 120
place1.latitude = 37.773972
place1.longitude = -122.431297
place1.save()
print(place1)
