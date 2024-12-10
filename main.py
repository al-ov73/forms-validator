from fastapi import Request, FastAPI

from database import get_items
from parser import get_template_name, parse_input_query


app = FastAPI()


@app.post("/get_form")
async def validate_form(request: Request) -> dict:
    """
    check input form and return name of template or parsed form
    """
    templates = get_items()
    input_query = dict(request.query_params)
    parsed_form_data = parse_input_query(input_query)
    template_name = get_template_name(templates, parsed_form_data)
    response = {"template_name": template_name}
    return response if template_name else parsed_form_data
