import streamlit as st
import sqlite3
from datetime import datetime

# ----------------- DATABASE -----------------
conn = sqlite3.connect("hospital.db", check_same_thread=False)
c = conn.cursor()

# Users table
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT,
    avatar_url TEXT
)
""")

# Appointments table
c.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    patient_name TEXT,
    service TEXT,
    date TEXT,
    time TEXT,
    provider TEXT,
    telehealth INTEGER,
    status TEXT,
    created_by TEXT
)
""")
conn.commit()

# ----------------- HELPERS -----------------
def hash_password(password):
    return password[::-1]

def check_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_password(password)))
    return c.fetchone()

def register_user(name, email, password, role, avatar_url):
    try:
        c.execute("INSERT INTO users (name,email,password,role,avatar_url) VALUES (?,?,?,?,?)",
                  (name, email, hash_password(password), role, avatar_url))
        conn.commit()
        return True
    except:
        return False

def create_appointment(patient_name, service, date, time, provider, telehealth, created_by):
    c.execute("""INSERT INTO appointments (patient_name,service,date,time,provider,telehealth,status,created_by)
                 VALUES (?,?,?,?,?,?,?,?)""",
              (patient_name, service, str(date), str(time), provider, int(telehealth), "Pending", created_by))
    conn.commit()

def get_appointments(user_email, role):
    if role=="admin":
        c.execute("SELECT * FROM appointments ORDER BY date DESC")
    elif role=="staff":
        c.execute("SELECT * FROM appointments WHERE provider=? ORDER BY date DESC", (user_email,))
    else:
        c.execute("SELECT * FROM appointments WHERE created_by=? ORDER BY date DESC", (user_email,))
    return c.fetchall()

# ----------------- SESSION -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Thrive Wellness Hospital", layout="wide")

# ----------------- STYLES -----------------
st.markdown("""
<style>
/* Card styling */
.card { background-color:#f5f5f5; padding:20px; border-radius:10px; text-align:center; margin:10px; transition: transform 0.2s; }
.card:hover { transform:translateY(-5px); box-shadow:0px 4px 8px rgba(0,0,0,0.2); }
/* Hero section */
.hero { position: relative; text-align: center; color: white; }
.hero img { width: 100%; height: auto; filter: brightness(0.7); }
.hero-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
.hero-text h1 { font-size: 3em; }
.hero-text button { font-size: 1.2em; padding: 12px 24px; margin: 10px; border-radius: 8px; border:none; background-color:#007ACC; color:white; cursor:pointer; }
.hero-text button:hover { background-color:#005f99; }
</style>
""", unsafe_allow_html=True)

# ----------------- PAGE FUNCTIONS -----------------
def home_page():
    st.markdown("""
    <div class='hero'>
        <img src='images/ai-generated-8722616_1280.jpg' alt='Clinic Hero'>
        <div class='hero-text'>
            <h1>Welcome to Thrive Wellness Hospital</h1>
            <button onclick="window.location.href='#Appointments'">Book Appointment</button>
            <button onclick="window.location.href='#Contact'">Contact Us</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def services_page():
    st.header("Our Services")
    services = [
        {"name":"Medication Management","desc":"Expert management of your medications."},
        {"name":"Psychotherapy","desc":"Individual, group, and family therapy sessions."},
        {"name":"Telehealth","desc":"Secure online therapy sessions."}
    ]
    cols = st.columns(len(services))
    for col, s in zip(cols, services):
        with col:
            st.markdown(f"<div class='card'><h3>{s['name']}</h3><p>{s['desc']}</p></div>", unsafe_allow_html=True)

def staff_page():
    st.header("Meet Our Staff")
    staff_list = [
        {"role":"PMHNP-BC","img":"images/marek-studzinski-Q3J1wmn7_8w-unsplash.jpg"},
        {"role":"Therapist","img":"images/pexels-karolina-grabowska-4226769.jpg"},
        {"role":"Counselor","img":"images/pexels-shvetsa-3845129.jpg"}
    ]
    cols = st.columns(len(staff_list))
    for col, s in zip(cols, staff_list):
        with col:
            st.image(s["img"], width=150)
            st.markdown(f"<h4>{s['role']}</h4>", unsafe_allow_html=True)

def about_page():
    st.header("About Our Clinic")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>Clinic Photo Placeholder</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("**Mission:** Provide quality mental health care.\n\n**Vision:** Promote wellness for all.\n\n**Certifications:** TBD", unsafe_allow_html=True)

def contact_page():
    st.header("Contact Us")
    st.markdown("**Address:** 123 Wellness Ave, Nairobi, Kenya")
    st.markdown("**Phone:** +254 700 000 000")
    st.markdown("**Email:** info@thrivewellness.com")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")
        if submit:
            st.success("Message sent!")

def login_register_page():
    st.header("Login / Register")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login", key="login_btn"):
            user = check_user(email, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success("Logged in successfully!")
            else:
                st.error("Invalid credentials")
    with col2:
        st.subheader("Register")
        name = st.text_input("Full Name", key="reg_name")
        email_r = st.text_input("Email", key="reg_email")
        password_r = st.text_input("Password", type="password", key="reg_pass")
        role = st.selectbox("Role", ["patient","staff"], key="reg_role")
        avatar_url = st.text_input("Avatar URL (optional)", key="avatar_url")
        if st.button("Register", key="reg_btn"):
            if register_user(name,email_r,password_r,role,avatar_url):
                st.success("Registered successfully! Please login.")
            else:
                st.error("Registration failed (maybe email exists)")

def appointments_page():
    st.header("Appointments / Booking")
    if not st.session_state.logged_in:
        st.info("Please login to book appointments.")
        return
    user = st.session_state.user
    with st.form("appointment_form"):
        patient_name = user[1] if user[4]=="patient" else st.text_input("Patient Name")
        service = st.selectbox("Select Service", ["Medication Management","Psychotherapy","Telehealth"])
        date = st.date_input("Select Date")
        time = st.time_input("Select Time")
        provider = st.selectbox("Select Provider", ["PMHNP-BC","Therapist","Counselor"])
        telehealth = st.checkbox("Telehealth Session")
        submit = st.form_submit_button("Book Appointment")
        if submit:
            create_appointment(patient_name, service, date, time, provider, telehealth, user[2])
            st.success(f"Appointment booked for {patient_name} with {provider} on {date} at {time}.")

def dashboard_page():
    st.header("Dashboard")
    user = st.session_state.user
    st.text(f"Hello, {user[1]}")
    if user[5]:
        try:
            st.image(user[5], width=100)
        except:
            st.info("Avatar not available")
    st.subheader("Appointments")
    appointments = get_appointments(user[2], user[4])
    if appointments:
        for appt in appointments:
            st.markdown(f"- {appt[1]} with {appt[5]} on {appt[3]} at {appt[4]} ({appt[7]})")
    else:
        st.info("No appointments yet.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.experimental_rerun()

# ----------------- NAVIGATION -----------------
pages = ["Home","Services","Staff","Appointments","About","Contact","Login/Register"]
if st.session_state.logged_in:
    pages.append("Dashboard")

page = st.sidebar.selectbox("Navigate", pages)

if page=="Home":
    home_page()
elif page=="Services":
    services_page()
elif page=="Staff":
    staff_page()
elif page=="About":
    about_page()
elif page=="Contact":
    contact_page()
elif page=="Login/Register":
    login_register_page()
elif page=="Appointments":
    appointments_page()
elif page=="Dashboard":
    dashboard_page()
