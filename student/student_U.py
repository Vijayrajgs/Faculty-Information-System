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

def update_student(stud_id, new_values):
    update_query = "UPDATE students SET stud_no = %s, stud_fname = %s, stud_mname = %s, stud_lname = %s, stud_gender = %s, stud_age = %s WHERE stud_id = %s"
    values = (new_values["stud_no"], new_values["stud_fname"], new_values["stud_mname"], new_values["stud_lname"], new_values["stud_gender"], new_values["stud_age"], stud_id)
    cursor.execute(update_query, values)
    db.commit()


cursor.execute("SELECT * FROM students")
student_data = cursor.fetchall()


st.title("Students Database")


st.header("Update Student")
student_to_update = st.selectbox("Select a Student to Update", [student[0] for student in student_data])
current_student = [student for student in student_data if student[0] == student_to_update][0]
new_values = {}


new_values["stud_no"] = st.text_input("New Student Number", value=current_student[1], max_chars=12)
new_values["stud_fname"] = st.text_input("New First Name", value=current_student[2], max_chars=200)
new_values["stud_mname"] = st.text_input("New Middle Name", value=current_student[3], max_chars=200)
new_values["stud_lname"] = st.text_input("New Last Name", value=current_student[4], max_chars=200)
new_values["stud_gender"] = st.selectbox("New Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(current_student[5]))
new_values["stud_age"] = st.text_input("New Age", value=current_student[6], max_chars=200)

if st.button("Update Student"):
    update_student(student_to_update, new_values)
    st.success("Student updated")


st.header("Existing Students")
for student in student_data:
    st.write(student)

db.close()