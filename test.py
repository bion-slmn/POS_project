#from models import storage
from models.category import Category
from models.item import Item
from models.sale import Sale
from models import storage

storage.load()
c = Category(name='Engine', description='Motorbike eninges')
i = Item(buying_price=190, selling_price=200, description='bearing', name='Bearing 2000')
s = Sale(name = 'Bearing 2000', no_of_items_sold=2, unit_price=10.5, total_price= 2*10.5)
c.save()
s.save()
i.save()
print(c.id, c.created_at)
print('after')
#from models import storage
