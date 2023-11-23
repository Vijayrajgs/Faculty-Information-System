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

st.title("Schedule Creation")

st.header("Add a New Schedule Entry")
sched_id = st.text_input("Schedule ID")
timehr = st.text_input("Time", max_chars=20)
days = st.text_input("Days", max_chars=20)
teach_id = st.text_input("Teacher ID")
yls_id = st.text_input("Year Level ID")
schoolyear = st.text_input("School Year", max_chars=20)
room = st.text_input("Room", max_chars=20)

if st.button("Add Schedule"):
    
    insert_query = "INSERT INTO schedule (sched_id, timehr, days, teach_id, yls_id, schoolyear, room) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (sched_id, timehr, days, teach_id, yls_id, schoolyear, room)
    cursor.execute(insert_query, values)
    database.commit()
    st.success("Schedule added to the database")


# st.header("Existing Schedule Entries")
# cursor.execute("SELECT * FROM schedule")
# schedule_data = cursor.fetchall()

st.header("Existing Schedule Entries")
cursor.execute("SELECT * FROM schedule")
schedule_data = cursor.fetchall()

if schedule_data:
    column_names = [description[0] for description in cursor.description]
    
    data_with_columns = [column_names] + list(schedule_data)
    
    st.table(data_with_columns)
else:
    st.info("No schedule entries found.")


# for entry in schedule_data:
#     st.write(entry)

database.close()