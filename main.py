from typing import Any

from fastapi import Request, FastAPI, Form
from tinydb import TinyDB, Query

app = FastAPI()
db = TinyDB('db.json')

@app.post("/")
async def validate_form(request: Request):
    print(type(request.query_params))
    return "Hello world"

# тестовое
# https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit?tab=t.0

# На вход по урлу /get_form POST запросом передаются данные такого вида:
# f_name1=value1&f_name2=value2


# https://tinydb.readthedocs.io/en/latest/getting-started.html#basic-usage
# >>> User = Query()
# >>> db.insert({'name': 'John', 'age': 22})
# >>> db.search(User.name == 'John')
# [{'name': 'John', 'age': 22}]
#
# >>> db.all()
# [{'count': 7, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]
#
# >>> Fruit = Query()
# >>> db.search(Fruit.type == 'peach')
# [{'count': 3, 'type': 'peach'}]
# >>> db.search(Fruit.count > 5)
# [{'count': 7, 'type': 'apple'}]