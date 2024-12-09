from tinydb import TinyDB, Query

db = TinyDB("db.json")


def get_items():
    return db.all()
