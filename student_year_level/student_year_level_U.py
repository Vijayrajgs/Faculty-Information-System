import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE


db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_DBASE
)

cursor = db.cursor()

st.title("Students Database")


def update_student_year_level(syl_id, new_values):
    update_query = "UPDATE student_year_level SET stud_id = %s, year_id = %s, schoolyear = %s WHERE syl_id = %s"
    values = (new_values["stud_id"], new_values["year_id"], new_values["schoolyear"], syl_id)
    cursor.execute(update_query, values)
    db.commit()


cursor.execute("SELECT * FROM student_year_level")
student_year_level_data = cursor.fetchall()

st.title("Students Year Level Database")

st.header("Update Student Year Level")
syl_to_update = st.selectbox("Select a Student Year Level to Update", [syl[0] for syl in student_year_level_data])
current_syl = [syl for syl in student_year_level_data if syl[0] == syl_to_update][0]
new_values = {}

new_values["stud_id"] = st.text_input("New Student ID", value=current_syl[1], max_chars=12)
new_values["year_id"] = st.text_input("New Year ID", value=current_syl[2], max_chars=12)
new_values["schoolyear"] = st.text_input("New School Year", value=current_syl[3], max_chars=20)

if st.button("Update Student Year Level"):
    update_student_year_level(syl_to_update, new_values)
    st.success("Student Year Level updated")

st.header("Existing Students Entries")
cursor.execute("SELECT * FROM student_year_level")
student_data = cursor.fetchall()

db.close()
