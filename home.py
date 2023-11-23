## Home page

import streamlit as st
from st_pages import Page, show_pages, add_page_title, Section

page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1508615121316-fe792af62a63?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2940&q=80");
    background-size: cover;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""

st.markdown(page_bg_image, unsafe_allow_html = True)

st.title("Faculty Information System 👨‍🏫 👩‍🏫")

st.write("""
### About the Database

The Faculty Information System is powered by a database that stores information about faculty members.

Our Faculty Information System is a comprehensive database that houses critical information about our esteemed faculty members. This database serves as a centralized repository for faculty data, enabling efficient management and retrieval of information.


Feel free to explore the system using the navigation menu on the left.
""")

# show_pages(
#     [
#         Page("home.py", "Home", "🏠", in_section = False),

#         Section(name = "Schedule", icon = "📆"),
#             Page("schedule_C.py", "Create Schedule", "📆"),
#             Page("schedule_U.py", "Update Schedule", "📆"),
#             Page("schedule_D.py", "Delete Schedule", "📆"),
#         Page("schedule_D.py", "Delete Schedule", "📆", in_section = False),
#         # Section(name = "Students", icon = "🧑‍🎓")
#     ]
# )

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("schedule_management.py", "Schedule", "🕰️"),
        Page("student.py", "Student", "🧑‍🎓"),
        # Page("", "Page 2", ":books:"),
        # Section(name = "My section", icon="🎈️"),
        # # Pages after a section will be indented
        # Page("schedule_D.py", icon="💪"),
        # # Unless you explicitly say in_section=False
        # Page("student_year.py", icon = "💪", in_section= False)
    ]
)