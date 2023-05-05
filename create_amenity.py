#!/usr/bin/python3
from models import *
from models.base_model import BaseModel, Base
from models.amenity import Amenity

print("-- Create new amenity --")
am1 = Amenity()
am1.name = "24-hour check-in"
am1.save()
print(am1)

am2 = Amenity()
am2.name = "Air conditioning"
am2.save()
print(am2)

am3 = Amenity()
am3.name = "Breakfast"
am3.save()
print(am3)

am4 = Amenity()
am4.name = "Wifi connection"
am4.save()
print(am4)

am5 = Amenity()
am5.name = "Cable TV"
am5.save()
print(am5)

am6 = Amenity()
am6.name = "Carbon monoxide detector"
am6.save()
print(am6)

am7 = Amenity()
am7.name = "Cat(s)"
am7.save()
print(am7)

m8 = Amenity()
m8.name = "Dog(s)"
m8.save()
print(m8)
