from database import db


templates = [
    {
        "name": "User_contacts",
        "username": "text",
        "user_email": "email",
        "user_phone": "phone",
        "created_at": "date",
    },
    {"name": "Order", "user": "text", "ordered": "date"},
]


def fill_db():
    db.truncate()
    for template in templates:
        db.insert(template)


if __name__ == "__main__":
    fill_db()
