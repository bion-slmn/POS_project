from models.engine.db_storage import Db_storage

storage_type = 'db'
if storage_type == 'db':
    from models.engine.db_storage import Db_storage
    storage = Db_storage()
    print('storage')
    storage.load()
