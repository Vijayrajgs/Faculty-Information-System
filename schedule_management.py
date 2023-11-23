import streamlit as st
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE
from display import display_table_entries
def add_schedule_entry(cursor, database):
    st.header("Add a New Schedule Entry")
    sched_id = st.text_input("Schedule ID")
    timehr = st.text_input("Time", max_chars = 20)
    days = st.text_input("Days", max_chars = 20)
    teach_id = st.text_input("Teacher ID")
    yls_id = st.text_input("Year Level ID")
    schoolyear = st.text_input("School Year", max_chars = 20)
    room = st.text_input("Room", max_chars = 20)

    if st.button("Add Schedule"):
        insert_query = "INSERT INTO schedule (sched_id, timehr, days, teach_id, yls_id, schoolyear, room) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (sched_id, timehr, days, teach_id, yls_id, schoolyear, room)
        cursor.execute(insert_query, values)
        database.commit()
        st.success("Schedule added to the database")

def update_schedule_entry(cursor, database):
    st.header("Update Schedule Entry")
    cursor.execute("SELECT * FROM schedule")
    schedule_data = cursor.fetchall()
    entry_to_update = st.selectbox("Select an Entry to Update", [entry[0] for entry in schedule_data])
    current_entry = [entry for entry in schedule_data if entry[0] == entry_to_update][0]
    new_values = {}
    
    new_values["timehr"] = st.text_input("New Time", value=current_entry[1], max_chars = 20)
    new_values["days"] = st.text_input("New Days", value=current_entry[2], max_chars = 20)
    new_values["teach_id"] = st.number_input("New Teacher ID", value=current_entry[3], min_value = 1)
    new_values["yls_id"] = st.number_input("New Year Level ID", value=current_entry[4], min_value = 1)
    new_values["schoolyear"] = st.text_input("New School Year", value=current_entry[5], max_chars = 20)
    new_values["room"] = st.text_input("New Room", value=current_entry[6], max_chars = 20)

    if st.button("Update Schedule"):
        update_query = "UPDATE schedule SET timehr = %s, days = %s, teach_id = %s, yls_id = %s, schoolyear = %s, room = %s WHERE sched_id = %s"
        values = (new_values["timehr"], new_values["days"], new_values["teach_id"], new_values["yls_id"], new_values["schoolyear"], new_values["room"], entry_to_update)
        cursor.execute(update_query, values)
        database.commit()
        st.success("Schedule updated")

def delete_schedule_entry(cursor, database):
    st.header("Delete Schedule Entry")
    cursor.execute("SELECT * FROM schedule")
    scheduled_data = cursor.fetchall()
    entry_to_delete = st.selectbox("Select an entry to delete", [entry[0] for entry in scheduled_data])

    if st.button("Delete Schedule"):
        delete_query = "DELETE FROM schedule WHERE sched_id = %s"
        cursor.execute(delete_query, (entry_to_delete,))
        database.commit()
        st.success("Schedule entry deleted!!")


def main():
    st.title("Schedule Management")
    
    database = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASS,
        database = DB_DBASE
    )
    cursor = database.cursor()
    
    action = st.selectbox("Choose an Action", ["Create Schedule Entry", "Update Schedule Entry", "Delete Schedule Entry"])
    
    if action == "Create Schedule Entry":
        add_schedule_entry(cursor, database)
    elif action == "Update Schedule Entry":
        update_schedule_entry(cursor, database)
    elif action == "Delete Schedule Entry":
        delete_schedule_entry(cursor, database)
    
    table_name = "schedule"
    display_table_entries(cursor, table_name)
    
    database.close()

if __name__ == "__main__":
    main()

# import streamlit as st
# import mysql.connector
# import logging
# from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE
# from display import display_table_entries

# # Setting up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def create_trigger_and_procedure(cursor, database):
#     try:
#         # Drop the trigger if it already exists
#         cursor.execute("DROP TRIGGER IF EXISTS after_schedule_insert")

#         # Create Trigger
#         cursor.execute("""
#             CREATE TRIGGER after_schedule_insert
#             AFTER INSERT ON schedule
#             FOR EACH ROW
#             BEGIN
#                 INSERT INTO schedule_log (sched_id, action_type, action_timestamp)
#                 VALUES (NEW.sched_id, 'INSERT', NOW());
#             END;
#         """)
#         st.success("Trigger created successfully")
#         logger.info("Trigger created successfully")

#         # Drop the procedure if it already exists
#         cursor.execute("DROP PROCEDURE IF EXISTS update_schedule_time")

#         # Create Stored Procedure
#         cursor.execute("""
#             CREATE PROCEDURE update_schedule_time(IN p_sched_id INT, IN p_new_time VARCHAR(255))
#             BEGIN
#                 UPDATE schedule
#                 SET timehr = p_new_time
#                 WHERE sched_id = p_sched_id;
#             END;
#         """)
#         st.success("Procedure created successfully")
#         logger.info("Procedure created successfully")

#         database.commit()

#     except Exception as e:
#         st.error("An error occurred while creating Trigger and Procedure.")
#         logger.error(f"Error in create_trigger_and_procedure: {e}")



# def add_schedule_entry(cursor, database):
#     st.header("Add a New Schedule Entry")
    
#     try:
#         sched_id = st.text_input("Schedule ID")
#         timehr = st.text_input("Time", max_chars=20)
#         days = st.text_input("Days", max_chars=20)
#         teach_id = st.text_input("Teacher ID")
#         yls_id = st.text_input("Year Level ID")
#         schoolyear = st.text_input("School Year", max_chars=20)
#         room = st.text_input("Room", max_chars=20)

#         if st.button("Add Schedule"):
#             # Validate inputs
#             if not all([sched_id, timehr, days, teach_id, yls_id, schoolyear, room]):
#                 st.error("All fields must be filled.")
#                 return

#             insert_query = "INSERT INTO schedule (sched_id, timehr, days, teach_id, yls_id, schoolyear, room) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             values = (sched_id, timehr, days, teach_id, yls_id, schoolyear, room)
#             cursor.execute(insert_query, values)
#             database.commit()
#             st.success("Schedule added to the database")
#             logger.info(f"Schedule added with ID: {sched_id}")

#     except Exception as e:
#         st.error("An error occurred while adding the schedule.")
#         logger.error(f"Error in add_schedule_entry: {e}")

# def update_schedule_entry(cursor, database):
#     st.header("Update Schedule Entry")

#     try:
#         cursor.execute("SELECT * FROM schedule")
#         schedule_data = cursor.fetchall()
#         entry_to_update = st.selectbox("Select an Entry to Update", [entry[0] for entry in schedule_data])
#         current_entry = [entry for entry in schedule_data if entry[0] == entry_to_update][0]
#         new_values = {}

#         new_values["timehr"] = st.text_input("New Time", value=current_entry[1], max_chars=20)
#         new_values["days"] = st.text_input("New Days", value=current_entry[2], max_chars=20)
#         new_values["teach_id"] = st.number_input("New Teacher ID", value=current_entry[3], min_value=1)
#         new_values["yls_id"] = st.number_input("New Year Level ID", value=current_entry[4], min_value=1)
#         new_values["schoolyear"] = st.text_input("New School Year", value=current_entry[5], max_chars=20)
#         new_values["room"] = st.text_input("New Room", value=current_entry[6], max_chars=20)

#         if st.button("Update Schedule"):
#             update_query = "UPDATE schedule SET timehr = %s, days = %s, teach_id = %s, yls_id = %s, schoolyear = %s, room = %s WHERE sched_id = %s"
#             values = (
#                 new_values["timehr"], new_values["days"], new_values["teach_id"],
#                 new_values["yls_id"], new_values["schoolyear"], new_values["room"], entry_to_update
#             )
#             cursor.execute(update_query, values)
#             database.commit()
#             st.success("Schedule updated")
#             logger.info(f"Schedule updated with ID: {entry_to_update}")

#     except Exception as e:
#         st.error("An error occurred while updating the schedule.")
#         logger.error(f"Error in update_schedule_entry: {e}")

# def delete_schedule_entry(cursor, database):
#     st.header("Delete Schedule Entry")

#     try:
#         cursor.execute("SELECT * FROM schedule")
#         scheduled_data = cursor.fetchall()
#         entry_to_delete = st.selectbox("Select an entry to delete", [entry[0] for entry in scheduled_data])

#         if st.button("Delete Schedule"):
#             delete_query = "DELETE FROM schedule WHERE sched_id = %s"
#             cursor.execute(delete_query, (entry_to_delete,))
#             database.commit()
#             st.success("Schedule entry deleted!!")
#             logger.info(f"Schedule deleted with ID: {entry_to_delete}")

#     except Exception as e:
#         st.error("An error occurred while deleting the schedule entry.")
#         logger.error(f"Error in delete_schedule_entry: {e}")

# def main():
#     st.title("Schedule Management")

#     try:
#         database = mysql.connector.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASS,
#             database=DB_DBASE
#         )
#         cursor = database.cursor()

#         create_trigger_and_procedure(cursor, database)

#         action = st.selectbox("Choose an Action", ["Create Schedule Entry", "Update Schedule Entry", "Delete Schedule Entry"])

#         if action == "Create Schedule Entry":
#             add_schedule_entry(cursor, database)
#         elif action == "Update Schedule Entry":
#             update_schedule_entry(cursor, database)
#         elif action == "Delete Schedule Entry":
#             delete_schedule_entry(cursor, database)

#         table_name = "schedule"
#         display_table_entries(cursor, table_name)

#     except Exception as e:
#         st.error("An error occurred while connecting to the database.")
#         logger.error(f"Error in main: {e}")

#     finally:
#         if 'database' in locals() and database.is_connected():
#             database.close()

# if __name__ == "__main__":
#     main()
