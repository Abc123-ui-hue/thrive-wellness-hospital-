import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("hospital.db", check_same_thread=False)
c = conn.cursor()

# Users Table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)""")

# Appointments Table
c.execute("""CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    service TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    provider TEXT NOT NULL,
    telehealth TEXT,
    status TEXT,
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")

# Reports Table
c.execute("""CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    treatment TEXT NOT NULL,
    solution TEXT NOT NULL,
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
conn.commit()

# ---------------- AUTH FUNCTIONS ----------------
def register_user(fullname, email, password, role):
    if not fullname or not email or not password or not role:
        return "missing"  # validation failed
    try:
        c.execute("INSERT INTO users (fullname, email, password, role) VALUES (?, ?, ?, ?)",
                  (fullname.strip(), email.strip(), password.strip(), role))
        conn.commit()
        return "success"
    except sqlite3.IntegrityError:
        return "exists"

def login_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    return c.fetchone()

# ---------------- DATA FUNCTIONS ----------------
def create_appointment(patient_name, service, date, time, provider, telehealth, created_by):
    c.execute("""INSERT INTO appointments 
              (patient_name, service, date, time, provider, telehealth, status, created_by) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
              (patient_name, service, str(date), str(time), provider, telehealth, "Pending", created_by))
    conn.commit()

def get_appointments():
    c.execute("SELECT * FROM appointments ORDER BY created_at DESC")
    return c.fetchall()

def create_report(patient_name, treatment, solution, created_by):
    c.execute("INSERT INTO reports (patient_name, treatment, solution, created_by) VALUES (?, ?, ?, ?)",
              (patient_name, treatment, solution, created_by))
    conn.commit()

def get_reports():
    c.execute("SELECT * FROM reports ORDER BY created_at DESC")
    return c.fetchall()

# ---------------- PAGE FUNCTIONS ----------------
def home_page():
    st.title("🏥 Thrive Wellness Hospital")
    st.subheader("Welcome to our digital portal")

def login_register_page():
    st.title("🔐 Login / Register")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state["user"] = user
                st.success("✅ Logged in successfully!")
            else:
                st.error("❌ Invalid credentials.")

    with tab2:
        fullname = st.text_input("Full Name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        role = st.selectbox("Role", ["patient", "staff", "admin"])
        if st.button("Register"):
            result = register_user(fullname, email, password, role)
            if result == "success":
                st.success("✅ Account created. Please login.")
            elif result == "exists":
                st.error("⚠️ Email already exists. Try logging in.")
            elif result == "missing":
                st.error("⚠️ Please fill in all fields.")

def appointment_page():
    st.title("📅 Book Appointment")
    if "user" not in st.session_state:
        st.warning("Please login first.")
        return
    patient_name = st.text_input("Patient Name")
    service = st.selectbox("Select Service", ["Medication Management", "Psychotherapy", "Telehealth"])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    provider = st.selectbox("Select Provider", ["PMHNP-BC", "Therapist", "Counselor"])
    telehealth = st.selectbox("Telehealth", ["Yes", "No"])
    if st.button("Book Appointment"):
        create_appointment(patient_name, service, date, time, provider, telehealth, st.session_state["user"][1])
        st.success("✅ Appointment booked successfully!")

def staff_page():
    st.title("🩺 Staff Dashboard")
    if "user" not in st.session_state or st.session_state["user"][4] not in ["staff", "admin"]:
        st.warning("Access restricted to staff/admin.")
        return

    st.subheader("Write Patient Report")
    patient_name = st.text_input("Patient Name")
    treatment = st.text_area("Treatment")
    solution = st.text_area("Solution")
    if st.button("Submit Report"):
        create_report(patient_name, treatment, solution, st.session_state["user"][1])
        st.success("✅ Report submitted.")

    st.subheader("📋 All Reports")
    reports = get_reports()
    for r in reports:
        st.write(f"**Patient:** {r[1]} | **Treatment:** {r[2]} | **Solution:** {r[3]} | By: {r[4]} | At: {r[5]}")

def admin_page():
    st.title("⚙️ Admin Dashboard")
    if "user" not in st.session_state or st.session_state["user"][4] != "admin":
        st.warning("Access restricted to admin.")
        return

    st.subheader("📅 All Appointments")
    appointments = get_appointments()
    for a in appointments:
        st.write(f"Patient: {a[1]} | Service: {a[2]} | Date: {a[3]} | Time: {a[4]} | Provider: {a[5]} | Status: {a[6]} | By: {a[7]}")

def contact_page():
    st.title("📞 Contact Us")
    st.write("Address: 123 Wellness Ave, Nairobi, Kenya")
    st.write("Phone: +254 700 000 000")
    st.write("Email: info@thrivewellness.com")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("✅ Message sent successfully!")

# ---------------- MAIN APP ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Login/Register", "Book Appointment", "Staff", "Admin", "Contact Us"])

if page == "Home":
    home_page()
elif page == "Login/Register":
    login_register_page()
elif page == "Book Appointment":
    appointment_page()
elif page == "Staff":
    staff_page()
elif page == "Admin":
    admin_page()
elif page == "Contact Us":
    contact_page()

# Logout button
if "user" in st.session_state:
    if st.sidebar.button("Logout"):
        del st.session_state["user"]
        st.success("✅ Logged out successfully.")
