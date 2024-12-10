from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB("db.json")


def get_items() -> list[Document]:
    """
    return list of all items in database
    """
    return db.all()
