import streamlit as st
import sqlite3
from datetime import datetime

# ----------------- DATABASE SETUP -----------------
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
              (patient_name, service, str(date), str(time), provider, telehealth, "Pending", created_by))
    conn.commit()

def get_appointments(user_email, role):
    if role=="admin":
        c.execute("SELECT * FROM appointments ORDER BY date DESC")
    elif role=="staff":
        c.execute("SELECT * FROM appointments WHERE provider=? ORDER BY date DESC", (user_email,))
    else:
        c.execute("SELECT * FROM appointments WHERE created_by=? ORDER BY date DESC", (user_email,))
    return c.fetchall()

# ----------------- SESSION STATE -----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ----------------- STYLES -----------------
st.markdown("""
<style>
@keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
.hero { background-image: url('images/ai-generated-8722616_1280.jpg'); background-size: cover; background-position: center; height: 450px; display:flex; align-items:center; justify-content:center; }
.hero-text { animation: fadeIn 2s ease-in-out; color:white; font-size:3rem; font-weight:bold; text-shadow:2px 2px 4px #000; text-align:center; }
.cta-buttons button { background-color:#4f8ef7; color:white; padding:10px 25px; margin:10px; border-radius:5px; border:none; cursor:pointer; }
.cta-buttons button:hover { background-color:#3a6fcc; }
.section { padding:50px; }
.service-card, .staff-card, .clinic-card { background-color:#f5f5f5; padding:20px; border-radius:10px; text-align:center; margin:10px; transition: transform 0.2s; }
.service-card:hover, .staff-card:hover, .clinic-card:hover { transform:translateY(-5px); box-shadow:0px 4px 8px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

# ----------------- HERO -----------------
st.markdown("<div class='hero'><div class='hero-text'>Thrive Wellness Hospital</div></div>", unsafe_allow_html=True)
st.markdown("""
<div class='cta-buttons'>
<button onclick="window.scrollTo({top:document.getElementById('appointment').offsetTop, behavior:'smooth'})">Book Appointment</button>
<button onclick="window.scrollTo({top:document.getElementById('contact').offsetTop, behavior:'smooth'})">Contact Us</button>
</div>
""", unsafe_allow_html=True)

# ----------------- LOGIN / REGISTER -----------------
st.markdown("<div class='section'><h2>Login / Register</h2></div>", unsafe_allow_html=True)
login_col, reg_col = st.columns(2)

with login_col:
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

with reg_col:
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

# ----------------- SERVICES -----------------
st.markdown("<div class='section'><h2>Our Services</h2></div>", unsafe_allow_html=True)
services_cols = st.columns(3)
services = [
    {"name": "Medication Management", "desc": "Expert management of your medications."},
    {"name": "Psychotherapy", "desc": "Individual, group, and family therapy sessions."},
    {"name": "Telehealth", "desc": "Secure online therapy sessions."}
]
for col, s in zip(services_cols, services):
    with col:
        st.markdown(f"<div class='service-card'><h3>{s['name']}</h3><p>{s['desc']}</p></div>", unsafe_allow_html=True)

# ----------------- STAFF -----------------
st.markdown("<div class='section'><h2>Meet Our Staff</h2></div>", unsafe_allow_html=True)
staff_cols = st.columns(3)
staff = [
    {"role":"PMHNP-BC","img":"images/marek-studzinski-Q3J1wmn7_8w-unsplash.jpg"},
    {"role":"Therapist","img":"images/pexels-karolina-grabowska-4226769.jpg"},
    {"role":"Counselor","img":"images/pexels-shvetsa-3845129.jpg"}
]
for col, s in zip(staff_cols, staff):
    with col:
        st.markdown(f"<div class='staff-card'><img src='{s['img']}' width='200'><h4>{s['role']}</h4></div>", unsafe_allow_html=True)

# ----------------- CLINIC PLACEHOLDERS -----------------
st.markdown("<div class='section'><h2>About Our Clinic</h2></div>", unsafe_allow_html=True)
clinic_cols = st.columns(2)
for col in clinic_cols:
    with col:
        st.markdown("<div class='clinic-card'>Clinic Photo Placeholder</div>", unsafe_allow_html=True)

# ----------------- APPOINTMENT -----------------
st.markdown("<div class='section'><h2 id='appointment'>Book Appointment</h2></div>", unsafe_allow_html=True)
if st.session_state.logged_in:
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
            create_appointment(patient_name, service, date, time, provider, int(telehealth), user[2])
            st.success(f"Appointment booked for {patient_name} with {provider} on {date} at {time}.")
else:
    st.info("Please login to book an appointment.")

# ----------------- CONTACT -----------------
st.markdown("<div class='section'><h2 id='contact'>Contact Us</h2></div>", unsafe_allow_html=True)
st.markdown("**Address:** 123 Wellness Ave, Nairobi, Kenya")
st.markdown("**Phone:** +254 700 000 000")
st.markdown("**Email:** info@thrivewellness.com")

with st.form("contact_form"):
    name = st.text_input("Your Name", key="contact_name")
    email = st.text_input("Your Email", key="contact_email")
    message = st.text_area("Your Message", key="contact_message")
    send = st.form_submit_button("Send Message")
    if send:
        st.success("Your message has been sent! We will contact you shortly.")

# ----------------- SOCIAL MEDIA & NEWSLETTER -----------------
st.markdown("<div class='section'><h2>Follow Us & Newsletter</h2></div>", unsafe_allow_html=True)
social_cols = st.columns(4)
social_links = [
    {"name": "Facebook", "url": "https://facebook.com"},
    {"name": "Twitter", "url": "https://twitter.com"},
    {"name": "Instagram", "url": "https://instagram.com"},
    {"name": "Subscribe", "url": "#"}
]
for col, s in zip(social_cols, social_links):
    with col:
        if s['name']=="Subscribe":
            email_sub = st.text_input("Your Email for Newsletter", key="newsletter_email")
            if st.button("Subscribe", key="newsletter_btn"):
                st.success("Subscribed successfully! ✅")
        else:
            st.markdown(f"<a href='{s['url']}' target='_blank'>{s['name']}</a>", unsafe_allow_html=True)

# ----------------- SIDEBAR DASHBOARD -----------------
if st.session_state.logged_in:
    st.sidebar.subheader("Dashboard")
    user = st.session_state.user
    st.sidebar.text(f"Hello, {user[1]}")
    if user[5]:
        try:
            st.sidebar.image(user[5], width=100)
        except:
            st.sidebar.info("Avatar not available")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False, "user": None}))
    
    st.sidebar.subheader("Appointments")
    appointments = get_appointments(user[2], user[4])
    if appointments:
        for appt in appointments:
            st.sidebar.markdown(f"- {appt[1]} with {appt[5]} on {appt[3]} at {appt[4]} ({appt[7]})")
    else:
        st.sidebar.info("No appointments yet.")
