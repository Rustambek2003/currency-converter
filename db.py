from tinydb import TinyDB

db = TinyDB('db.json', indent = 4)

teble1 = db.table('Apple')

print(teble1.get(doc_id=3))
