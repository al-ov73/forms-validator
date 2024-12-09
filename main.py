from fastapi import Request, FastAPI

from database import get_items
from parser import get_template_name, parse_input_query


app = FastAPI()


@app.post("/get_form")
async def validate_form(request: Request):
    templates = get_items()
    print(templates)
    params = dict(request.query_params)
    parsed = parse_input_query(params)
    template_name = get_template_name(templates, parsed)
    return template_name if template_name else parsed


# http://localhost:8000/get_form?user=value&ordered=2024-12-12

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
# >>> db.search(Fruit.type == 'peach')n
# [{'count': 3, 'type': 'peach'}]
# >>> db.search(Fruit.count > 5)
# [{'count': 7, 'type': 'apple'}]
