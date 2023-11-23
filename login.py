import customtkinter as ctk
import subprocess
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_DBASE

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

def Login():
    username = user_name.get()
    password = user_pass.get()

    db_host = DB_HOST
    db_user = DB_USER
    db_pass = DB_PASS
    db_dbase = DB_DBASE

    try:
        connection = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_pass,
            database = db_dbase
        )
        cursor = connection.cursor()

        query = "SELECT * FROM admin WHERE adm_username = %s AND adm_password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            message_label.configure(text = "Login successful !!!")
            subprocess.run(["streamlit", "run", "home.py"])
            app.destroy()
        
        else:
            message_label.configure(text = "Invalid username or password, Try Again!!!")
        connection.close()
    
    except Exception as e:
        print("Error!!!", e)

label = ctk.CTkLabel(app, text = "Faculty information System 👨‍🏫👩‍🏫")
label.pack(pady = 55)

frame = ctk.CTkFrame(master = app)
frame.pack(padx = 10, pady = 12)

user_name = ctk.CTkEntry(master = frame, placeholder_text = "Username")
user_name.pack(padx = 10, pady = 12)

user_pass = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
user_pass.pack(padx = 10, pady = 12)

login_button = ctk.CTkButton(master = frame, text = "Login", command = Login)
login_button.pack(padx = 10, pady = 12)

message_label = ctk.CTkLabel(app, text = "")
message_label.pack(pady = 10)

app.mainloop()