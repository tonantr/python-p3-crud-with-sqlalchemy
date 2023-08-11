#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    # session.add(albert_einstein)
    # session.commit()

    # print(f"New student ID is {albert_einstein.id}.")

    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()

    # students = session.query(Student).all()

    # print(students)

    # names = session.query(Student.name).all()

    # print(names)

    # students_by_name = session.query(
    #         Student.name).order_by(
    #         Student.name).all()

    # print(students_by_name)

    # students_by_grade_desc = session.query(
    #         Student.name, Student.grade).order_by(
    #         desc(Student.grade)).all()

    # print(students_by_grade_desc)

    oldest_student = session.query(
            Student.name, Student.birthday).order_by(
            desc(Student.grade)).limit(1).all()

    print(oldest_student)

    
