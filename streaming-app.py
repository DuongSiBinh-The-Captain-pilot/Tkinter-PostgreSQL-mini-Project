import streamlit as st
import psycopg2
import pandas as pd

# PostgreSQL connection function
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="turtlecode"
    )

# App title
st.title("📇 Contacts App")

# Form to add a new contact
with st.form(key='add_contact_form'):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    submit_button = st.form_submit_button(label='Add Contact')

if submit_button:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s)",
        (first_name, last_name, email)
    )
    conn.commit()
    cur.close()
    conn.close()
    st.success(f"{first_name} {last_name} has been added successfully!")

# Display existing contacts
conn = get_connection()
df = pd.read_sql("SELECT * FROM contacts;", conn)
st.subheader("📋 Saved Contacts")
st.dataframe(df)
conn.close()