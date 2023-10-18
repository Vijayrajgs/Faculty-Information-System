import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE
from display import display_table_entries
def create_student(cursor, database):
    st.header("Add New Student")
    stud_no = st.text_input("Student Number", max_chars = 12)
    stud_fname = st.text_input("First Name", max_chars = 200)
    stud_mname = st.text_input("Middle Name", max_chars = 200)
    stud_lname = st.text_input("Last Name", max_chars = 200)
    stud_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    stud_age = st.text_input("Age", max_chars = 200)

    if st.button("Add Student"):
        insert_query = "INSERT INTO students (stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (stud_no, stud_fname, stud_mname, stud_lname, stud_gender, stud_age)
        cursor.execute(insert_query, values)
        database.commit()
        st.success("Student added to the database")

def update_student(cursor, database):
    st.header("Update Student")
    cursor.execute("SELECT * FROM students")
    student_data = cursor.fetchall()
    student_to_update = st.selectbox("Select a Student to Update", [student[0] for student in student_data])
    current_student = [student for student in student_data if student[0] == student_to_update][0]
    new_values = {}

    new_values["stud_no"] = st.text_input("New Student Number", value=current_student[1], max_chars = 12)
    new_values["stud_fname"] = st.text_input("New First Name", value=current_student[2], max_chars = 200)
    new_values["stud_mname"] = st.text_input("New Middle Name", value=current_student[3], max_chars = 200)
    new_values["stud_lname"] = st.text_input("New Last Name", value=current_student[4], max_chars = 200)
    new_values["stud_gender"] = st.selectbox("New Gender", ["Male", "Female", "Other"], index = ["Male", "Female", "Other"].index(current_student[5]))
    new_values["stud_age"] = st.text_input("New Age", value=current_student[6], max_chars = 200)

    if st.button("Update Student"):
        update_query = "UPDATE students SET stud_no = %s, stud_fname = %s, stud_mname = %s, stud_lname = %s, stud_gender = %s, stud_age = %s WHERE stud_id = %s"
        values = (new_values["stud_no"], new_values["stud_fname"], new_values["stud_mname"], new_values["stud_lname"], new_values["stud_gender"], new_values["stud_age"], student_to_update)
        cursor.execute(update_query, values)
        database.commit()
        st.success("Student updated")

def delete_student(cursor, database):
    st.header("Delete Student")
    cursor.execute("SELECT * FROM students")
    student_data = cursor.fetchall()
    student_to_delete = st.selectbox("Select a Student to Delete", [student[0] for student in student_data])

    if st.button("Delete Student"):
        delete_query = "DELETE FROM students WHERE stud_id = %s"
        cursor.execute(delete_query, (student_to_delete,))
        database.commit()
        st.success("Student deleted")

def main():
    st.title("Students Database")

    database = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DBASE
    )
    cursor = database.cursor()

    action = st.selectbox("Choose an Action", ["Add Student", "Update Student", "Delete Student"])

    if action == "Add Student":
        create_student(cursor, database)
    elif action == "Update Student":
        update_student(cursor, database)
    elif action == "Delete Student":
        delete_student(cursor, database)

    table_name = "students"
    display_table_entries(cursor, table_name)

    database.close()

if __name__ == "__main__":
    main()
