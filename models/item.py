#!/usr/bin/env python3
'''this defines a class item'''
from models.base_model import BaseModel


class Item(BaseModel):
    '''defines a class item describes how items sold
    are defined'''
    name = ''
    buying_price = 0
    selling_price = 0
    photo = ''
    description = ''
    sales_id = []
