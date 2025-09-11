import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ---------- CSS Styling ----------
st.markdown("""
<style>
/* Full-page background */
[data-testid="stAppViewContainer"] { 
    background: linear-gradient(135deg, #e0f7fa 0%, #80deea 100%);
    color: #003366;
    font-family: 'Lato', sans-serif;
}

/* Hero section */
.hero {
    background-image: url('https://via.placeholder.com/1200x400?text=Thrive+Mental+Wellness');
    background-size: cover;
    background-position: center;
    padding: 80px 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
}

/* Cards for sections */
.card { 
    background-color: white; 
    padding:20px; 
    border-radius:15px; 
    box-shadow:2px 2px 15px rgba(0,0,0,0.15); 
    margin-bottom:20px; 
    transition: transform 0.3s; 
}
.card:hover { transform: scale(1.03); }

/* Buttons */
button, .stButton>button { 
    background: linear-gradient(90deg,#0072E3,#00BFFF); 
    color:white; 
    padding:10px 20px; 
    border-radius:12px; 
    border:none; 
    font-weight:bold; 
    transition: 0.3s; 
}
button:hover, .stButton>button:hover { 
    background: linear-gradient(90deg,#005BB5,#0095CC); 
}

/* Input fields styling */
.stTextInput>div>div>input, 
.stTextArea>div>div>textarea, 
.stSelectbox>div>div>div>select {
    border-radius:10px; 
    border:1px solid #0072E3; 
    padding:5px;
}

/* Sidebar */
[data-testid="stSidebar"] { background: #b2ebf2; }

/* Footer */
.footer { 
    text-align:center; 
    padding:20px; 
    font-size:14px; 
    color:#003366; 
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.session_state.staff_index = 0

# ---------- Users Database ----------
def load_users():
    pre_populated = [
        {"Email":"admin@thrivewellness.com","Password":"Admin123!","Role":"Admin"},
        {"Email":"staff1@thrivewellness.com","Password":"Staff123!","Role":"Staff"},
        {"Email":"staff2@thrivewellness.com","Password":"Staff123!","Role":"Staff"}
    ]
    
    if os.path.exists("users.csv"):
        df = pd.read_csv("users.csv")
    else:
        df = pd.DataFrame(pre_populated)
        df.to_csv("users.csv", index=False)
    
    return {row["Email"]: {"password": row["Password"], "role": row["Role"]} for idx, row in df.iterrows()}

users_db = load_users()

def save_user(email, password, role):
    new_df = pd.DataFrame([{"Email": email, "Password": password, "Role": role}])
    if os.path.exists("users.csv"):
        new_df.to_csv("users.csv", mode='a', header=False, index=False)
    else:
        new_df.to_csv("users.csv", index=False)

# ---------- Authentication ----------
def authenticate_user(email, password):
    if not email.endswith("@thrivewellness.com"):
        return None
    if email in users_db and users_db[email]["password"] == password:
        return users_db[email]["role"]
    return None

def logout_user():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.rerun()

# ---------- Registration ----------
def register_user():
    st.subheader("Register New User (Official Email Only)")
    new_email = st.text_input("Email", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_password")
    role = st.selectbox("Role", ["Admin", "Staff"], key="reg_role")
    
    if st.button("Register", key="reg_btn"):
        if not new_email.endswith("@thrivewellness.com"):
            st.error("Please use your official hospital email")
        elif new_email.strip() == "" or new_password.strip() == "":
            st.error("Please provide both email and password")
        elif new_email in users_db:
            st.error("User already exists")
        else:
            users_db[new_email] = {"password": new_password, "role": role}
            save_user(new_email, new_password, role)
            st.success(f"{role} registered successfully! You can now log in.")

# ---------- Helper Functions ----------
def load_csv(filename, columns):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=columns)

def save_csv(df, filename):
    df.to_csv(filename, index=False)

def assign_staff():
    staff_emails = [email for email, info in users_db.items() if info["role"]=="Staff"]
    if staff_emails:
        assigned = staff_emails[st.session_state.staff_index % len(staff_emails)]
        st.session_state.staff_index += 1
        return assigned
    return ""

# ---------- Pages ----------
def home_page():
    st.markdown(
        """<div class="hero"><h1>Welcome to Thrive Mental Wellness LLC</h1>
        <p>Your mental health is our priority</p></div>""", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h2>Medication Management</h2><p>Personalized care using medications to manage mental health conditions.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h2>Psychotherapy</h2><p>Professional therapy sessions to support emotional well-being.</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><h2>Book Your Appointment</h2><p>Click the Book Appointment tab in the sidebar to schedule your session.</p></div>', unsafe_allow_html=True)

def staff_page():
    st.subheader("Staff Profiles")
    staff_df = load_csv("staff_profiles.csv", ["Name","Role","Bio","Photo"])
    for idx, row in staff_df.iterrows():
        photo = row["Photo"] if pd.notna(row["Photo"]) else "https://via.placeholder.com/150?text=Staff+Photo"
        st.image(photo, width=150)
        st.write(f"**{row['Name']}** - {row['Role']}")
        st.write(row['Bio'])
        st.write("---")

def book_appointment():
    st.subheader("Book Appointment")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    service = st.selectbox("Service", ["Medication Management", "Psychotherapy"])
    date_time = st.date_input("Preferred Date")
    notes = st.text_area("Additional Notes")
    
    if st.button("Submit Appointment"):
        assigned_staff = assign_staff()
        submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = load_csv("appointments.csv", ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"])
        df = df.append({"Name":name,"Email":email,"Phone":phone,"Service":service,"Date":date_time,"Notes":notes,
                        "SubmittedAt":submitted_at,"Status":"Pending","AssignedTo":assigned_staff}, ignore_index=True)
        save_csv(df, "appointments.csv")
        st.success(f"Appointment submitted! Assigned to: {assigned_staff}")
        st.info("Telehealth link placeholder: https://example.com/telehealth")

def dashboard():
    st.subheader(f"{'Admin' if st.session_state.role=='Admin' else 'Staff'} Dashboard")
    df = load_csv("appointments.csv", ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"])
    if st.session_state.role=="Staff":
        df = df[df["AssignedTo"]==st.session_state.user_email]
    
    st.markdown("### Appointment Table")
    st.dataframe(df)

    st.markdown("### Record Patient Information")
    patient_name = st.text_input("Patient Name")
    patient_notes = st.text_area("Notes / Illness / Treatment")
    if st.button("Save Patient Notes"):
        if patient_name.strip() != "":
            new_row = {"Name":patient_name,"Email":"","Phone":"","Service":"","Date":datetime.today().date(),
                       "Notes":patient_notes,"SubmittedAt":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                       "Status":"Recorded","AssignedTo":st.session_state.user_email}
            df_all = load_csv("appointments.csv", ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"])
            df_all = df_all.append(new_row, ignore_index=True)
            save_csv(df_all, "appointments.csv")
            st.success("Patient information recorded!")

    st.markdown("### Upload Profile Photo")
    uploaded_file = st.file_uploader("Upload photo", type=["png","jpg","jpeg"])
    if uploaded_file is not None:
        staff_df = load_csv("staff_profiles.csv", ["Name","Role","Bio","Photo"])
        staff_df = staff_df.append({"Name":st.session_state.user_email,"Role":st.session_state.role,"Bio":"","Photo":uploaded_file.getvalue()}, ignore_index=True)
        save_csv(staff_df, "staff_profiles.csv")
        st.success("Profile photo uploaded!")

# ---------- Main App ----------
if not st.session_state.logged_in:
    st.title("Welcome to Thrive Mental Wellness Portal")
    
    tab = st.radio("Choose Action", ["Login", "Register"], horizontal=True)
    
    if tab == "Login":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            role = authenticate_user(email, password)
            if role:
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.user_email = email
                st.success(f"Logged in as {role}")
                st.rerun()

            else:
                st.error("Invalid credentials or not an official hospital email")
    elif tab == "Register":
        register_user()
else:
    st.sidebar.button("Logout", on_click=logout_user)
    st.sidebar.title(f"Logged in as: {st.session_state.role}")
    
    page = st.sidebar.radio("Navigation", ["Home", "Services", "Staff", "Book Appointment", "Dashboard"])
    
    if page == "Home":
        home_page()
    elif page == "Services":
        home_page()
    elif page == "Staff":
        staff_page()
    elif page == "Book Appointment":
        book_appointment()
    elif page == "Dashboard":
        dashboard()

# Footer
st.markdown('<div class="footer">© 2025 Thrive Mental Wellness LLC | Contact: info@thrivewellness.com | Follow us on social media</div>', unsafe_allow_html=True)
