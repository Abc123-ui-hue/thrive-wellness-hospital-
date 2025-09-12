import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DATABASE ----------------
conn = sqlite3.connect("hospital.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    service TEXT,
    date TEXT,
    time TEXT,
    provider TEXT
)
""")
conn.commit()

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- AUTH FUNCTIONS ----------------
def register_user(fullname, email, password, role):
    try:
        c.execute("INSERT INTO users (fullname, email, password, role) VALUES (?, ?, ?, ?)",
                  (fullname, email, password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    return c.fetchone()

# ---------------- PAGES ----------------
def home_page():
    st.title("🏥 Thrive Wellness Hospital")
    st.write("Welcome to **Thrive Wellness Hospital Portal**.")
    st.write("Please use the sidebar to navigate.")

def about_page():
    st.title("ℹ️ About Our Clinic")
    st.write("We provide professional and compassionate healthcare services.")

def services_page():
    st.title("🛎 Our Services")
    st.write("- Medication Management\n- Psychotherapy\n- Telehealth")

def contact_page():
    st.title("📞 Contact Us")
    st.write("**Address:** 123 Wellness Ave, Nairobi, Kenya")
    st.write("**Phone:** +254 700 000 000")
    st.write("**Email:** info@thrivewellness.com")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Message sent successfully!")

def login_register_page():
    st.title("🔑 Login / Register")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.role = user[4]
                st.session_state.user = user
                st.success("Logged in successfully!")
            else:
                st.error("Invalid credentials.")

    with tab2:
        fullname = st.text_input("Full Name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        role = st.selectbox("Role", ["patient", "staff", "admin"])
        if st.button("Register"):
            if register_user(fullname, email, password, role):
                st.success("Account created. Please login.")
            else:
                st.error("Email already exists.")

def patient_page():
    st.title("👩‍⚕️ Patient Dashboard")
    st.subheader("Book Appointment")
    name = st.text_input("Patient Name")
    service = st.selectbox("Service", ["Medication Management", "Psychotherapy", "Telehealth"])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    provider = st.text_input("Provider")
    if st.button("Book"):
        c.execute("INSERT INTO appointments (patient_name, service, date, time, provider) VALUES (?, ?, ?, ?, ?)",
                  (name, service, str(date), str(time), provider))
        conn.commit()
        st.success("Appointment booked!")

def staff_page():
    st.title("👨‍⚕️ Staff Dashboard")
    st.subheader("View Appointments")
    c.execute("SELECT * FROM appointments")
    rows = c.fetchall()
    if rows:
        for r in rows:
            st.write(f"📌 {r[1]} | {r[2]} on {r[3]} at {r[4]} with {r[5]}")
    else:
        st.info("No appointments found.")

def admin_page():
    st.title("🛠 Admin Dashboard")
    st.subheader("Manage Users")
    c.execute("SELECT fullname, email, role FROM users")
    users = c.fetchall()
    if users:
        for u in users:
            st.write(f"👤 {u[0]} | {u[1]} | {u[2]}")
    else:
        st.info("No users registered.")

# ---------------- MAIN APP ----------------
st.sidebar.title("🌐 Navigation")

if st.session_state.logged_in:
    st.sidebar.write(f"Welcome, **{st.session_state.user[1]}** ({st.session_state.role})")
    page = st.sidebar.radio("Go to", ["Home", "About", "Services", "Contact", "Patient", "Staff", "Admin", "Logout"])

    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Services":
        services_page()
    elif page == "Contact":
        contact_page()
    elif page == "Patient" and st.session_state.role == "patient":
        patient_page()
    elif page == "Staff" and st.session_state.role == "staff":
        staff_page()
    elif page == "Admin" and st.session_state.role == "admin":
        admin_page()
    elif page == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user = None
        st.success("Logged out successfully!")

else:
    page = st.sidebar.radio("Go to", ["Home", "About", "Services", "Contact", "Login/Register"])
    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Services":
        services_page()
    elif page == "Contact":
        contact_page()
    elif page == "Login/Register":
        login_register_page()
