from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/insert_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('form.html', students=students)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']

    # Insert data into the database
    student = Student(name=name, department=department, email=email)
    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return render_template('form.html', students=Student.query.all(), error="Email already exists!")

    return redirect(url_for('index'))
@app.route('/student_table')
def student_table():
    students = Student.query.all()
    return render_template('student_table.html', students=students)

@app.route('/filter', methods=['GET'])
def filter_students():
    query = request.args.get('query', '')
    students = Student.query.filter(
        (Student.name.ilike(f'%{query}%')) |
        (Student.department.ilike(f'%{query}%')) |
        (Student.email.ilike(f'%{query}%'))
    ).all()
    return render_template('student_table.html', students=students)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.department = request.form['department']
        student.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
