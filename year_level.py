import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE
from display import display_table_entries

def add_year_entry(cursor, database):
    st.header("Add a New Year Entry")
    year_id = st.number_input("Year ID", min_value=1)
    year_level = st.text_input("Year Level", max_chars=200)
    section = st.text_input("Section", max_chars=12)

    if st.button("Add Year Entry"):
        insert_query = "INSERT INTO year_level (year_id, year_level, section) VALUES (%s, %s, %s)"
        values = (year_id, year_level, section)
        cursor.execute(insert_query, values)
        database.commit()
        st.success("Year entry added to the database")

def update_year_entry(cursor, database):
    st.header("Update Year Entry")
    cursor.execute("SELECT * FROM year_level")
    year_data = cursor.fetchall()
    entry_to_update = st.selectbox("Select an Entry to Update", [entry[0] for entry in year_data])
    current_entry = [entry for entry in year_data if entry[0] == entry_to_update][0]
    new_values = {}

    new_values["year_level"] = st.text_input("New Year Level", value=current_entry[1], max_chars=200)
    new_values["section"] = st.text_input("New Section", value=current_entry[2], max_chars=12)

    if st.button("Update Year Entry"):
        update_query = "UPDATE year_level SET year_level = %s, section = %s WHERE year_id = %s"
        values = (new_values["year_level"], new_values["section"], entry_to_update)
        cursor.execute(update_query, values)
        database.commit()
        st.success("Year entry updated")

def delete_year_entry(cursor, database):
    st.header("Delete Year Entry")
    cursor.execute("SELECT * FROM year_level")
    year_data = cursor.fetchall()
    entry_to_delete = st.selectbox("Select an entry to delete", [entry[0] for entry in year_data])

    if st.button("Delete Year Entry"):
        delete_query = "DELETE FROM year_level WHERE year_id = %s"
        cursor.execute(delete_query, (entry_to_delete,))
        database.commit()
        st.success("Year entry deleted!!")

def main():
    st.title("Year Level Management")

    database = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DBASE
    )
    cursor = database.cursor()

    action = st.selectbox("Choose an Action", ["Add Year Entry", "Update Year Entry", "Delete Year Entry"])

    if action == "Add Year Entry":
        add_year_entry(cursor, database)
    elif action == "Update Year Entry":
        update_year_entry(cursor, database)
    elif action == "Delete Year Entry":
        delete_year_entry(cursor, database)

    table_name = "year_level"
    display_table_entries(cursor, table_name)

    database.close()

if __name__ == "__main__":
    main()
