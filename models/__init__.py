from mongoengine.connection import connect

from config import DB_URI_WITH_INDEX, DB_URI_WITHOUT_INDEX

db_with_index = connect(host=DB_URI_WITH_INDEX, alias='default')
db_without_index = connect(host=DB_URI_WITHOUT_INDEX, alias='without_index')

print("db_with_index: ", db_with_index)
print("db_without_index: ", db_without_index)