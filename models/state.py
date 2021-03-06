#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ""

        @property
        def cities(self):
            cities_dict = models.storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
