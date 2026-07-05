import tkinter as tk
from tkinter import messagebox
import psycopg2

# ---------------- DATABASE CONNECTION ----------------

def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="<your_password>",
        host="localhost",
        port="5432"
    )

def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# ---------------- CRUD FUNCTIONS ----------------

def add_student():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, age) VALUES (%s, %s)",
            (name, age)
        )
        conn.commit()
        cur.close()
        conn.close()

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

        load_students()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def load_students():
    student_list.delete(0, tk.END)

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, age FROM students")
        rows = cur.fetchall()

        for row in rows:
            student_list.insert(
                tk.END, f"{row[0]} - {row[1]} ({row[2]} years old)"
            )

        cur.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_student():
    selected = student_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a student")
        return

    student_id = student_list.get(selected[0]).split(" - ")[0]

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        cur.close()
        conn.close()

        load_students()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI ----------------

init_db()
root = tk.Tk()
root.title("Student Management App")
root.geometry("400x400")

# Labels & Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Delete Selected Student", 
            command=delete_student).pack(pady=5)

# Listbox
student_list = tk.Listbox(root, width=50)
student_list.pack(pady=10)

load_students()

root.mainloop()