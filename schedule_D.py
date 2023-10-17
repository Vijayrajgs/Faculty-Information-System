import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE

database = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASS,
    database = DB_DBASE
)

cursor = database.cursor()

def delete_scheduled_data(sched_id):
    delete_query = "DELETE FROM schedule WHERE sched_id = %s"
    cursor.execute(delete_query, (sched_id,))
    database.commit()


cursor.execute("SELECT * FROM schedule")
scheduled_data = cursor.fetchall()

st.title("Schedule Deletion")

st.header("Delete Schedule Entry")

entry_to_delete = st.selectbox("Select an entry to delete", [entry[0] for entry in scheduled_data])

if st.button("Delete Schedule"):
    delete_scheduled_data(entry_to_delete)
    st.success("Schedule entry deleted!!")

st.header("Existing Schedule Entries")
for entry in scheduled_data:
    st.write(entry)

database.close()
