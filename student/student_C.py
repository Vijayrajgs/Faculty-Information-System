import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE


db = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASS,
    database = DB_DBASE
)

cursor = db.cursor()


st.title("Students Database")


def create_student(stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age):
    insert_query = "INSERT INTO students (stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age)
    cursor.execute(insert_query, values)
    db.commit()


st.header("Add New Student")
stud_no = st.text_input("Student Number", max_chars=12)
stud_fname = st.text_input("First Name", max_chars=200)
stud_mname = st.text_input("Middle Name", max_chars=200)
stud_lname = st.text_input("Last Name", max_chars=200)
stud_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
stud_age = st.text_input("Age", max_chars=200)

if st.button("Add Student"):
    create_student(stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age)
    st.success("Student added to the database")


st.header("Existing Schedule Entries")
cursor.execute("SELECT * FROM students")
schedule_data = cursor.fetchall()

if schedule_data:
    column_names = [description[0] for description in cursor.description]
    
    data_with_columns = [column_names] + list(schedule_data)
    
    st.table(data_with_columns)
else:
    st.info("No schedule entries found.")




db.close()