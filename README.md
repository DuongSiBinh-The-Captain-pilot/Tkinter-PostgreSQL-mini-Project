# Student Management Application

A simple student management system built with **Tkinter** (GUI) and **PostgreSQL** (database).

---

## Features

- ✅ **Add Student**: Insert student name and age into the database
- ✅ **View All Students**: Display all students in a list with ID, name, and age
- ✅ **Delete Student**: Remove selected student from the database
- ✅ **Auto Database Setup**: Automatically creates the `students` table on startup

---

## Prerequisites

Before running the application, ensure you have:

1. **Python 3.x** installed
2. **PostgreSQL** installed and running
3. **psycopg2** package installed

### Installation

```bash
pip install psycopg2-binary
```

---

## Database Configuration

The application connects to PostgreSQL with the following default credentials:

```python
dbname="postgres"
user="postgres"
password="benvip156"
host="localhost"
port="5432"
```

**If your PostgreSQL setup is different, modify the `connect_db()` function in `main.py`:**

```python
def connect_db():
    return psycopg2.connect(
        dbname="your_database",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )
```

---

## How to Use

### Running the Application

```bash
python main.py
```

The application window will open with a simple interface.

### Adding a Student

1. Enter the **student's name** in the "Name" field
2. Enter the **student's age** in the "Age" field
3. Click the **"Add Student"** button
4. The student will be added to the database and appear in the list

### Viewing All Students

- Students are automatically loaded when the app starts
- The list displays: `ID - Name (Age years old)`
- Example: `1 - John Doe (20 years old)`

### Deleting a Student

1. Select a student from the list
2. Click the **"Delete Selected Student"** button
3. The student will be removed from the database and the list will refresh

---

## How to Get Information Using pgAdmin

### Step 1: Open pgAdmin

1. Launch **pgAdmin** (usually accessible at `http://localhost:5050`)
2. Log in with your credentials

### Step 2: Navigate to the Database

1. In the left panel, expand: **Servers → PostgreSQL → Databases → postgres → Schemas → public → Tables**
2. You should see the `students` table

### Step 3: View Student Data

**Option A: Using the GUI**
1. Right-click on the `students` table
2. Select **"View/Edit Data"** → **"All Rows"**
3. All students will be displayed in a table format

**Option B: Using SQL Query**
1. Right-click on the `postgres` database
2. Select **"Query Tool"**
3. Execute any of these SQL commands:

```sql
-- View all students
SELECT * FROM students;

-- View specific columns
SELECT id, name, age FROM students;

-- View students by age
SELECT * FROM students WHERE age > 20;

-- Count total students
SELECT COUNT(*) FROM students;

-- View students sorted by name
SELECT * FROM students ORDER BY name;
```

### Step 4: Refresh pgAdmin

If you don't see updated data after adding/deleting students in the app:
- Right-click on the **Tables** folder → **Refresh**

---

## Database Schema

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER
);
```

- `id`: Auto-incrementing unique identifier
- `name`: Student's name (max 50 characters)
- `age`: Student's age (integer)

---

## File Structure

```
TkinterVsPostgreSQL/
├── main.py              # Main application file
├── README.md            # This file
├── sample_query.sql     # Sample SQL queries
└── streaming-app.py     # Additional app file
```

---

## Troubleshooting

### Error: "relation 'students' does not exist"

**Solution**: The table might not exist in the database. The app automatically creates it on startup, so:
1. Ensure PostgreSQL is running
2. Check your database credentials in `connect_db()`
3. Restart the application

### Error: "psycopg2.OperationalError: could not connect to server"

**Solution**: PostgreSQL is not running or the connection credentials are incorrect
1. Start PostgreSQL service
2. Verify credentials in `connect_db()` function

### Error: "could not translate host name 'localhost'"

**Solution**: Change `host="localhost"` to `host="127.0.0.1"` in the `connect_db()` function

---

## Example SQL Queries

Check the [sample_query.sql](sample_query.sql) file for more query examples.

---

## Author

Created for learning Tkinter and PostgreSQL integration in Python.

---

## License

This project is open source and available for educational purposes.