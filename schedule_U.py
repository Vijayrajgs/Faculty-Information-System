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

st.title("Schedule Updation")

def update_schedule_entry(sched_id, new_values):
    update_query = "UPDATE schedule SET timehr = %s, days = %s, teach_id = %s, yls_id = %s, schoolyear = %s, room = %s WHERE sched_id = %s"
    values = (new_values["timehr"], new_values["days"], new_values["teach_id"], new_values["yls_id"], new_values["schoolyear"], new_values["room"], sched_id)
    cursor.execute(update_query, values)
    database.commit()

cursor.execute("SELECT * FROM schedule")
schedule_data = cursor.fetchall()
st.header("Update Schedule Entry")
entry_to_update = st.selectbox("Select an Entry to Update", [entry[0] for entry in schedule_data])
current_entry = [entry for entry in schedule_data if entry[0] == entry_to_update][0]
new_values = {}

new_values["timehr"] = st.text_input("New Time", value=current_entry[1], max_chars=20)
new_values["days"] = st.text_input("New Days", value=current_entry[2], max_chars=20)
new_values["teach_id"] = st.number_input("New Teacher ID", value=current_entry[3], min_value=1)
new_values["yls_id"] = st.number_input("New Year Level ID", value=current_entry[4], min_value=1)
new_values["schoolyear"] = st.text_input("New School Year", value=current_entry[5], max_chars=20)
new_values["room"] = st.text_input("New Room", value=current_entry[6], max_chars=20)

if st.button("Update Schedule"):
    update_schedule_entry(entry_to_update, new_values)
    st.success("Schedule updated")


st.header("Existing Schedule Entries")
cursor.execute("SELECT * FROM schedule")
schedule_data = cursor.fetchall()

for entry in schedule_data:
    st.write(entry)

database.close()