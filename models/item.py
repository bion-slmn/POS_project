#!/usr/bin/env python3
'''this defines a class item'''
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Integer, DateTime, Column, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String


class Item(BaseModel, Base):
    '''defines a class item describes how items sold
    are defined'''

    __tablename__ = "items"
    print("IN items")

    buying_price = Column(Float, nullable=False)
    selling_price = Column(Float,  nullable=False)
    photo = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    # creating a relationship with sales
    sales = relationship('Sale', backref='items', cascade='all, delete')
    # creating a relationship with category
    category_id = Column(
            String(60), ForeignKey("categories.id"), nullable=True
            )
