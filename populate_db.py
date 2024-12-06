import random

from tinydb import TinyDB

NUMBER_OF_RECORDS_TO_INSERT = 20

FIELD_NAMES = [
    "user_name",
    "order_date",
    "lead_email",
    "user_phone",
    "user_date",
    "user_email",
    "order_date",
]
FIELD_VALUES = ["phone", "email", "date", "text"]

db = TinyDB("src/db.json")


def create_random_data() -> dict:
    data = []
    for _ in range(NUMBER_OF_RECORDS_TO_INSERT):
        row = {}
        number_of_elements = random.randint(2, 4)  # noqa: S311
        row["name"] = f"field #{random.randint(10, 99)}"  # noqa: S311
        for _ in range(number_of_elements):
            name = generate_random_name()
            value = generate_random_value()
            row[name] = value
        data.append(row)
    return data


def populate_db() -> None:
    data = create_random_data()
    db.insert_multiple(data)
    print(f"Inserted {len(data)} documents")  # noqa: T201


def generate_random_name() -> str:
    return random.choice(FIELD_NAMES)  # noqa: S311


def generate_random_value() -> str:
    return random.choice(FIELD_VALUES)  # noqa: S311


if __name__ == "__main__":
    populate_db()
