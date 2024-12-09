from validators import is_valid_date, is_valid_email, is_valid_phone_number


validators = {
    "phone": is_valid_phone_number,
    "date": is_valid_date,
    "email": is_valid_email,
}


def parse_param(param):
    for key, validator in validators.items():
        if validator(param):
            return key
    return "text"


def parse_input_query(query: dict) -> dict:
    result = {}
    for field_name, value in query.items():
        result[field_name] = parse_param(value)
    return result


def get_template_name(templates: list[dict], form: dict) -> str | None:
    for template in templates:
        template_name = template["name"]
        rest_template = {k: v for k, v in template.items() if k != "name"}
        if rest_template.items() <= form.items():
        # if all(
        #     key in rest_template and form[key] == rest_template[key] for key in form
        # ):
            return template_name
    return None
