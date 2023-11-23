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

# Streamlit UI elements
st.title("Students Database")

# Function to delete a student
def delete_student(stud_id):
    delete_query = "DELETE FROM students WHERE stud_id = %s"
    cursor.execute(delete_query, (stud_id,))
    db.commit()


cursor.execute("SELECT * FROM students")
student_data = cursor.fetchall()


st.title("Students Database")


st.header("Delete Student")
student_to_delete = st.selectbox("Select a Student to Delete", [student[0] for student in student_data])

if st.button("Delete Student"):
    delete_student(student_to_delete)
    st.success("Student deleted")


st.header("Existing Students")
for student in student_data:
    st.write(student)


db.close()

