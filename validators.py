from datetime import datetime
import re


def is_valid_phone_number(phone):
    # Регулярное выражение для формата +7 xxx xxx xx xx
    pattern = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"

    return bool(re.match(pattern, phone))


def is_valid_date(date_str):
    formats = ["%d.%m.%Y", "%Y-%m-%d"]

    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            pass

    return False


def is_valid_email(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if re.fullmatch(regex, email):
        return True
    else:
        return False
