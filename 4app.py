# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime
from io import BytesIO

# -----------------------
# Basic setup & styling
# -----------------------
st.set_page_config(page_title="Thrive Mental Wellness Portal", layout="wide")

st.markdown("""
<style>
/* Full-page background */
[data-testid="stAppViewContainer"] { 
    background: linear-gradient(135deg, #e8f6ff 0%, #c6f0ee 100%);
    color: #003366;
    font-family: 'Lato', sans-serif;
}

/* Hero section */
.hero {
    background-image: url('https://via.placeholder.com/1400x420?text=Thrive+Mental+Wellness');
    background-size: cover;
    background-position: center;
    padding: 64px 24px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

/* Cards for sections */
.card { 
    background-color: white; 
    padding:18px; 
    border-radius:12px; 
    box-shadow:2px 2px 12px rgba(0,0,0,0.12); 
    margin-bottom:18px; 
    transition: transform 0.18s; 
}
.card:hover { transform: scale(1.02); }

/* Buttons */
button, .stButton>button { 
    background: linear-gradient(90deg,#0072E3,#00BFFF); 
    color:white; padding:8px 18px; border-radius:10px; border:none; font-weight:600; 
}
button:hover, .stButton>button:hover { opacity:0.95; transform: translateY(-1px); }

/* Inputs */
.stTextInput>div>div>input, 
.stTextArea>div>div>textarea, 
.stSelectbox>div>div>div>select {
    border-radius:10px; border:1px solid #0072E3; padding:6px;
}

/* Sidebar */
[data-testid="stSidebar"] { background: #bfeff2; }

/* Footer */
.footer { text-align:center; padding:14px; font-size:13px; color:#003366; margin-top:18px; }
</style>
""", unsafe_allow_html=True)

# -----------------------
# Ensure uploads folder exists
# -----------------------
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

# -----------------------
# Session state defaults
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.session_state.staff_index = 0
    st.session_state.logout_trigger = False

# -----------------------
# Users persistence (users.csv)
# -----------------------
USERS_CSV = "users.csv"

def load_users():
    pre_populated = [
        {"Email":"admin@thrivewellness.com","Password":"Admin123!","Role":"Admin"},
        {"Email":"staff1@thrivewellness.com","Password":"Staff123!","Role":"Staff"},
        {"Email":"staff2@thrivewellness.com","Password":"Staff123!","Role":"Staff"}
    ]
    if os.path.exists(USERS_CSV):
        df = pd.read_csv(USERS_CSV)
    else:
        df = pd.DataFrame(pre_populated)
        df.to_csv(USERS_CSV, index=False)
    return {row["Email"]: {"password": row["Password"], "role": row["Role"]} for _, row in df.iterrows()}

def save_user(email, password, role):
    new_df = pd.DataFrame([{"Email": email, "Password": password, "Role": role}])
    if os.path.exists(USERS_CSV):
        new_df.to_csv(USERS_CSV, mode='a', header=False, index=False)
    else:
        new_df.to_csv(USERS_CSV, index=False)

users_db = load_users()

# -----------------------
# Staff Profiles persistence (staff_profiles.csv)
# -----------------------
PROFILES_CSV = "staff_profiles.csv"

def load_profiles():
    if os.path.exists(PROFILES_CSV):
        return pd.read_csv(PROFILES_CSV)
    else:
        df = pd.DataFrame(columns=["Email","Name","Role","Bio","PhotoPath"])
        df.to_csv(PROFILES_CSV, index=False)
        return df

def save_profiles(df):
    df.to_csv(PROFILES_CSV, index=False)

# -----------------------
# Appointments persistence
# -----------------------
APPTS_CSV = "appointments.csv"

def load_appointments():
    if os.path.exists(APPTS_CSV):
        df = pd.read_csv(APPTS_CSV)
        # ensure Date column is consistent
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"]).dt.date
        return df
    else:
        cols = ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"]
        df = pd.DataFrame(columns=cols)
        df.to_csv(APPTS_CSV, index=False)
        return df

def save_appointments(df):
    df.to_csv(APPTS_CSV, index=False)

# -----------------------
# Authentication
# -----------------------
def authenticate_user(email, password):
    if not email.endswith("@thrivewellness.com"):
        return None
    if email in users_db and users_db[email]["password"] == password:
        return users_db[email]["role"]
    return None

def logout_user():
    # reset session and trigger rerun outside callback
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.session_state.logout_trigger = True

# -----------------------
# Register
# -----------------------
def register_user_ui():
    st.subheader("Register New User (Official Email Only)")
    new_email = st.text_input("Email", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_password")
    role = st.selectbox("Role", ["Admin", "Staff"], key="reg_role")
    if st.button("Register", key="reg_btn"):
        if not new_email.endswith("@thrivewellness.com"):
            st.error("Please use your official hospital email: @thrivewellness.com")
            return
        if new_email.strip() == "" or new_password.strip() == "":
            st.error("Please provide both email and password")
            return
        if new_email in users_db:
            st.error("User already exists")
            return
        users_db[new_email] = {"password": new_password, "role": role}
        save_user(new_email, new_password, role)
        st.success(f"{role} registered successfully. Now login from the Login tab.")

# -----------------------
# Helper: save profile image bytes to a file and return path
# -----------------------
def save_profile_image(email, uploaded_file):
    if uploaded_file is None:
        return ""
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    safe_name = email.replace("@", "_at_")
    filename = f"{safe_name}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    # write bytes
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())
    return filepath

# -----------------------
# Admin: create/update profile UI (admin-only)
# -----------------------
def admin_profile_management():
    st.markdown("<h2>Manage Staff & Admin Profiles</h2>", unsafe_allow_html=True)
    profiles_df = load_profiles()

    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("#### Create / Update Profile")
        email = st.text_input("Official Email (must end with @thrivewellness.com)", key="profile_email")
        name = st.text_input("Full Name", key="profile_name")
        role = st.selectbox("Role", ["Admin", "Staff"], key="profile_role")
        bio = st.text_area("Short Bio", key="profile_bio")
        uploaded_file = st.file_uploader("Upload Profile Photo (png/jpg)", type=["png","jpg","jpeg"], key="profile_photo_uploader")
        if st.button("Save Profile"):
            if not email.endswith("@thrivewellness.com"):
                st.error("Profile email must be an official hospital email.")
            elif email.strip() == "" or name.strip() == "":
                st.error("Please provide email and name.")
            else:
                photo_path = ""
                if uploaded_file is not None:
                    photo_path = save_profile_image(email, uploaded_file)
                # if profile exists, update it
                if email in list(profiles_df["Email"].astype(str)):
                    idx = profiles_df.index[profiles_df["Email"]==email][0]
                    profiles_df.at[idx, "Name"] = name
                    profiles_df.at[idx, "Role"] = role
                    profiles_df.at[idx, "Bio"] = bio
                    if photo_path:
                        profiles_df.at[idx, "PhotoPath"] = photo_path
                else:
                    new_row = {"Email":email, "Name":name, "Role":role, "Bio":bio, "PhotoPath":photo_path}
                    profiles_df = profiles_df.append(new_row, ignore_index=True)
                save_profiles(profiles_df)
                st.success("Profile saved/updated.")
    with col2:
        st.markdown("#### Existing Profiles")
        if profiles_df.empty:
            st.info("No profiles yet.")
        else:
            for _, row in profiles_df.iterrows():
                ph = row["PhotoPath"] if pd.notna(row["PhotoPath"]) and row["PhotoPath"]!="" else "https://via.placeholder.com/120x120?text=Photo"
                st.image(ph, width=80)
                st.write(f"**{row['Name']}** — {row['Role']}")
                st.write(row["Email"])
                st.write(row["Bio"])
                st.write("---")

# -----------------------
# Staff: edit own profile UI
# -----------------------
def staff_profile_editor():
    profiles_df = load_profiles()
    email = st.session_state.user_email
    st.markdown("### Your Profile")
    existing = profiles_df[profiles_df["Email"]==email]
    if not existing.empty:
        row = existing.iloc[0]
        st.image(row["PhotoPath"] if pd.notna(row["PhotoPath"]) and row["PhotoPath"]!="" else "https://via.placeholder.com/150?text=Photo", width=140)
        name = st.text_input("Full name", value=row["Name"], key="self_name")
        bio = st.text_area("Bio", value=row["Bio"], key="self_bio")
    else:
        name = st.text_input("Full name", key="self_name")
        bio = st.text_area("Bio", key="self_bio")
    uploaded_file = st.file_uploader("Upload profile photo", type=["png","jpg","jpeg"], key="self_photo")
    if st.button("Save My Profile"):
        profiles_df = load_profiles()
        photo_path = ""
        if uploaded_file is not None:
            photo_path = save_profile_image(email, uploaded_file)
        if email in list(profiles_df["Email"].astype(str)):
            idx = profiles_df.index[profiles_df["Email"]==email][0]
            profiles_df.at[idx, "Name"] = name
            profiles_df.at[idx, "Bio"] = bio
            if photo_path:
                profiles_df.at[idx, "PhotoPath"] = photo_path
        else:
            new_row = {"Email":email, "Name":name, "Role":st.session_state.role, "Bio":bio, "PhotoPath":photo_path}
            profiles_df = profiles_df.append(new_row, ignore_index=True)
        save_profiles(profiles_df)
        st.success("Profile updated.")

# -----------------------
# Booking UI
# -----------------------
def book_appointment_ui():
    st.header("Book Appointment")
    with st.form("book_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        service = st.selectbox("Service", ["Medication Management", "Psychotherapy"])
        date_time = st.date_input("Preferred Date")
        notes = st.text_area("Additional Notes")
        submitted = st.form_submit_button("Submit Appointment")
        if submitted:
            assigned_staff = assign_staff()
            submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = load_appointments()
            new_row = {"Name":name,"Email":email,"Phone":phone,"Service":service,"Date":str(date_time),
                       "Notes":notes,"SubmittedAt":submitted_at,"Status":"Pending","AssignedTo":assigned_staff}
            df = df.append(new_row, ignore_index=True)
            save_appointments(df)
            st.success(f"Appointment submitted! Assigned to: {assigned_staff}")
            st.info("Telehealth link placeholder: https://example.com/telehealth")

# -----------------------
# Dashboard (Admin & Staff)
# -----------------------
def dashboard_ui():
    st.header(f"{'Admin' if st.session_state.role=='Admin' else 'Staff'} Dashboard")
    appts = load_appointments()
    # Admin sees all, staff sees their assigned
    if st.session_state.role == "Staff":
        appts = appts[appts["AssignedTo"]==st.session_state.user_email]

    # Top stats (bigger for Admin)
    col1, col2, col3, col4 = st.columns([2,1,1,1])
    total_appts = len(load_appointments())
    total_staff = sum(1 for v in users_db.values() if v["role"]=="Staff")
    recorded_notes = sum(load_appointments()["Status"]=="Recorded") if not load_appointments().empty else 0

    col1.metric("Total Appointments", total_appts)
    col2.metric("Total Staff", total_staff)
    col3.metric("Recorded Notes", recorded_notes)
    col4.metric("Your Role", st.session_state.role)

    # Appointments table and management
    st.subheader("Appointments")
    if appts.empty:
        st.info("No appointments found.")
    else:
        # show table
        st.dataframe(appts.sort_values(by="Date", ascending=True).reset_index(drop=True))
        if st.session_state.role == "Admin":
            st.markdown("**Admin Tools**")
            # simple controls to update status or reassign
            with st.form("admin_update_form"):
                sel_email = st.text_input("Select patient name to update (exact match)", key="admin_sel_name")
                new_status = st.selectbox("New Status", ["Pending","Completed","Recorded"], key="admin_status")
                reassign_to = st.selectbox("Assign to staff (leave blank to skip)", [""] + [e for e,r in users_db.items() if r["role"]=="Staff"], key="admin_assign")
                do_update = st.form_submit_button("Apply Update")
                if do_update:
                    df_all = load_appointments()
                    mask = df_all["Name"] == sel_email
                    if mask.any():
                        if new_status:
                            df_all.loc[mask, "Status"] = new_status
                        if reassign_to:
                            df_all.loc[mask, "AssignedTo"] = reassign_to
                        save_appointments(df_all)
                        st.success("Update applied.")
                    else:
                        st.error("No appointment found with that patient name.")

    # Record patient info (both staff and admin)
    st.subheader("Record Patient Information")
    with st.form("record_patient_form", clear_on_submit=True):
        patient_name = st.text_input("Patient Name")
        patient_notes = st.text_area("Notes / Illness / Treatment")
        submit_notes = st.form_submit_button("Save Patient Notes")
        if submit_notes:
            if patient_name.strip() == "":
                st.error("Please enter patient name")
            else:
                df_all = load_appointments()
                new_row = {"Name":patient_name,"Email":"","Phone":"","Service":"","Date":str(datetime.today().date()),
                           "Notes":patient_notes,"SubmittedAt":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           "Status":"Recorded","AssignedTo":st.session_state.user_email}
                df_all = df_all.append(new_row, ignore_index=True)
                save_appointments(df_all)
                st.success("Patient information recorded.")

    # Admin analytics (simple charts)
    if st.session_state.role == "Admin":
        st.subheader("Analytics")
        df_all = load_appointments()
        if not df_all.empty:
            try:
                df_all["Date"] = pd.to_datetime(df_all["Date"]).dt.date
            except Exception:
                pass
            svc_counts = df_all["Service"].value_counts()
            st.bar_chart(svc_counts)
            # time series: appointments per day
            time_series = df_all.groupby("Date").size()
            if not time_series.empty:
                st.line_chart(time_series)

    # Profile editor
    st.subheader("Profile")
    if st.session_state.role == "Admin":
        admin_profile_management()
    else:
        staff_profile_editor()

# -----------------------
# Main layout & routing
# -----------------------
def main():
    # top-level navigation
    if not st.session_state.logged_in:
        st.title("Welcome to Thrive Mental Wellness Portal")
        choice = st.radio("Choose action", ["Login", "Register"], horizontal=True)

        if choice == "Login":
            st.subheader("Login (official hospital email required)")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_pass")
            if st.button("Login"):
                role = authenticate_user(email, password)
                if role:
                    st.session_state.logged_in = True
                    st.session_state.role = role
                    st.session_state.user_email = email
                    st.success(f"Logged in as {role}")
                    # set trigger to rerun cleanly
                    st.session_state.logout_trigger = False
                    st.rerun()
                else:
                    st.error("Invalid credentials or not an official hospital email")
        else:
            register_user_ui()
    else:
        # check logout trigger from callbacks
        if st.session_state.get("logout_trigger", False):
            st.session_state.logout_trigger = False
            st.rerun()

        # logged in UI
        st.sidebar.markdown(f"**Logged in as:** {st.session_state.user_email}")
        if st.sidebar.button("Logout"):
            logout_user()
            st.rerun()     # safe here to request rerun right after setting trigger

        page = st.sidebar.radio("Navigation", ["Home", "Services", "Staff", "Book Appointment", "Dashboard"], index=0)
        if page == "Home":
            st.markdown('<div class="hero"><h1>Welcome to Thrive Mental Wellness LLC</h1><p>Your mental health is our priority</p></div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="card"><h3>Medication Management</h3><p>Personalized care using medications to manage mental health conditions.</p></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="card"><h3>Psychotherapy</h3><p>Professional therapy sessions to support emotional well-being.</p></div>', unsafe_allow_html=True)
        elif page == "Services":
            st.header("Services")
            st.markdown('<div class="card"><h3>Medication Management</h3><p>Medication titration and monitoring for complex cases.</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="card"><h3>Psychotherapy</h3><p>Evidence-based psychotherapy and supportive therapy sessions.</p></div>', unsafe_allow_html=True)
        elif page == "Staff":
            st.header("Staff Profiles")
            df_profiles = load_profiles()
            if df_profiles.empty:
                st.info("No staff profiles yet. Admin can create profiles in Dashboard.")
            else:
                for _, row in df_profiles.iterrows():
                    photo = row["PhotoPath"] if pd.notna(row["PhotoPath"]) and row["PhotoPath"]!="" else "https://via.placeholder.com/150?text=Photo"
                    c1, c2 = st.columns([1,4])
                    with c1:
                        st.image(photo, width=110)
                    with c2:
                        st.markdown(f"**{row['Name']}**  ")
                        st.markdown(f"*{row['Role']}*  ")
                        st.write(row["Bio"])
                        st.markdown("---")
        elif page == "Book Appointment":
            book_appointment_ui()
        elif page == "Dashboard":
            dashboard_ui()

    # footer
    st.markdown('<div class="footer">© 2025 Thrive Mental Wellness LLC | Contact: info@thrivewellness.com</div>', unsafe_allow_html=True)

# Run
if __name__ == "__main__":
    main()
