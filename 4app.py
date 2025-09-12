import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("hospital.db", check_same_thread=False)
c = conn.cursor()

def reset_database():
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )""")

    c.execute("DROP TABLE IF EXISTS reports")
    c.execute("""CREATE TABLE reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        treatment TEXT,
        solution TEXT,
        created_by TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    c.execute("DROP TABLE IF EXISTS appointments")
    c.execute("""CREATE TABLE appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        service TEXT,
        date TEXT,
        time TEXT,
        provider TEXT,
        telehealth TEXT,
        status TEXT,
        created_by TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    conn.commit()

# Reset DB on first run
if "db_initialized" not in st.session_state:
    reset_database()
    st.session_state.db_initialized = True

# ---------------- AUTH FUNCTIONS ----------------
def register_user(fullname, email, password, role):
    try:
        c.execute("INSERT INTO users (fullname, email, password, role) VALUES (?, ?, ?, ?)",
                  (fullname.strip(), email.strip(), password.strip(), role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email.strip(), password.strip()))
    return c.fetchone()

# ---------------- DASHBOARDS ----------------
def admin_dashboard():
    st.subheader("👨‍💼 Admin Dashboard")
    st.write("Welcome Admin, manage everything here.")

    st.write("### Registered Users")
    users = c.execute("SELECT fullname, email, role FROM users").fetchall()
    for u in users:
        st.write(f"- {u[0]} | {u[1]} | {u[2]}")

    st.write("### All Appointments")
    appts = c.execute("SELECT * FROM appointments").fetchall()
    for a in appts:
        st.write(f"- {a[1]} | {a[2]} on {a[3]} {a[4]} | {a[6]} | {a[7]}")

def staff_dashboard():
    st.subheader("🧑‍⚕️ Staff Dashboard")
    st.write("Welcome Staff, manage reports and patients.")

    patient_name = st.text_input("Patient Name")
    treatment = st.text_area("Treatment")
    solution = st.text_area("Solution")

    if st.button("Save Report"):
        if patient_name and treatment and solution:
            c.execute("INSERT INTO reports (patient_name, treatment, solution, created_by) VALUES (?,?,?,?)",
                      (patient_name, treatment, solution, st.session_state.get("user", "Unknown")))
            conn.commit()
            st.success("✅ Report saved successfully!")
        else:
            st.warning("⚠️ Please fill all fields")

    st.write("### Reports")
    reports = c.execute("SELECT * FROM reports ORDER BY created_at DESC").fetchall()
    for r in reports:
        st.write(f"**{r[1]}** | {r[2]} → {r[3]} | By {r[4]} at {r[5]}")

def patient_dashboard():
    st.subheader("🧑 Patient Dashboard")
    st.write("Welcome Patient, manage your appointments.")

    patient_name = st.session_state.get("user", "Anonymous")
    service = st.selectbox("Select Service", ["Medication Management", "Psychotherapy", "Telehealth"])
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    provider = st.text_input("Provider")
    telehealth = st.selectbox("Telehealth Option", ["Yes", "No"])

    if st.button("Book Appointment"):
        c.execute("""INSERT INTO appointments 
                     (patient_name, service, date, time, provider, telehealth, status, created_by)
                     VALUES (?,?,?,?,?,?,?,?)""",
                  (patient_name, service, str(date), str(time), provider, telehealth, "Pending", patient_name))
        conn.commit()
        st.success("✅ Appointment booked successfully!")

    st.write("### Your Appointments")
    appts = c.execute("SELECT * FROM appointments WHERE patient_name=?", (patient_name,)).fetchall()
    for a in appts:
        st.write(f"- {a[2]} on {a[3]} {a[4]} | Status: {a[6]}")

# ---------------- PUBLIC PAGES ----------------
def home_page():
    st.title("🏥 Thrive Wellness Hospital")
    st.subheader("Your Partner in Mental Health & Wellness")
    st.write("We provide **Medication Management**, **Psychotherapy**, and **Telehealth Services**.")

def about_page():
    st.title("ℹ️ About Us")
    st.write("Compassionate, patient-centered mental healthcare.")

def services_page():
    st.title("🛠 Services")
    st.write("- Medication Management\n- Psychotherapy\n- Telehealth")

def contact_page():
    st.title("📞 Contact Us")
    st.write("🏠 Address: 123 Wellness Ave, Nairobi, Kenya")
    st.write("📧 Email: info@thrivewellness.com")
    st.write("📱 Phone: +254 700 000 000")

def login_register_page():
    st.title("🔑 Login / Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email (Login)")
        password = st.text_input("Password (Login)", type="password")
        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state.user = user[1]
                st.session_state.role = user[4]
                st.session_state.logged_in = True
                st.success(f"✅ Logged in as {user[1]} ({user[4]})")
            else:
                st.error("❌ Invalid email or password")

    with tab2:
        fullname = st.text_input("Full Name (Register)")
        email = st.text_input("Email (Register)")
        password = st.text_input("Password (Register)", type="password")
        role = st.selectbox("Role", ["patient", "staff", "admin"])

        if st.button("Register"):
            if register_user(fullname, email, password, role):
                st.success("✅ Registration successful! Please login.")
            else:
                st.error("❌ Email already exists!")

# ---------------- MAIN APP ----------------
st.sidebar.title("🌐 Navigation")

# Show logout if logged in
if st.session_state.get("logged_in"):
    st.sidebar.write(f"👋 Hello, {st.session_state.get('user')}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.success("✅ Logged out successfully!")

page = st.sidebar.radio("Go to", ["Home", "About", "Services", "Contact", "Login/Register", "Dashboard"])

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
elif page == "Dashboard":
    if not st.session_state.get("logged_in"):
        st.warning("⚠️ Please login first.")
    else:
        if st.session_state.role == "admin":
            admin_dashboard()
        elif st.session_state.role == "staff":
            staff_dashboard()
        elif st.session_state.role == "patient":
            patient_dashboard()
