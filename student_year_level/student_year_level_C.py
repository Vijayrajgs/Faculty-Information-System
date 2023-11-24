import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE

try:
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DBASE
    )

    cursor = db.cursor()

    st.title("Students Database")


    def create_student(syl_id, stud_id, year_id, schoolyear):
        insert_query = "INSERT INTO students (syl_id, stud_id, year_id, schoolyear) VALUES (%s, %s, %s, %s)"
        values = (syl_id, stud_id, year_id, schoolyear)
        cursor.execute(insert_query, values)
        db.commit()


    st.header("Add New Student")
    syl_id = st.text_input("Syllabus ID", max_chars=12)
    stud_id = st.text_input("Student ID", max_chars=12)
    year_id = st.text_input("Year ID", max_chars=12)
    schoolyear = st.text_input("School Year", max_chars=20)

    if st.button("Add Student"):
        create_student(syl_id, stud_id, year_id, schoolyear)
        st.success("Student added to the database")


    st.header("Existing Students Entries")
    cursor.execute("SELECT * FROM student_year_level")
    student_data = cursor.fetchall()

    if student_data:
        column_names = [description[0] for description in cursor.description]

        data_with_columns = [column_names] + list(student_data)

        st.table(data_with_columns)
    else:
        st.info("No student entries found.")

except mysql.connector.Error as err:
    st.error(f"Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()