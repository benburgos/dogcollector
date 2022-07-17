from django.db import models

# Create your models here.
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Noah', 'Heeler', 'Old Man.', 8),
    Dog('Minnie', 'GoldenDox', 'Crazy.', 1)
]