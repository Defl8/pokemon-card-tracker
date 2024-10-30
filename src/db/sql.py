import sqlite3


# TODO: Maybe remove later?
def connect_to_db(db_name: str) -> sqlite3.Connection:
    """Connect to a database

    Args:
    db_name(str): The name of the database to connect to.

    Returns:
    sqlite3 Connection object.
    """
    conn: sqlite3.Connection = sqlite3.connect(database=db_name)
    return conn


def make_sql_table(table_statement: str, db_name: str) -> bool:
    with sqlite3.connect(db_name) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
