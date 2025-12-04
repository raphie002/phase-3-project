# Students Enrollment & Records Management System (SERMS)
A full backend CLI-based school management system built with Python, SQLAlchemy ORM, Alembic migrations, and SQLite.
It manages Students, Courses, Grades, and Attendance, with full CRUD support through an intuitive text-based interface.

## Features
Students
   - Add new students
   - List all students
   - Update stedent details
   - Delete students

Courses
   - Add courses
   - Update course details
   - List all courses
   - Delete courses

Grades
   - Assign grades to students
   - Update grades
   - Delete grades
   - View all grade records

Attendance
   - Record attendance per student per course
   - Update attendance
   - Delete attendace logs
   - View all attendance history

System Features
   - SQLAlchemy ORM
   - Alembic migrations with versioning
   - Databases seeding using seed.py
   - Clean, modular CLI (in lib/cli.py)

## Technology Stack
| Component        | Tool               |
| :-------         | -------:           |
| **Language**     | Python3            |
| **ORM**          | SQLAlchemy         |
| **Migrations**   | Alembic            |
| **Database**     | SQLite             |
| **Interface**    | Command-Line (CLI) |

## Installation & Setup
  1. Clone the repository:
     ```
     git clone <repository_url>
     cd <repository_folder>
     ```
  
  2. Create / Activate virtual environment:
     ```
     pipenv install
     pipenv shell
     ```
  3. Apply database migrations:
     ```
     alembic upgrade head
     ```
  4. Seed the database:
     ```
     python3 lib/seed.py
     ```
  5. Running the application:
     ```
     python3 lib/cli.py
     ```
     You should see the main menu:
     ```
     === SCHOOL MANAGEMENT SYSTEM ===
     1. Students
     2. Courses
     3. Grades
     4. Attendance
     5. Exit
     ```

## Database Schema

Student
   - id
   - name
   - age
   - department

Course
   - id
   - name
   - code
   - description

Grade
   - id
   - student_id
   - course_id
   - score
   - letter

Attendance
   - id
   - student_id
   - course_id
   - date
   - status

## CRUD Examples (SQLAlchemy ORM)
Create a student
   ```
   new_student = Student(name="John Doe", age=21, department="Computer Science")
   session.add(new_student)
   session.commit()
   ```

Fetch all courses
   ```
   courses = session.query(Course).all()
   ```

Update grade
   ```
   grade = session.query(Grade).get(1)
   grade.score = 88
   grade.letter = "B+"
   session.commit()
   ```

Delete attendance record
   ```
   record = session.query(Attendance).get(3)
   session.delete(record)
   session.commit()
   ```

## Expected Outcomes
   - Fully functional school records management system
   - Clean database architecture with migrations
   - Robust CRUD operations
   - Clear separation of models, migrations, CLI logic, and seeding


## Author
Raphael Njoroge