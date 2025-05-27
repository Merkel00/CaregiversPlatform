# CaregiversPlatform
Online Caregivers Platform

## Project Overview

The platform allows:
- Caregivers to register, set their rates, and apply to jobs
- Family members to register, post job ads, search for caregivers, and make appointments
- Both sides to view and manage applications and appointments

The project consists of:
- Relational database schema in **PostgreSQL**
- Python scripts using **SQLAlchemy** to interact with the database
- Optional bonus: web interface using **Flask**

## Technologies Used

- Python 3
- PostgreSQL
- SQLAlchemy (ORM and raw SQL)
- (Optional) Flask for web app
- Jupyter Notebook / PyCharm / DataGrip for development

## Database Schema

The platform uses the following schema:

- `USER(user_id, email, given_name, surname, city, phone_number, profile_description, password)`
- `CAREGIVER(caregiver_user_id, photo, gender, caregiving_type, hourly_rate)`
- `MEMBER(member_user_id, house_rules)`
- `ADDRESS(member_user_id, house_number, street, town)`
- `JOB(job_id, member_user_id, required_caregiving_type, other_requirements, date_posted)`
- `JOB_APPLICATION(caregiver_user_id, job_id, date_applied)`
- `APPOINTMENT(appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status)`

## How to Run

1. **Install dependencies**  
   ```bash
   pip install sqlalchemy psycopg2

2. **Set up PostgreSQL database**  
   Create a new PostgreSQL database
   Import the schema and data:
   psql -U your_user -d your_db -f caregivers_platform.sql

3. **Run the script**
   Update main.py with your DB credentials, then run:
   python main.py
