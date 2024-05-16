import json
import os
import sqlite3
import pandas as pd


def load_json(file_name: str):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    with open (file_path, "r") as file:
        data = json.load(file)
    return data


def create_database_with_data(json_data: dict, connection: sqlite3.Connection):
    """
    Er wordt een database gebouwd op basis van een json structuur. Als een tabel 
    gebouwd is, wordt ze gevuld met data.

    Deze brondata bevat zowel de metadata van de tabellen als de echte data.

    Parameters
    ----------
    json_data: dict
        De brondata die zowel metadata als data van de tabellen bevat.
    connection: sqlite3.Connection
        De connectie naar de in memory databas.
    """
    cursor = connection.cursor()
    # Create all the tables
    for table_name, table_data in json_data.items():
        metadata = table_data['metadata']
        fields = ', '.join([f"{field['name']} {field['type']}" for field in metadata['fields']])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        cursor.execute(create_table_query)

        # Insert data per table
        for row in table_data['data']:
            columns = ', '.join(row.keys())
            placeholders = ', '.join(['?' for _ in range(len(row))])
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(insert_query, list(row.values()))

    # Commit the statements
    connection.commit()
    # Close the cursor
    cursor.close()


def extract_hobbys(connection: sqlite3.Connection) -> pd.DataFrame:
    """
    Ophalen van hobbydata.

    Parameters
    ----------
    connection: sqlite3.Connection
        De connectie naar de in memory database

    Returns
    -------
    pd.DataFrame
    """
    sql_query = "select hobby from hobby"
    hobby_panda = pd.read_sql_query(sql_query, connection)
    return hobby_panda


def extract_opleiding(connection: sqlite3.Connection) -> pd.DataFrame:
    """
    Ophalen van data die te maken heeft met de opleiding. 

    Parameters
    ----------
    connection: sqlite3.Connection
        De connectie naar de in memory database

    Returns
    -------
    pd.DataFrame
    """
    sql_query = "select S.instelling, D.diploma, O.status_diploma, O.afstudeerjaar, O.module, O.status_module from opleiding O " \
                "left outer join Diploma D on O.diploma_id = D.id " \
                "left outer join School S on O.school_id = S.id"
    opleiding_panda = pd.read_sql_query(sql_query, connection)
    return opleiding_panda


def extract_werkervaring(connection: sqlite3.Connection) -> pd.DataFrame:
    """
    Ophalen van data die te maken heeft met de werkervaring. 

    Parameters
    ----------
    connection: sqlite3.Connection
        De connectie naar de in memory database

    Returns
    -------
    pd.DataFrame
    """
    sql_query = "select W.functie, WG.werkgever, W.van, W.tot from werkervaring W left outer join werkgever WG on W.werkgever_id = WG.id"
    werkervaring_panda = pd.read_sql_query(sql_query, connection)
    return werkervaring_panda
