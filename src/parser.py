from .validators import is_valid_date, is_valid_email, is_valid_phone_number


VALIDATORS = {
    "phone": is_valid_phone_number,
    "date": is_valid_date,
    "email": is_valid_email,
}


def parse_param(param: str) -> str:
    """
    rarse input value and return value type according 'validaters'
    """
    for key, validator in VALIDATORS.items():
        if validator(param):
            return key
    return "text"


def parse_input_query(query: dict) -> dict:
    """
    parse input query 'key: value' and return 'key: value_type'
    """
    result = {}
    for field_name, value in query.items():
        result[field_name] = parse_param(value)
    return result


def get_template_name(templates: list[dict], form: dict) -> str | None:
    """
    get form and list of templates and return name of template or None
    """
    for template in templates:
        template_name = template["name"]
        rest_template = {k: v for k, v in template.items() if k != "name"}
        if rest_template.items() <= form.items():
            return template_name
    return None
