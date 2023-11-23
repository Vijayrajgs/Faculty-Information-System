import streamlit as st
import mysql.connector

def display_table_entries(cursor, table_name):
    st.header(f"Existing {table_name} Entries")
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()

    if table_data:
        column_names = [description[0] for description in cursor.description]
        data_with_columns = [column_names] + list(table_data)
        st.table(data_with_columns)
    else:
        st.info(f"No {table_name} entries found.")