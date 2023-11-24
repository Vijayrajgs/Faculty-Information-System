import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE

def create_student(cursor, db, syl_id, stud_id, year_id, schoolyear):
    insert_query = "INSERT INTO students (syl_id, stud_id, year_id, schoolyear) VALUES (%s, %s, %s, %s)"
    values = (syl_id, stud_id, year_id, schoolyear)
    cursor.execute(insert_query, values)
    db.commit()

def update_student_year_level(cursor, db, syl_id, new_values):
    update_query = "UPDATE student_year_level SET stud_id = %s, year_id = %s, schoolyear = %s WHERE syl_id = %s"
    values = (new_values["stud_id"], new_values["year_id"], new_values["schoolyear"], syl_id)
    cursor.execute(update_query, values)
    db.commit()

def delete_student(cursor, db, stud_id):
    delete_query = "DELETE FROM students WHERE stud_id = %s"
    cursor.execute(delete_query, (stud_id,))
    db.commit()

def delete_student_year_level(cursor, db, stud_id):
    delete_query = "DELETE FROM student_year_level WHERE stud_id = %s"
    cursor.execute(delete_query, (stud_id,))
    db.commit()

def main():
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DBASE
    )
    cursor = db.cursor()

    st.title("Students Database")

    action = st.selectbox("Choose an Action", ["Add Student", "Update Student Year Level", "Delete Student"])

    if action == "Add Student":
        st.header("Add New Student")
        syl_id = st.text_input("Syllabus ID", max_chars=12)
        stud_id = st.text_input("Student ID", max_chars=12)
        year_id = st.text_input("Year ID", max_chars=12)
        schoolyear = st.text_input("School Year", max_chars=20)

        if st.button("Add Student"):
            create_student(cursor, db, syl_id, stud_id, year_id, schoolyear)
            st.success("Student added to the database")

    elif action == "Update Student Year Level":
        st.title("Students Year Level Database")
        st.header("Update Student Year Level")

        cursor.execute("SELECT * FROM student_year_level")
        student_year_level_data = cursor.fetchall()

        syl_to_update = st.selectbox("Select a Student Year Level to Update", [syl[0] for syl in student_year_level_data])
        current_syl = [syl for syl in student_year_level_data if syl[0] == syl_to_update][0]
        new_values = {}

        new_values["stud_id"] = st.text_input("New Student ID", value=current_syl[1], max_chars=12)
        new_values["year_id"] = st.text_input("New Year ID", value=current_syl[2], max_chars=12)
        new_values["schoolyear"] = st.text_input("New School Year", value=current_syl[3], max_chars=20)

        if st.button("Update Student Year Level"):
            update_student_year_level(cursor, db, syl_to_update, new_values)
            st.success("Student Year Level updated")

    elif action == "Delete Student":
        st.title("Students Database")
        st.header("Delete Student")

        cursor.execute("SELECT * FROM students")
        student_data = cursor.fetchall()

        student_to_delete = st.selectbox("Select a Student to Delete", [student[0] for student in student_data])

        if st.button("Delete Student"):
            delete_student(cursor, db, student_to_delete)
            delete_student_year_level(cursor, db, student_to_delete)
            st.success("Student and corresponding records deleted")

    # Display existing entries
    st.header("Existing Entries")
    cursor.execute("SELECT * FROM student_year_level")
    schedule_data = cursor.fetchall()

    for entry in schedule_data:
        st.write(entry)

    db.close()

if __name__ == "__main__":
    main()
