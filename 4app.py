import streamlit as st
import sqlite3
from hashlib import sha256
from datetime import datetime
import pandas as pd
import plotly.express as px

# ---------- Page Config ----------
st.set_page_config(page_title="Thrive Mental Wellness", layout="wide")

# ---------- CSS Styling ----------
st.markdown("""
<style>
.stApp { background: linear-gradient(to right, #e0f7fa, #e1bee7); color: #0a3d62; }
h1,h2,h3,h4 { color:#0a3d62; font-family: 'Helvetica', sans-serif; }
.card { background-color: rgba(255,255,255,0.9); border-radius: 15px; padding: 20px; margin-bottom:20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);}
div.stButton > button { background-color:#0a3d62; color:white; border-radius:10px; height:40px; width:220px; font-size:16px; }
div.stButton > button:hover { background-color:#3c6382; }
.stTabs [role="tab"] { color:#0a3d62; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------- Database Setup ----------
conn = sqlite3.connect("hospital.db", check_same_thread=False)
c = conn.cursor()

# Users Table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT,
    bio TEXT,
    phone TEXT,
    qualifications TEXT
)""")

# Requests / Appointments Table
c.execute("""CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    staff_id INTEGER,
    service TEXT,
    date TEXT,
    time TEXT,
    telehealth TEXT,
    status TEXT DEFAULT 'Pending',
    payment_status TEXT DEFAULT 'Unpaid',
    notes TEXT,
    FOREIGN KEY(patient_id) REFERENCES users(id),
    FOREIGN KEY(staff_id) REFERENCES users(id)
)""")

# Reports Table
c.execute("""CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    staff_id INTEGER,
    date TEXT,
    symptoms TEXT,
    diagnosis TEXT,
    treatment TEXT,
    prescriptions TEXT,
    follow_up TEXT,
    attached_docs TEXT
)""")

conn.commit()

# ---------- Helper Functions ----------
def hash_password(password): return sha256(password.encode()).hexdigest()
def register_user(name,email,password,role='patient',bio="",phone="",qualifications=""):
    try: 
        c.execute("INSERT INTO users (name,email,password,role,bio,phone,qualifications) VALUES (?,?,?,?,?,?,?)",
                  (name,email,hash_password(password),role,bio,phone,qualifications)); conn.commit(); return True
    except sqlite3.IntegrityError: return False
def login_user(email,password): 
    c.execute("SELECT * FROM users WHERE email=? AND password=?",(email,hash_password(password)))
    return c.fetchone()
def create_appointment(patient_id,service,date,time,staff_id=None,telehealth="No"):
    c.execute("INSERT INTO appointments (patient_id,service,date,time,staff_id,telehealth) VALUES (?,?,?,?,?,?)",
              (patient_id,service,date,time,staff_id,telehealth))
    conn.commit()
def get_user_appointments(patient_id):
    c.execute("SELECT * FROM appointments WHERE patient_id=?",(patient_id,))
    return c.fetchall()
def get_all_appointments(): 
    c.execute("""SELECT appointments.id, u1.name as patient_name, u2.name as staff_name, appointments.service, appointments.date, appointments.time,
                 appointments.telehealth, appointments.status, appointments.payment_status 
                 FROM appointments 
                 LEFT JOIN users u1 ON appointments.patient_id=u1.id
                 LEFT JOIN users u2 ON appointments.staff_id=u2.id""")
    return c.fetchall()
def update_appointment_status(app_id,status): c.execute("UPDATE appointments SET status=? WHERE id=?",(status,app_id)); conn.commit()
def mark_payment(app_id,status): c.execute("UPDATE appointments SET payment_status=? WHERE id=?",(status,app_id)); conn.commit()
def submit_report(patient_id,staff_id,date,symptoms,diagnosis,treatment,prescriptions,follow_up="",attached_docs=""):
    c.execute("INSERT INTO reports (patient_id,staff_id,date,symptoms,diagnosis,treatment,prescriptions,follow_up,attached_docs) VALUES (?,?,?,?,?,?,?,?,?)",
              (patient_id,staff_id,date,symptoms,diagnosis,treatment,prescriptions,follow_up,attached_docs))
    conn.commit()
def get_patient_reports(patient_id): c.execute("SELECT * FROM reports WHERE patient_id=?",(patient_id,)); return c.fetchall()
def get_all_reports():
    c.execute("""SELECT reports.id, u1.name as patient, u2.name as staff, date, symptoms, diagnosis, treatment, prescriptions, follow_up, attached_docs
                 FROM reports
                 LEFT JOIN users u1 ON reports.patient_id=u1.id
                 LEFT JOIN users u2 ON reports.staff_id=u2.id""")
    return c.fetchall()
def get_kpi():
    c.execute("SELECT COUNT(*) FROM users WHERE role='patient'"); total_patients=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE role='staff'"); total_staff=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM appointments"); total_apps=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM appointments WHERE status='Pending'"); pending=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM appointments WHERE status='Approved'"); approved=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM appointments WHERE status='Canceled'"); canceled=c.fetchone()[0]
    return total_patients,total_staff,total_apps,pending,approved,canceled

# ---------- Navigation ----------
menu = ["Home","About Us","Services","Contact","Staff Profiles","Login/Register"]
choice = st.sidebar.selectbox("Navigate", menu)

# ---------- Public Pages ----------
if choice=="Home":
    st.markdown('<div class="card"><h1>Welcome to Thrive Mental Wellness</h1><p>Comprehensive, professional mental wellness services.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Our Services</h3><ul><li>Medication Management</li><li>Psychotherapy (Individual, Group, Family)</li><li>Telehealth</li></ul></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Featured Staff</h3><p>Cecilia Wamburu PMHNP-BC</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Testimonials</h3><p>"Best care I have ever received!" - Patient A</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Mental Health Tips</h3><p>Stay hydrated, exercise, and sleep well.</p></div>',unsafe_allow_html=True)

elif choice=="About Us":
    st.markdown('<div class="card"><h2>About Thrive Mental Wellness</h2><p>Our mission: Provide professional mental health care to all patients.</p></div>',unsafe_allow_html=True)

elif choice=="Services":
    st.markdown('<div class="card"><h2>Services Offered</h2><ul><li>Medication Management</li><li>Psychotherapy (Individual, Group, Family)</li><li>Telehealth/Online Therapy</li></ul></div>',unsafe_allow_html=True)

elif choice=="Contact":
    st.markdown('<div class="card"><h2>Contact Us</h2><p>Email: contact@thrivewellness.com | Phone: +254700000000</p><p>Clinic Address: Nairobi, Kenya</p></div>',unsafe_allow_html=True)

elif choice=="Staff Profiles":
    st.markdown('<div class="card"><h2>Our Staff</h2><p>Cecilia Wamburu PMHNP-BC</p></div>',unsafe_allow_html=True)

elif choice=="Login/Register":
    tab1, tab2 = st.tabs(["Login","Register"])
    with tab1:
        email=st.text_input("Email"); password=st.text_input("Password",type="password")
        if st.button("Login"):
            user=login_user(email,password)
            if user: st.session_state['user']=user; st.success(f"Welcome {user[1]}! Role: {user[4]}")
            else: st.error("Invalid credentials")
    with tab2:
        name=st.text_input("Full Name"); email_reg=st.text_input("Email"); password_reg=st.text_input("Password",type="password")
        role=st.selectbox("Role",["patient","staff","admin"])
        if st.button("Register"):
            if register_user(name,email_reg,password_reg,role):
                st.success("Registration successful!")
            else: st.error("Email already exists!")

# ---------- Dashboard / Logged-in Users ----------
if 'user' in st.session_state:
    user=st.session_state['user']
    st.markdown(f'<div class="card"><h2>Dashboard | {user[4].capitalize()}</h2><p>Welcome {user[1]}</p></div>',unsafe_allow_html=True)
    
    # Patient Dashboard
    if user[4]=="patient":
        tab1, tab2, tab3 = st.tabs(["Appointments","Reports","Payments"])
        with tab1:
            st.markdown('<h3>Book Appointment</h3>',unsafe_allow_html=True)
            service=st.selectbox("Service",["Medication Management","Psychotherapy"])
            date=st.date_input("Date"); time=st.text_input("Time"); tele=st.selectbox("Telehealth?",["Yes","No"])
            if st.button("Book Appointment"):
                create_appointment(user[0],service,str(date),time,telehealth=tele)
                st.success("Appointment booked!")
            st.markdown('<h3>My Appointments</h3>',unsafe_allow_html=True)
            apps=get_user_appointments(user[0])
            for a in apps:
                st.info(f"{a[3]} on {a[4]} at {a[5]} | Telehealth: {a[6]} | Status: {a[7]} | Payment: {a[8]}")

        with tab2:
            st.markdown('<h3>My Reports</h3>',unsafe_allow_html=True)
            reports=get_patient_reports(user[0])
            for r in reports:
                st.info(f"Date: {r[3]} | Symptoms: {r[4]} | Diagnosis: {r[5]} | Treatment: {r[6]} | Prescriptions: {r[7]}")

        with tab3:
            st.markdown('<h3>Payments</h3>',unsafe_allow_html=True)
            for a in apps:
                status=a[8]
                if status=="Unpaid" and st.button(f"Mark Paid for {a[3]}"):
                    mark_payment(a[0],"Paid")
                    st.success("Payment updated!")

    # Staff Dashboard
    elif user[4]=="staff":
        tab1,tab2,tab3=st.tabs(["My Patients","Reports","Appointments"])
        with tab1:
            st.markdown('<h3>Assigned Patients</h3>',unsafe_allow_html=True)
            apps=get_all_appointments()
            for a in apps:
                if a[2]==user[1] or a[2]==None:
                    st.info(f"Patient: {a[1]} | Service: {a[3]} | Date: {a[4]} | Status: {a[7]}")
        with tab2:
            st.markdown('<h3>Create Reports</h3>',unsafe_allow_html=True)
            c.execute("SELECT id,name FROM users WHERE role='patient'"); patients=c.fetchall()
            patient_select=st.selectbox("Select Patient",[f"{p[1]}|{p[0]}" for p in patients])
            symptoms=st.text_area("Symptoms"); diagnosis=st.text_area("Diagnosis"); treatment=st.text_area("Treatment"); prescriptions=st.text_area("Prescriptions"); date=datetime.today()
            if st.button("Submit Report"):
                pid=int(patient_select.split("|")[1])
                submit_report(pid,user[0],str(date),symptoms,diagnosis,treatment,prescriptions)
                st.success("Report submitted!")

        with tab3:
            st.markdown('<h3>Appointments</h3>',unsafe_allow_html=True)
            apps=get_all_appointments()
            for a in apps:
                if a[2]==user[1]:
                    st.info(f"Patient: {a[1]} | Service: {a[3]} | Date: {a[4]} | Status: {a[7]}")

    # Admin Dashboard
    elif user[4]=="admin":
        tab1,tab2,tab3,tab4=st.tabs(["Users","Appointments","Reports","Analytics"])
        with tab1:
            st.markdown('<h3>Manage Users</h3>',unsafe_allow_html=True)
            c.execute("SELECT id,name,email,role FROM users"); users=c.fetchall()
            for u in users: st.info(f"{u[1]} | {u[2]} | Role: {u[3]}")
        with tab2:
            st.markdown('<h3>Appointments Management</h3>',unsafe_allow_html=True)
            apps=get_all_appointments()
            for a in apps:
                st.info(f"Patient: {a[1]} | Staff: {a[2]} | Service: {a[3]} | Date: {a[4]} | Status: {a[7]} | Payment: {a[8]}")
                cols=st.columns(2)
                if cols[0].button(f"Approve {a[0]}"): update_appointment_status(a[0],"Approved"); st.success("Approved")
                if cols[1].button(f"Cancel {a[0]}"): update_appointment_status(a[0],"Canceled"); st.error("Canceled")
        with tab3:
            st.markdown('<h3>Reports</h3>',unsafe_allow_html=True)
            reports=get_all_reports()
            for r in reports:
                st.info(f"Patient: {r[1]} | Staff: {r[2]} | Date: {r[3]} | Diagnosis: {r[5]} | Treatment: {r[6]}")
        with tab4:
            st.markdown('<h3>Analytics</h3>',unsafe_allow_html=True)
            total_patients,total_staff,total_apps,pending,approved,canceled=get_kpi()
            st.success(f"Total Patients: {total_patients}")
            st.info(f"Total Staff: {total_staff}")
            st.warning(f"Pending Appointments: {pending}")
            st.success(f"Approved Appointments: {approved}")
            st.error(f"Canceled Appointments: {canceled}")

    # Logout
    if st.button("Logout"):
        del st.session_state['user']
        st.success("Logged out successfully.")
