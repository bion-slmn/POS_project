#!/usr/bin/env python3
'''defines a sale class'''
from models.base_model import BaseModel


class Sale(BaseModel):
    '''defiines a sale of an item'''
    name = ''
    no_of_items_sold = 0
    unit_price = 0
    discount = 0
    total_price = 0
