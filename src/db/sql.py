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
    """Make a table in the specified database.

    Args:
    table_statement(str): the table creation query in sqlite format.
    db_name(str): The name of the database to connect to.

    Returns:
    Boolean representing whether the table creation was successful or not.
    """
    try:
        # Auto close connection when statement finishes.
        with sqlite3.connect(db_name) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            _ = cursor.execute(table_statement)
            conn.commit()
            return True
    except sqlite3.OperationalError as err:
        print(f"Operational error when trying to make table. ERROR: {err}")
        return False
