#!/usr/bin/env python3
'''This module defines a database storage'''
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, URL


class Db_storage:
    '''defines a storage database in Mysql'''
    __session = None
    __engine = None

    def __init__(self):
        '''constructs the engine for MYSQL'''
        url_obj = URL.create(
                'mysql+mysqldb',
                username = getenv('POS_USER'),
                password = getenv('POS_PWD'),
                database = getenv('POS_DB'),
                host = 'localhost')
        self.__engine = create_engine(url_object, pool_recycle=3600)

    def new(self, obj):
        '''this method add and object to the database
        -parameter
        obj : (object)  on object of one of the mapped classess
        '''
        self.__session.add(obj)

    def save(self):
        ''' save and object to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete and object if given from the database'''
        if obj:
            self.__session.delete(obj)

    def load(self):
        '''this method creates all tables, start a session'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''close a session '''
        self.__session.remove()
