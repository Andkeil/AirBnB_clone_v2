#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import models


class DBStorage:
        __engine = None
        __session = None

        def __init__(self):
            """
            Initialization Method
            """
            user = os.getenv('HBNB_MYSQL_USER', default=None)
            pw = os.getenv('HBNB_MYSQL_PWD', default=None)
            host = os.getenv('HBNB_MYSQL_HOST', default=None)
            db = os.getenv('HBNB_MYSQL_DB', default=None)
            form = "mysql+mysqldb://{}:{}@{}/{}"
            connection = form.format(user, pw, host, db)
            self.__engine = create_engine(connection, pool_pre_ping=True)
            if os.getenv('HBNB_ENV') == 'test':
                    Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """
            query current database based on cls name
            """
            allobjs = {}
            if cls:
                cname = cls.__name__
                query = self.__session.query(cls)
                for instance in query:
                    allobjs[cname + '.' + instance.id] = instance
            else:
                for subclass in Base.__subclasses__():
                    query = self.__session.query(subclass)
                    cname = subclass.__name__
                    for instance in query:
                        allobjs[cname + '.' + instance.id] = instance
            return allobjs

        def new(self, obj):
            """
            New Method
            """
            if obj:
                self.__session.add(obj)

        def save(self):
            """
            Save Method
            """
            self.__session.commit()

        def delete(self, obj=None):
            """
            Delete Method
            """
            if obj:
                self.__session.delete(obj)
                self.save()

        def reload(self):
            """
            Reload Method
            """
            Base.metadata.create_all(self.__engine)
            sm = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sm)
            self.__session = Session()

        def close(self):
            self.__session.remove()
