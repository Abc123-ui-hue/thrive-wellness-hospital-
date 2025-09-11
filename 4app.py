# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ---------------- Settings / Files ----------------
st.set_page_config(page_title="Thrive Mental Wellness Portal", layout="wide")
USERS_FILE = "users.csv"
APPTS_FILE = "appointments.csv"
PROFILES_FILE = "profiles.csv"
UPLOAD_DIR = "uploads"

# Ensure upload directory
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------------- Helpers: Init & CSV ----------------
def init_files():
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame([
            {"email":"admin@thrivewellness.com","password":"Admin123!","role":"Admin"},
            {"email":"staff1@thrivewellness.com","password":"Staff123!","role":"Staff"},
            {"email":"staff2@thrivewellness.com","password":"Staff123!","role":"Staff"},
        ])
        df.to_csv(USERS_FILE, index=False)
    if not os.path.exists(APPTS_FILE):
        df = pd.DataFrame(columns=["patient","doctor","date","time","reason","created_by"])
        df.to_csv(APPTS_FILE, index=False)
    if not os.path.exists(PROFILES_FILE):
        df = pd.DataFrame(columns=["email","name","specialty","bio","photopath"])
        df.to_csv(PROFILES_FILE, index=False)

def load_users_df():
    return pd.read_csv(USERS_FILE)

def save_user_to_csv(email, password, role):
    df = load_users_df()
    df = df.append({"email":email,"password":password,"role":role}, ignore_index=True)
    df.to_csv(USERS_FILE, index=False)

def load_appts_df():
    return pd.read_csv(APPTS_FILE)

def save_appts_df(df):
    df.to_csv(APPTS_FILE, index=False)

def load_profiles_df():
    return pd.read_csv(PROFILES_FILE)

def save_profiles_df(df):
    df.to_csv(PROFILES_FILE, index=False)

# ---------------- Authentication ----------------
def register_user(email, password, role):
    if not email.endswith("@thrivewellness.com"):
        st.error("❌ Please use your official hospital email: @thrivewellness.com")
        return False
    users = load_users_df()
    if email in users['email'].values:
        st.error("⚠️ Email already registered.")
        return False
    save_user_to_csv(email, password, role)
    st.success("✅ Registered. Please log in.")
    return True

def validate_user(email, password):
    users = load_users_df()
    row = users[(users['email']==email) & (users['password']==password)]
    if not row.empty:
        return row.iloc[0]['role']
    return None

# ---------------- Utility: save uploaded photo ----------------
def save_uploaded_photo(email, uploaded_file):
    if uploaded_file is None:
        return ""
    ext = os.path.splitext(uploaded_file.name)[1]
    safe = email.replace("@", "_at_")
    filename = f"{safe}{ext}"
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

# ---------------- Appointments CRUD ----------------
def add_appointment(patient, doctor, date, time, reason, created_by):
    df = load_appts_df()
    df = df.append({
        "patient": patient,
        "doctor": doctor,
        "date": str(date),
        "time": str(time),
        "reason": reason,
        "created_by": created_by
    }, ignore_index=True)
    save_appts_df(df)
    st.success("✅ Appointment saved.")

def rewrite_appointments(list_of_rows):
    cols = ["patient","doctor","date","time","reason","created_by"]
    df = pd.DataFrame(list_of_rows, columns=cols)
    save_appts_df(df)

# ---------------- Appointment Manager with Filters & Permissions ----------------
def manage_appointments_ui(user_role, user_email):
    st.subheader("🔍 Appointments — Search / Filter / Manage")
    df_all = load_appts_df()
    if df_all.empty:
        st.info("No appointments found.")
        return

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        search_patient = st.text_input("Patient name filter", key="filter_patient")
    with col2:
        search_doctor = st.text_input("Doctor name filter", key="filter_doctor")
    with col3:
        filter_date = st.date_input("Filter by date (optional)", key="filter_date")

    # Build filtered list of appointment dicts and track original indices
    filtered = []
    for idx, row in df_all.iterrows():
        # permission: staff sees only their created appts
        if user_role != "Admin" and row["created_by"] != user_email:
            continue
        if search_patient and search_patient.lower() not in str(row["patient"]).lower():
            continue
        if search_doctor and search_doctor.lower() not in str(row["doctor"]).lower():
            continue
        if filter_date:
            if str(filter_date) != str(row["date"]):
                continue
        filtered.append((idx, row.tolist()))  # (original_index, row_list)

    if not filtered:
        st.warning("No appointments match the filters.")
        return

    # Show and allow edit/delete per appointment (unique widget keys)
    for display_i, (orig_idx, row_list) in enumerate(filtered):
        patient, doctor, date, time, reason, created_by = row_list
        exp_label = f"{patient} — Dr. {doctor} on {date} at {time}"
        with st.expander(f"📌 {exp_label}"):
            st.write(f"**Reason:** {reason}")
            st.write(f"📧 Created by: {created_by}")
            # editable fields with unique keys
            new_patient = st.text_input(f"Patient name {display_i}", value=patient, key=f"np_{orig_idx}")
            new_doctor = st.text_input(f"Doctor {display_i}", value=doctor, key=f"nd_{orig_idx}")
            new_date = st.text_input(f"Date {display_i}", value=date, key=f"dt_{orig_idx}")
            new_time = st.text_input(f"Time {display_i}", value=time, key=f"tm_{orig_idx}")
            new_reason = st.text_area(f"Reason {display_i}", value=reason, key=f"nr_{orig_idx}")

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button(f"💾 Save {orig_idx}", key=f"save_{orig_idx}"):
                    df = load_appts_df()
                    df.at[orig_idx, "patient"] = new_patient
                    df.at[orig_idx, "doctor"] = new_doctor
                    df.at[orig_idx, "date"] = new_date
                    df.at[orig_idx, "time"] = new_time
                    df.at[orig_idx, "reason"] = new_reason
                    save_appts_df(df)
                    st.success("✅ Appointment updated.")
            with col_b:
                if st.button(f"🗑️ Delete {orig_idx}", key=f"del_{orig_idx}"):
                    df = load_appts_df()
                    df = df.drop(index=orig_idx).reset_index(drop=True)
                    save_appts_df(df)
                    st.warning("🗑️ Appointment deleted.")

    # Admin: export filtered results
    if user_role == "Admin":
        cols = ["patient","doctor","date","time","reason","created_by"]
        export_df = pd.DataFrame([r for _, r in filtered], columns=cols)
        csv = export_df.to_csv(index=False)
        st.download_button("⬇️ Download filtered results as CSV", csv, "appointments_filtered.csv", mime="text/csv")

# ---------------- Profile Management ----------------
def profile_display_and_edit_ui(user_email, is_admin=False):
    st.subheader("👤 My Profile")
    profiles = load_profiles_df()
    existing = profiles[profiles['email'] == user_email]
    if not existing.empty:
        row = existing.iloc[0]
        photopath = row.get("photopath", "")
        if isinstance(photopath, str) and photopath and os.path.exists(photopath):
            st.image(photopath, width=140)
        else:
            st.image("https://via.placeholder.com/140x140?text=No+Photo", width=140)
        name = st.text_input("Full name", value=row.get("name",""), key="p_name")
        specialty = st.text_input("Specialty", value=row.get("specialty",""), key="p_spec")
        bio = st.text_area("Short bio", value=row.get("bio",""), key="p_bio")
    else:
        name = st.text_input("Full name", key="p_name")
        specialty = st.text_input("Specialty", key="p_spec")
        bio = st.text_area("Short bio", key="p_bio")
        photopath = ""

    uploaded = st.file_uploader("Upload profile photo (png/jpg)", type=["png","jpg","jpeg"], key="p_upload")
    if st.button("Save Profile"):
        profiles = load_profiles_df()
        photo_path = photopath
        if uploaded is not None:
            photo_path = save_uploaded_photo(user_email, uploaded)
        if not existing.empty:
            idx = existing.index[0]
            profiles.loc[idx, "name"] = name
            profiles.loc[idx, "specialty"] = specialty
            profiles.loc[idx, "bio"] = bio
            profiles.loc[idx, "photopath"] = photo_path
        else:
            profiles = profiles.append({
                "email": user_email,
                "name": name,
                "specialty": specialty,
                "bio": bio,
                "photopath": photo_path
            }, ignore_index=True)
        save_profiles_df(profiles)
        st.success("✅ Profile saved.")

    # Admin: see all staff profiles
    if is_admin:
        st.markdown("---")
        st.subheader("All Staff Profiles (Admin View)")
        profiles = load_profiles_df()
        if profiles.empty:
            st.info("No profiles yet.")
        else:
            for _, r in profiles.iterrows():
                p_photo = r["photopath"] if isinstance(r["photopath"], str) and r["photopath"] and os.path.exists(r["photopath"]) else "https://via.placeholder.com/100?text=Photo"
                c1, c2 = st.columns([1,4])
                with c1:
                    st.image(p_photo, width=80)
                with c2:
                    st.markdown(f"**{r['name']}** — {r['specialty']}")
                    st.write(r['email'])
                    st.write(r['bio'])
                    st.markdown("---")

# ---------------- UI: Login / Register / Logout ----------------
def login_ui():
    st.title("🔐 Thrive Mental Wellness Portal — Login")
    email = st.text_input("Official email", placeholder="yourname@thrivewellness.com", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        role = validate_user(email, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.email = email
            st.session_state.role = role
            st.session_state.login_flag = True  # trigger a rerun in main
            st.success("✅ Login successful.")
        else:
            st.error("❌ Invalid credentials or not an official hospital email.")

def register_ui():
    st.title("📝 Register New Account")
    email = st.text_input("Official email", placeholder="yourname@thrivewellness.com", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_password")
    role = st.selectbox("Role", ["Staff","Admin"], key="reg_role")
    if st.button("Register"):
        register_user(email, password, role)

def logout_action():
    st.session_state.logged_in = False
    st.session_state.email = None
    st.session_state.role = None
    st.session_state.logout_flag = True

# ---------------- Dashboards ----------------
def admin_dashboard():
    st.title("🏥 Admin Dashboard — Thrive Mental Wellness")
    st.sidebar.markdown(f"**Logged in:** {st.session_state.email} (Admin)")
    if st.sidebar.button("Logout"):
        logout_action()
    # big admin area
    col1, col2 = st.columns([2,1])
    with col1:
        st.header("Hospital Overview")
        # simple stats
        appts = load_appts_df()
        profiles = load_profiles_df()
        st.metric("Total Appointments", len(appts))
        st.metric("Total Staff Profiles", len(profiles))
        # appointment manager
        manage_appointments_ui("Admin", st.session_state.email)
    with col2:
        st.header("Profile")
        profile_display_and_edit_ui(st.session_state.email, is_admin=True)

def staff_dashboard():
    st.title("👩‍⚕️ Staff Dashboard — Thrive Mental Wellness")
    st.sidebar.markdown(f"**Logged in:** {st.session_state.email} (Staff)")
    if st.sidebar.button("Logout"):
        logout_action()
    col1, col2 = st.columns([2,1])
    with col1:
        st.header("My Work")
        # appointment booking form
        st.subheader("➕ Book Appointment")
        patient = st.text_input("Patient full name", key="book_patient")
        doctor = st.text_input("Doctor name", key="book_doctor")
        date = st.date_input("Date", key="book_date")
        time = st.time_input("Time", key="book_time")
        reason = st.text_area("Reason", key="book_reason")
        if st.button("Save Appointment", key="book_save"):
            add_appointment(patient, doctor, date, time, reason, st.session_state.email)
        st.markdown("---")
        # manage only their appointments
        manage_appointments_ui("Staff", st.session_state.email)
    with col2:
        st.header("Profile")
        profile_display_and_edit_ui(st.session_state.email, is_admin=False)

# ---------------- Main ----------------
def main():
    init_files()

    # session flags default
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "login_flag" not in st.session_state:
        st.session_state.login_flag = False
    if "logout_flag" not in st.session_state:
        st.session_state.logout_flag = False

    # If login_flag or logout_flag then rerun once to refresh the UI (avoids calling rerun inside callbacks)
    if st.session_state.login_flag:
        st.session_state.login_flag = False
        st.experimental_rerun()  # safe here at top-level to force refresh after login
    if st.session_state.logout_flag:
        st.session_state.logout_flag = False
        st.experimental_rerun()

    # Styling header / hero
    st.markdown("""
        <div style='padding:18px;border-radius:8px;margin-bottom:18px; background: linear-gradient(90deg,#0072E3,#00BFFF); color:white'>
            <h1 style='margin:0'>Thrive Mental Wellness LLC</h1>
            <p style='margin:0'>Professional psychiatric health & treatment portal</p>
        </div>
    """, unsafe_allow_html=True)

    # Not logged in: show tabs for Login / Register
    if not st.session_state.logged_in:
        tab = st.tabs(["🔐 Login","📝 Register"])
        with tab[0]:
            login_ui()
        with tab[1]:
            register_ui()
        st.stop()

    # Logged in: route to dashboard based on role
    role = st.session_state.role
    if role == "Admin":
        admin_dashboard()
    else:
        staff_dashboard()

if __name__ == "__main__":
    main()
