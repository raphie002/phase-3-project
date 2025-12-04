
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore

Base = declarative_base()


# STUDENT MODEL
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    department = Column(String(100))

    # Relationships
    grades = relationship("Grade", back_populates="student", cascade="all, delete-orphan")
    attendance_records = relationship("Attendance", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Student id={self.id}, name={self.name}>"


# INSTRUCTOR MODEL
class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100))

    def __repr__(self):
        return f"<Instructor id={self.id}, name={self.name}>"


# COURSE MODEL
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), nullable=False, unique=True)
    description = Column(String(255))

    # Relationships
    grades = relationship("Grade", back_populates="course", cascade="all, delete-orphan")
    attendance_records = relationship("Attendance", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Course id={self.id}, code={self.code}>"


# GRADES MODEL
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    score = Column(Float)
    letter = Column(String(5))

    student = relationship("Student", back_populates="grades")
    course = relationship("Course", back_populates="grades")

    def __repr__(self):
        return f"<Grade id={self.id}, student={self.student_id}, course={self.course_id}, score={self.score}>"


# ATTENDANCE MODEL
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)  # Present / Absent / Late

    student = relationship("Student", back_populates="attendance_records")
    course = relationship("Course", back_populates="attendance_records")

    def __repr__(self):
        return f"<Attendance id={self.id}, student={self.student_id}, date={self.date}, status={self.status}>"
