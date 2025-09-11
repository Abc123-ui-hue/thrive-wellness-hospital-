import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime

# --------------------------
# Page Config & Styling
# --------------------------
st.set_page_config(page_title="Thrive Wellness Hospital Portal", layout="centered")

# ✅ Embedded Base64 Logo (replace with your own if needed)
LOGO_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAYAAAA+7c6nAAAABHNCSVQICAgIfAhkiAAAIABJREFU"
    "eJzt3X9sXNd93/H3O2zjDIqErJ0QAkixJQFSSgvhCltZUBYkQmCNC1glIkRxtT5vAk2Wi8TstLaD"
    "FNUiZsAJpkbUgx9mAIQCYgSMLVhbAqtqimDQoxAyFhAwLhrGBY1iyTAoRzNn8uTsOfdHZvucO/fO"
    "mc8Z3b2zszM/9/5+3n3O3bt3772f53e9/3cf5/ua3AIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    "AAAAAAAAAADwXzWNPQnWfFfOKwAAAABJRU5ErkJggg=="
)

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f0ff 100%) !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .main {
            background: white;
            border-radius: 18px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        .stButton>button {
            background-color: #1E90FF;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #4682B4;
            color: #fff;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------
# Logo & Title
# --------------------------
st.markdown(
    f"""
    <div style="text-align:center; margin-bottom:20px;">
        <img src="data:image/png;base64,{LOGO_BASE64}" alt="Hospital Logo" width="120"/>
        <h2 style="color:#1E90FF;">🏥 Thrive Wellness Hospital Portal</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------
# CSV Files for Persistence
# --------------------------
USERS_FILE = "users.csv"
PATIENTS_FILE = "patients.csv"
STAFF_FILE = "staff.csv"
APPOINTMENTS_FILE = "appointments.csv"

def init_csv(file, columns):
    if not os.path.exists(file):
        pd.DataFrame(columns=columns).to_csv(file, index=False)

init_csv(USERS_FILE, ["email", "password", "role"])
init_csv(PATIENTS_FILE, ["name", "condition", "date", "plan", "recorded_by"])
init_csv(STAFF_FILE, ["name", "specialization", "email", "photo"])
init_csv(APPOINTMENTS_FILE, ["patient", "service", "date", "staff_email"])

# --------------------------
# Session States
# --------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "email" not in st.session_state:
    st.session_state["email"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# --------------------------
# Auth Functions
# --------------------------
def register_user(email, password, role):
    users = pd.read_csv(USERS_FILE)
    if email in users["email"].values:
        return False, "⚠️ User already exists!"
    users.loc[len(users)] = [email, password, role]
    users.to_csv(USERS_FILE, index=False)
    return True, "✅ Registration successful! You can now log in."

def login_user(email, password):
    users = pd.read_csv(USERS_FILE)
    match = users[(users["email"] == email) & (users["password"] == password)]
    if not match.empty:
        st.session_state["logged_in"] = True
        st.session_state["email"] = email
        st.session_state["role"] = match.iloc[0]["role"]
        return True
    return False

def logout_user():
    st.session_state["logged_in"] = False
    st.session_state["email"] = None
    st.session_state["role"] = None
    st.session_state["page"] = "login"

# --------------------------
# Pages
# --------------------------
def show_login():
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(email, password):
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials.")

    st.info("Don't have an account? Register below 👇")
    if st.button("Go to Register"):
        st.session_state["page"] = "register"

def show_register():
    st.title("📝 Register")
    email = st.text_input("Email (e.g., meshmuth18@gmail.com)")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["staff", "admin"])

    if st.button("Register"):
        success, msg = register_user(email, password, role)
        if success:
            st.success(msg)
        else:
            st.error(msg)

    if st.button("Back to Login"):
        st.session_state["page"] = "login"

def show_admin_dashboard():
    st.title("🏥 Admin Dashboard")
    st.write(f"Welcome **{st.session_state['email']}** (Admin)")

    st.subheader("📊 Manage Patients")
    pname = st.text_input("Patient Name")
    condition = st.text_input("Illness / Condition")
    pdate = st.date_input("Admission Date")
    plan = st.text_area("Treatment Plan")
    if st.button("Save Patient Record"):
        patients = pd.read_csv(PATIENTS_FILE)
        patients.loc[len(patients)] = [pname, condition, str(pdate), plan, st.session_state["email"]]
        patients.to_csv(PATIENTS_FILE, index=False)
        st.success("✅ Patient record saved!")

    st.dataframe(pd.read_csv(PATIENTS_FILE))

    st.subheader("👨‍⚕️ Manage Staff Profiles")
    sname = st.text_input("Staff Full Name")
    spec = st.text_input("Specialization")
    semail = st.text_input("Staff Email")
    if st.button("Save Staff Profile"):
        staff = pd.read_csv(STAFF_FILE)
        staff.loc[len(staff)] = [sname, spec, semail, "uploaded_later"]
        staff.to_csv(STAFF_FILE, index=False)
        st.success("✅ Staff profile saved!")

    st.dataframe(pd.read_csv(STAFF_FILE))

    st.subheader("📅 Appointments")
    st.dataframe(pd.read_csv(APPOINTMENTS_FILE))

    if st.button("Logout"):
        logout_user()

def show_staff_dashboard():
    st.title("👩‍⚕️ Staff Dashboard")
    st.write(f"Welcome **{st.session_state['email']}** (Staff)")

    st.subheader("📋 My Profile")
    name = st.text_input("Full Name")
    spec = st.text_input("Specialization")
    if st.button("Save My Profile"):
        staff = pd.read_csv(STAFF_FILE)
        staff.loc[len(staff)] = [name, spec, st.session_state["email"], "uploaded_later"]
        staff.to_csv(STAFF_FILE, index=False)
        st.success("✅ Profile saved!")

    st.subheader("🧑‍🤝‍🧑 Record Patient Info")
    pname = st.text_input("Patient Name")
    condition = st.text_input("Illness / Condition")
    pdate = st.date_input("Visit Date")
    notes = st.text_area("Notes / Observations")
    if st.button("Save Patient Record"):
        patients = pd.read_csv(PATIENTS_FILE)
        patients.loc[len(patients)] = [pname, condition, str(pdate), notes, st.session_state["email"]]
        patients.to_csv(PATIENTS_FILE, index=False)
        st.success("✅ Patient record saved!")

    st.subheader("📅 My Appointments")
    patient = st.text_input("Patient for Appointment")
    service = st.text_input("Service")
    adate = st.date_input("Appointment Date")
    if st.button("Save Appointment"):
        apps = pd.read_csv(APPOINTMENTS_FILE)
        apps.loc[len(apps)] = [patient, service, str(adate), st.session_state["email"]]
        apps.to_csv(APPOINTMENTS_FILE, index=False)
        st.success("✅ Appointment saved!")

    st.dataframe(pd.read_csv(APPOINTMENTS_FILE))

    if st.button("Logout"):
        logout_user()

# --------------------------
# Router
# --------------------------
if not st.session_state["logged_in"]:
    if st.session_state["page"] == "login":
        show_login()
    elif st.session_state["page"] == "register":
        show_register()
else:
    if st.session_state["role"] == "admin":
        show_admin_dashboard()
    elif st.session_state["role"] == "staff":
        show_staff_dashboard()
