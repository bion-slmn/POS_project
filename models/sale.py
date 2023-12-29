#!/usr/bin/env python3
'''this defines a class item'''
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Integer, DateTime, Column, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String


class Sale(BaseModel, Base):
    '''defines a class item describes how items sold
    are defined'''

    __tablename__ = "sales"
    print("SALES")

    no_of_items_sold = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    discount = Column(Float)
    total_price = Column(Float, nullable=False)
    # creating a relationship with items
    item_id = Column(
            String(60), ForeignKey("items.id"), nullable=True
            )
