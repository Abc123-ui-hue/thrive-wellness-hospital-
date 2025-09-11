import streamlit as st
import sqlite3
from datetime import datetime
import os

# ---------------- Database Setup ----------------
DB_FILE = "hospital.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

# ---------------- Helper function to add missing columns ----------------
def ensure_column(table, column, col_type="TEXT"):
    try:
        c.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # column already exists

# ---------------- Users Table ----------------
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    bio TEXT,
    phone TEXT
)""")
conn.commit()
ensure_column("users", "avatar_url")

# ---------------- Reports Table ----------------
c.execute("""CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT
)""")
conn.commit()
for col, typ in [
    ("patient_name", "TEXT"),
    ("treatment", "TEXT"),
    ("solution", "TEXT"),
    ("created_by", "TEXT"),
    ("created_by_avatar", "TEXT"),
    ("created_at", "TEXT")
]:
    ensure_column("reports", col, typ)

# ---------------- Appointments Table ----------------
c.execute("""CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT
)""")
conn.commit()
for col, typ in [
    ("patient_name", "TEXT"),
    ("service", "TEXT"),
    ("date", "TEXT"),
    ("time", "TEXT"),
    ("provider", "TEXT"),
    ("telehealth", "BOOLEAN"),
    ("status", "TEXT"),
    ("created_by", "TEXT")
]:
    ensure_column("appointments", col, typ)

# ---------------- Helper Functions ----------------
def hash_password(password):
    return password[::-1]  # simple hash for demo

def check_password(password, hashed):
    return hash_password(password) == hashed

def get_avatar_url():
    return "https://thispersondoesnotexist.com/image"

def get_user(email):
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    return c.fetchone()

def register_user(name, email, password, role):
    if not name or not email or not password or not role:
        st.error("All fields are required!")
        return False
    avatar_url = get_avatar_url()
    try:
        c.execute(
            "INSERT INTO users (name,email,password,role,avatar_url) VALUES (?,?,?,?,?)",
            (name, email, hash_password(password), role, avatar_url)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        st.error("Email already exists!")
        return False
    except sqlite3.OperationalError as e:
        st.error(f"Database error: {e}")
        return False

def update_profile(user_id, name, bio, phone, avatar_url):
    c.execute("UPDATE users SET name=?, bio=?, phone=?, avatar_url=? WHERE id=?",
              (name, bio, phone, avatar_url, user_id))
    conn.commit()

def create_report(patient_name, treatment, solution, created_by, avatar_url):
    c.execute("""INSERT INTO reports (patient_name,treatment,solution,created_by,created_by_avatar,created_at) 
                 VALUES (?,?,?,?,?,?)""",
              (patient_name, treatment, solution, created_by, avatar_url, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_reports():
    c.execute("SELECT * FROM reports ORDER BY created_at DESC")
    return c.fetchall()

def create_appointment(patient_name, service, date, time, provider, telehealth, created_by):
    c.execute("""INSERT INTO appointments (patient_name,service,date,time,provider,telehealth,status,created_by) 
                 VALUES (?,?,?,?,?,?,?,?)""",
              (patient_name, service, str(date), str(time), provider, telehealth, "Pending", created_by))
    conn.commit()

def get_appointments():
    c.execute("SELECT * FROM appointments ORDER BY date DESC, time DESC")
    return c.fetchall()

def safe_display_image(img_path, width=100):
    """Safely display avatar: URL, local path, or fallback."""
    if img_path:
        if img_path.startswith("http"):
            st.image(img_path, width=width)
        elif os.path.exists(img_path):
            st.image(open(img_path, "rb"), width=width)
        else:
            st.image(get_avatar_url(), width=width)
    else:
        st.image(get_avatar_url(), width=width)

# ---------------- Streamlit Config ----------------
st.set_page_config(page_title="Thrive Wellness Hospital Portal", layout="wide")
st.markdown("""
<style>
.stApp {background: linear-gradient(to right, #a1c4fd, #c2e9fb); min-height:100vh;}
.stButton>button {background-color: #4CAF50; color: white;}
.stMetric-value {font-size:2rem !important; color:#1a1a1a;}
</style>
""", unsafe_allow_html=True)

# ---------------- Session State ----------------
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user" not in st.session_state: st.session_state.user = None

# ---------------- Public Pages ----------------
def home_page():
    st.header("Welcome to Thrive Wellness Hospital")
    st.subheader("Your mental health matters")
    st.image(get_avatar_url(), width=150)
    st.write("Services: Medication Management, Psychotherapy (Individual, Group, Family)")
    st.button("Book Appointment")
    st.button("Contact Us")
    st.markdown("**Featured Staff:** Cecilia Wamburu PMHNP-BC")
    st.markdown("**Testimonials / Success Stories**: Patient A, Patient B")
    st.markdown("Follow us on [Facebook](#) | [Twitter](#) | [Instagram](#)")

# ---------------- Login/Register Functions ----------------
def login_tab():
    st.subheader("Login")
    email = st.text_input("Login Email", key="login_email")
    password = st.text_input("Login Password", type="password", key="login_password")
    if st.button("Login", key="login_btn"):
        user = get_user(email)
        if user and check_password(password, user[3]):
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success(f"Welcome, {user[1]}!")
        else:
            st.error("Invalid email or password.")

def register_tab():
    st.subheader("Register")
    name = st.text_input("Full Name", key="register_name")
    email = st.text_input("Email", key="register_email")
    password = st.text_input("Password", type="password", key="register_password")
    role = st.selectbox("Role", ["Patient","Staff","Admin"], key="register_role")
    if st.button("Register", key="register_btn"):
        if register_user(name, email, password, role):
            st.success("Registration successful! You can login now.")

# ---------------- Main App -----------------
if not st.session_state.logged_in:
    tabs = st.tabs(["Home", "Login", "Register"])
    with tabs[0]:
        home_page()
    with tabs[1]:
        login_tab()
    with tabs[2]:
        register_tab()
else:
    user = st.session_state.user
    safe_display_image(user[7], width=100)  # <- Safe avatar display
    st.sidebar.write(f"**{user[1]}**")
    st.sidebar.write(f"Role: {user[4]}")
    st.sidebar.write(f"Bio: {user[5]}")
    st.sidebar.write(f"Phone: {user[6]}")

    menu_items = ["Dashboard","Profile","Patient Reports","Appointments","Book Appointment","Logout"]
    page = st.sidebar.selectbox("Menu", menu_items)

    if page == "Logout":
        st.session_state.logged_in = False
        st.session_state.user = None
        st.experimental_rerun()

    elif page == "Profile":
        st.header("Edit Profile")
        name = st.text_input("Name", value=user[1], key="profile_name")
        bio = st.text_area("Bio", value=user[5] if user[5] else "", key="profile_bio")
        phone = st.text_input("Phone", value=user[6] if user[6] else "", key="profile_phone")
        avatar_file = st.file_uploader("Upload Avatar", type=["png","jpg","jpeg"], key="profile_avatar")
        avatar_url = user[7]
        if avatar_file:
            avatar_path = f"avatars/{user[1].replace(' ','_')}.png"
            os.makedirs("avatars", exist_ok=True)
            with open(avatar_path, "wb") as f:
                f.write(avatar_file.getbuffer())
            avatar_url = avatar_path
        if st.button("Update Profile", key="profile_update_btn"):
            update_profile(user[0], name, bio, phone, avatar_url)
            st.success("Profile updated! Reload page.")
            st.session_state.user = get_user(user[2])

    elif page == "Dashboard":
        st.header("Dashboard")
        total_users = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        total_reports = c.execute("SELECT COUNT(*) FROM reports").fetchone()[0]
        total_appointments = c.execute("SELECT COUNT(*) FROM appointments").fetchone()[0]
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Users", total_users)
        col2.metric("Total Reports", total_reports)
        col3.metric("Total Appointments", total_appointments)

    elif page == "Patient Reports":
        st.header("Patient Reports")
        if user[4] in ["Admin","Staff"]:
            st.subheader("Add Report")
            patient_name = st.text_input("Patient Name", key="report_patient_name")
            treatment = st.text_input("Treatment", key="report_treatment")
            solution = st.text_input("Solution", key="report_solution")
            if st.button("Create Report", key="create_report_btn"):
                create_report(patient_name, treatment, solution, user[1], user[7])
                st.success("Report added successfully!")
        st.subheader("All Reports")
        reports = get_reports()
        for r in reports:
            col1, col2 = st.columns([1,5])
            with col1:
                safe_display_image(r[5], width=50)
            with col2:
                st.markdown(f"**Patient:** {r[1]}  \n**Treatment:** {r[2]}  \n**Solution:** {r[3]}  \n**By:** {r[4]}  \n**At:** {r[6]}")
            st.markdown("---")

    elif page == "Appointments":
        st.header("Appointments")
        appointments = get_appointments()
        for a in appointments:
            st.markdown(f"**Patient:** {a[1]} | **Service:** {a[2]} | **Date:** {a[3]} | **Time:** {a[4]} | **Provider:** {a[5]} | **Telehealth:** {a[6]} | **Status:** {a[7]}")

    elif page == "Book Appointment":
        st.header("Book Appointment")
        patient_name = st.text_input("Your Name", key="book_name")
        service = st.selectbox("Service", ["Medication Management","Psychotherapy"], key="book_service")
        date = st.date_input("Select Date", key="book_date")
        time = st.time_input("Select Time", key="book_time")
        provider = st.selectbox("Provider", ["Cecilia Wamburu PMHNP-BC","John Doe Therapist"], key="book_provider")
        telehealth = st.checkbox("Telehealth / Online", key="book_telehealth")
        if st.button("Book", key="book_btn"):
            create_appointment(patient_name, service, date, time, provider, telehealth, user[1])
            st.success("Appointment booked successfully! Confirmation sent (simulated)")
