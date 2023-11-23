import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE
from display import display_table_entries

def add_admin_entry(cursor, database):
    st.header("Add a New Admin Entry")
    adm_id = st.number_input("Admin ID", min_value=1)
    adm_username = st.text_input("Admin Username", max_chars=200)
    adm_password = st.text_input("Admin Password", max_chars=200, type="password")

    if st.button("Add Admin Entry"):
        insert_query = "INSERT INTO admin (adm_id, adm_username, adm_password) VALUES (%s, %s, %s)"
        values = (adm_id, adm_username, adm_password)
        cursor.execute(insert_query, values)
        database.commit()
        st.success("Admin entry added to the database")

def update_admin_entry(cursor, database):
    st.header("Update Admin Entry")
    cursor.execute("SELECT * FROM admin")
    admin_data = cursor.fetchall()
    entry_to_update = st.selectbox("Select an Entry to Update", [entry[0] for entry in admin_data])
    current_entry = [entry for entry in admin_data if entry[0] == entry_to_update][0]
    new_values = {}

    new_values["adm_username"] = st.text_input("New Admin Username", value=current_entry[1], max_chars=200)
    new_values["adm_password"] = st.text_input("New Admin Password", value=current_entry[2], max_chars=200, type="password")

    if st.button("Update Admin Entry"):
        update_query = "UPDATE admin SET adm_username = %s, adm_password = %s WHERE adm_id = %s"
        values = (new_values["adm_username"], new_values["adm_password"], entry_to_update)
        cursor.execute(update_query, values)
        database.commit()
        st.success("Admin entry updated")

def delete_admin_entry(cursor, database):
    st.header("Delete Admin Entry")
    cursor.execute("SELECT * FROM admin")
    admin_data = cursor.fetchall()
    entry_to_delete = st.selectbox("Select an entry to delete", [entry[0] for entry in admin_data])

    if st.button("Delete Admin Entry"):
        delete_query = "DELETE FROM admin WHERE adm_id = %s"
        cursor.execute(delete_query, (entry_to_delete,))
        database.commit()
        st.success("Admin entry deleted!!")

def main():
    st.title("Admin Management")

    database = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DBASE
    )
    cursor = database.cursor()

    action = st.selectbox("Choose an Action", ["Add Admin Entry", "Update Admin Entry", "Delete Admin Entry"])

    if action == "Add Admin Entry":
        add_admin_entry(cursor, database)
    elif action == "Update Admin Entry":
        update_admin_entry(cursor, database)
    elif action == "Delete Admin Entry":
        delete_admin_entry(cursor, database)

    table_name = "admin"
    display_table_entries(cursor, table_name)

    database.close()

if __name__ == "__main__":
    main()
