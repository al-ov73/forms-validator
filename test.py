from src.parser import get_template_name, parse_input_query, parse_param
from src.validators import is_valid_date, is_valid_email, is_valid_phone_number


def test_parse_param() -> None:
    assert parse_param("+7 123 456 78 90") == "phone"
    assert parse_param("2023-12-31") == "date"
    assert parse_param("31.12.2023") == "date"
    assert parse_param("test@example.com") == "email"
    assert parse_param("random text") == "text"
    print("test_parse_param passed")


def test_parse_input_query() -> None:
    query = {
        "contact": "+7 123 456 78 90",
        "birth_date": "31.12.2023",
        "email": "test@example.com",
        "note": "random text",
    }
    expected = {
        "contact": "phone",
        "birth_date": "date",
        "email": "email",
        "note": "text",
    }
    assert parse_input_query(query) == expected
    print("test_parse_input_query passed")


def test_get_template_name() -> None:
    templates = [
        {"name": "template1", "field1": "value1", "field2": "value2"},
        {"name": "template2", "field1": "value3", "field3": "value4"},
    ]

    form1 = {"field1": "value1", "field2": "value2"}
    form2 = {"field1": "value3", "field3": "value4"}
    form3 = {"field1": "value1", "field3": "value2"}

    assert get_template_name(templates, form1) == "template1"
    assert get_template_name(templates, form2) == "template2"
    assert get_template_name(templates, form3) is None
    print("test_get_template_name passed")


def test_is_valid_phone_number() -> None:
    assert is_valid_phone_number("+7 123 456 78 90") == True
    assert is_valid_phone_number("+7 123 4567 890") == False
    assert is_valid_phone_number("123 456 78 90") == False
    assert is_valid_phone_number("+7 123 456 78") == False
    print("test_is_valid_phone_number passed")


def test_is_valid_date() -> None:
    assert is_valid_date("31.12.2023") == True
    assert is_valid_date("2023-12-31") == True
    assert is_valid_date("31/12/2023") == False
    assert is_valid_date("12-31-2023") == False
    print("test_is_valid_date passed")


def test_is_valid_email() -> None:
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name+tag+sorting@example.com") == True
    assert is_valid_email("plainaddress") == False
    assert is_valid_email("@missingusername.com") == False
    assert is_valid_email("username@.com") == False
    print("test_is_valid_email passed")


if __name__ == "__main__":
    test_parse_param()
    test_parse_input_query()
    test_get_template_name()
    test_is_valid_phone_number()
    test_is_valid_date()
    test_is_valid_email()
    print("All tests passed!")
