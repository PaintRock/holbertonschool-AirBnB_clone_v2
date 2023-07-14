#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """city getter"""
            city_list = []
            for obj in models.storage.all(City).values():
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list

    def cities(self):
        """getter added in web_flask """
        cities_list = []
        for city in list (storage.all(City).value()):
            if city.state.id == self.id:
                cities_list.append(city)
        return cities_list if len(cities_list) > 0 else None
