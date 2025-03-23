# Student Management System

This is a **Flask-based web application** for managing student information. The application allows users to:
- Add new students.
- View all students in a table.
- Edit student details.
- Delete students.
- Search and filter students dynamically using AJAX.

## Features

1. **Add Students**: Users can add a student's name, department, and email. The email field is unique and prevents duplicate entries.
2. **View Students**: All students are displayed in a table with their details.
3. **Edit Students**: Users can edit a student's information.
4. **Delete Students**: Users can delete a student's record.
5. **Search Students**: A search bar allows users to filter students dynamically by name, department, or email using AJAX.

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate
- **Frontend**: HTML, Bootstrap, JavaScript (AJAX)
- **Database**: MySQL
- **ORM**: SQLAlchemy

## Prerequisites

- Python 3.x
- MySQL server
- `pip` (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/insert_database.git
   cd insert_database
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Ensure MySQL is running.
   - Create a database named `insert_database` in MySQL.

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open the application in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
insert_database/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── migrations/            # Flask-Migrate migration files
├── templates/             # HTML templates
│   ├── form.html          # Main page with form and student table
│   ├── edit.html          # Edit student page
│   ├── student_table.html # Partial template for AJAX filtering
├── .gitignore             # Git ignore file
└── README.md              # Project description
```

## Screenshots

### Add Student Form
![Add Student Form](https://via.placeholder.com/800x400?text=Add+Student+Form)

### Student Table with AJAX Search
![Student Table](https://via.placeholder.com/800x400?text=Student+Table+with+Search)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Developed by **Your Name**. Feel free to reach out for any questions or suggestions!