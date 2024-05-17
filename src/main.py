import sqlite3

import pandas as pd
from database import convert_pandas_to_json_file, load_json, create_database_with_data, extract_werkervaring, extract_hobbys, extract_opleiding
from generate_html import generate_index_html

def database_and_html_and_json_files(json_brondata: dict, css_file: str, js_file: str):
    # Connect to the SQLite database (in-memory)
    connection = sqlite3.connect(":memory:")

    # Create the tables and fill it with data
    create_database_with_data(json_brondata, connection)

    # Extract it again
    hobby_panda = extract_hobbys(connection)
    opleiding_panda = extract_opleiding(connection)
    werkervaring_panda = extract_werkervaring(connection)

    # Close the connection
    connection.close()

    convert_pandas_to_json_file(hobby_panda, "hobby.json")
    convert_pandas_to_json_file(opleiding_panda, "opleiding.json")
    convert_pandas_to_json_file(werkervaring_panda, "werkervaring.json")

    generate_index_html(css_file=css_file, js_file=js_file)

    
if __name__ == "__main__":
    css_file = "styles.css"
    js_file = "interactie.js"
    json_file = "brondata.json"

    json_brondata = load_json(json_file)

    database_and_html_and_json_files(json_brondata=json_brondata, css_file=css_file, js_file=js_file)
    