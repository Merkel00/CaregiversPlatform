from datetime import date, datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import select
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Time,
    Float, event, text
)

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String,  DDL
from sqlalchemy.orm import aliased
from sqlalchemy import delete

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5434/db_ass')

Session = sessionmaker(bind=engine)
session = Session()

# ddl = DDL("CREATE SCHEMA IF NOT EXISTS assignment")
# event.listen(Base.metadata, 'before_create', ddl)


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "myschema"}
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    given_name = Column(String)
    surname = Column(String)
    city = Column(String)
    phone_number = Column(String)
    profile_description = Column(String)
    password = Column(String)


class Caregiver(Base):
    __tablename__ = "caregiver"
    __table_args__ = {"schema": "myschema"}
    caregiver_user_id = Column(
        Integer, ForeignKey("myschema.user.user_id"), primary_key=True
    )
    photo = Column(String)
    gender = Column(String)
    caregiving_type = Column(String)
    hourly_rate = Column(Float)


class Member(Base):
    __tablename__ = "member"
    __table_args__ = {"schema": "myschema"}
    member_user_id = Column(Integer, ForeignKey("myschema.user.user_id"), primary_key=True)
    house_rules = Column(String)


class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema": "myschema"}
    member_user_id = Column(
        Integer, ForeignKey("myschema.member.member_user_id"), primary_key=True
    )
    house_number = Column(String)
    street = Column(String)
    town = Column(String)


class Job(Base):
    __tablename__ = "job"
    __table_args__ = {"schema": "myschema"}
    job_id = Column(Integer, primary_key=True)
    member_user_id = Column(Integer, ForeignKey("myschema.member.member_user_id"))
    required_caregiving_type = Column(String)
    other_requirements = Column(String)
    date_posted = Column(Date)


class JobApplication(Base):
    __tablename__ = "job_application"
    __table_args__ = {"schema": "myschema"}
    caregiver_user_id = Column(Integer, ForeignKey("myschema.caregiver.caregiver_user_id"))
    job_id = Column(Integer, ForeignKey("myschema.job.job_id"))
    date_applied = Column(Date, primary_key=True)


class Appointment(Base):
    __tablename__ = "appointment"
    __table_args__ = {"schema": "myschema"}
    appointment_id = Column(Integer, primary_key=True)
    caregiver_user_id = Column(Integer, ForeignKey("myschema.caregiver.caregiver_user_id"))
    member_user_id = Column(Integer, ForeignKey("myschema.member.member_user_id"))
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    work_hours = Column(Float)
    status = Column(String)

#
# engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/postgres')
# engine.execute("CREATE SCHEMA IF NOT EXISTS testscheme")
Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()


new_user = Appointment(
    caregiver_user_id=17,
    member_user_id=8,
    appointment_date='2023-11-28',
    appointment_time='12:00:00',
    work_hours=4.0,
    status='Accepted'
)





#session.add(new_user)
# caregiver_to_delete = session.query(Job).filter_by(job_id=2).first()
#

# session.delete(caregiver_to_delete)

#2.3.1
#
# askar = session.query(User).filter_by(given_name='Askar', surname='Askarov').first()
# askar.phone_number = '+77771010001'

#2.3.2
# caregivers = session.query(Caregiver).all()
#
# for caregiver in caregivers:
#     if caregiver.hourly_rate < 9:
#         caregiver.hourly_rate += 0.5 #adding 0.5
#     else:
#         caregiver.hourly_rate *= 1.1 #comission 10%

#2.4.1

# bolat = session.query(Job).join(Member).join(User).filter(
#     User.given_name == 'Bolat', User.surname == 'Bolatov'
# ).all()
#
# for job in bolat:
#     session.query(JobApplication).filter(JobApplication.job_id == job.job_id).update(
#         {JobApplication.job_id: None}, synchronize_session=False
#     )
#
# for job in bolat:
#     session.delete(job)

#2.4.2


# turan_members = session.query(Member).join(Address).filter(Address.street == 'Turan Street').all()
#
# for member in turan_members:
#     session.query(Appointment).filter(Job.member_user_id == member.member_user_id).delete()
#
# for member in turan_members:
#     session.query(JobApplication).filter(Job.member_user_id == member.member_user_id).delete()
#
# for member in turan_members:
#     session.query(Job).filter(Job.member_user_id == member.member_user_id).delete()
#
#
# for member in turan_members:
#     session.query(Address).filter(Address.member_user_id == member.member_user_id).delete()
#
# for member in turan_members:
#     session.delete(member)




session.commit()


session.close()

# users = session.query(User).all()
#
# for user in users:
#     print(f"User ID: {user.user_id}, Phone: {user.phone_number},Email: {user.email}, Name: {user.given_name} {user.surname}, City: {user.city}")
#
# caregivers = session.query(Caregiver).all()
#
# for user in caregivers:
#     print(f"Caregiver ID: {user.caregiver_user_id}, Type: {user.caregiving_type}, "
#           f"Hourly Rate: {user.hourly_rate}")
#
# members = session.query(Member).all()
#
# for user in members:
#     print(f"Member ID: {user.member_user_id}, House Rules: {user.house_rules}")
#
# jobs = session.query(Job).all()
#
# for user in jobs:
#     print(f"Job ID: {user.job_id}, Required Type: {user.required_caregiving_type}, Date posted: {user.date_posted}")
#
# applicants = session.query(JobApplication).all()
#
# for user in applicants:
#     print(f"Job ID: {user.job_id}, Caregiver ID: {user.caregiver_user_id}, Date applied: {user.date_applied}")
#
# appointments = session.query(Appointment).all()
#
# for user in appointments:
#     print(f"Caregiver ID: {user.caregiver_user_id}, Member ID: {user.member_user_id}, Date: {user.appointment_date},"
#           f"Time: {user.appointment_time}, Work hours: {user.work_hours}, Status: {user.status}")
# user_caregiver = aliased(User, name='user_caregiver')
#
# user_member = aliased(User, name='user_member')


#2.5.1


# accepted = (
#     session.query(Appointment, Caregiver, Member, user_caregiver, user_member)
#     .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .join(Member, Appointment.member_user_id == Member.member_user_id)
#     .join(user_caregiver, Appointment.caregiver_user_id == user_caregiver.user_id)
#     .join(user_member, Appointment.member_user_id == user_member.user_id)
#     .filter(Appointment.status == 'Accepted')
#     .all()
# )
#
# for appointment, caregiver, member, caregiver_user, member_user in accepted:
#     caregiver_name = f"{caregiver_user.given_name} {caregiver_user.surname}"
#     member_name = f"{member_user.given_name} {member_user.surname}"
#     print(f"Caregiver: {caregiver_name}, Member: {member_name}")



# #2.5.2
# gentle = (
#     session.query(Job.job_id)
#     .filter(Job.other_requirements=='Gentle')
#     .all()
# )
#
# gentle_ids = [job.job_id for job in gentle]
# print(f"Job IDs with Gentle requirement: {gentle_ids}")


# #2.5.3
# baby_sitter = (
#     session.query(Appointment, User, Caregiver, Member)
#     .join(User, Appointment.caregiver_user_id == User.user_id)
#     .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .join(Member, Appointment.member_user_id == Member.member_user_id)
#     .filter(Caregiver.caregiving_type == 'Baby Sitter')
#     .all()
# )
# 
# for appointment, user, caregiver, member in baby_sitter:
#     print(f"Work hours: {appointment.work_hours}")


# #2.5.4
# elderly_care = (
#     session.query(Member, User, Address)
#     .join(User, Member.member_user_id == User.user_id)
#     .join(Address, Member.member_user_id == Address.member_user_id)
#     .filter(Address.town == 'Astana', Member.house_rules == 'No pets')
#     .all()
# )
#
# for member, user, address in elderly_care:
#     member_name = f"{user.given_name} {user.surname}"
#     print(f"Member Name: {member_name}, Address: {address.street}, "
#           f"{address.town}, House Rules: {member.house_rules}")


# from sqlalchemy import func
#
#
# member_user_id = 2
#
# job_count = (
#     session.query(Job.job_id, func.count(JobApplication.job_id).label('count'))
#         .join(JobApplication, Job.job_id == JobApplication.job_id)
#         .join(Member, Job.member_user_id == Member.member_user_id)
#         .filter(Member.member_user_id == member_user_id)
#         .group_by(Job.job_id)
#         .all()
# )
#
# for job_id, count in job_count:
#     print(f"Applicant Count: {count}")
#
# total_hours = (
#     session.query(func.sum(Appointment.work_hours).label('total_hours'))
#     .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .filter(Appointment.status == 'Accepted')
#     .all()
# )
#
#
# for result in total_hours:
#     print(f"Total Hours: {result.total_hours}")
#
# average_pay = (
#     session.query(func.avg(Appointment.work_hours * Caregiver.hourly_rate))
#     .filter(Appointment.status == 'Accepted')
#     .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .scalar()
# )
#
# print(f"Average Pay: ${average_pay}")
#
#
# above_average = (
#     session.query(Caregiver)
#     .join(Appointment, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .filter(Appointment.status == 'Accepted')
#     .group_by(Caregiver.caregiver_user_id)
#     .having(func.sum(Appointment.work_hours * Caregiver.hourly_rate) > average_pay)
#     .all()
# )
#
# for caregiver in above_average:
#     print(f"Caregiver ID: {caregiver.caregiver_user_id}")
#


#
# total = (
#     session.query(func.sum(Appointment.work_hours * Caregiver.hourly_rate))
#     .filter(Appointment.status == 'Accepted')
#     .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
#     .scalar()
# )
#
# print(f"Total cost: ${total}")


# job_applications = (
#     session.query(JobApplication, User, Caregiver, Job)
#     .join(User, JobApplication.caregiver_user_id == User.user_id)
#     .join(Caregiver, JobApplication.caregiver_user_id == Caregiver.caregiver_user_id)
#     .join(Job, JobApplication.job_id == Job.job_id)
#     .all()
# )
#
#
# for job_application, user, caregiver, job in job_applications:
#     name = f"{user.given_name} {user.surname}"
#     print(f"Job Title: {job.required_caregiving_type }, Applicant: {name}")

