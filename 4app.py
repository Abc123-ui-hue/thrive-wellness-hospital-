import streamlit as st
from datetime import datetime
import pandas as pd
import os
import plotly.express as px

# ---------- CSS Styling ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #E6F2FF; }
h1,h2,h3 { font-family: 'Lato', sans-serif; color: #003366; }
.card { background-color: white; padding:20px; border-radius:15px; box-shadow:2px 2px 12px rgba(0,0,0,0.1); margin-bottom:20px; transition: transform 0.3s; }
.card:hover { transform: scale(1.03); }
button, .stButton>button { background: linear-gradient(90deg,#0072E3,#00BFFF); color:white; padding:10px 20px; border-radius:10px; border:none; font-weight:bold; }
button:hover, .stButton>button:hover { background: linear-gradient(90deg,#005BB5,#0095CC); }
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.session_state.staff_index = 0

# ---------- Dummy User Database ----------
users_db = {
    "admin@example.com": {"password": "admin123", "role": "Admin"},
    "staff1@example.com": {"password": "staff123", "role": "Staff"},
    "staff2@example.com": {"password": "staff123", "role": "Staff"}
}

# ---------- Helper Functions ----------
def authenticate_user(email, password):
    if email in users_db and users_db[email]["password"] == password:
        return users_db[email]["role"]
    return None

def logout_user():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_email = None
    st.experimental_rerun()

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
    st.markdown('<div class="card"><h1>Welcome to Thrive Mental Wellness LLC</h1><p>Your mental health is our priority.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h2>Services</h2><ul><li>Medication Management</li><li>Psychotherapy</li></ul></div>', unsafe_allow_html=True)

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
        st.info("Email notifications are placeholders and will be added later.")
        st.info("Telehealth link placeholder: https://example.com/telehealth")

# ---------- Dashboard ----------
def dashboard():
    st.subheader(f"{'Admin' if st.session_state.role=='Admin' else 'Staff'} Dashboard")
    df = load_csv("appointments.csv", ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"])
    if st.session_state.role=="Staff":
        df = df[df["AssignedTo"]==st.session_state.user_email]
    
    st.markdown("### Appointment Table / Calendar")
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Try AgGrid, fallback to simple table
    try:
        from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
        df["StatusColor"] = df["Status"].apply(lambda x: 'lightgreen' if x=="Completed" else 'yellow')
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_selection(selection_mode="single", use_checkbox=True)
        gb.configure_column("Status", cellStyle=lambda params: {'backgroundColor': 'lightgreen' if params.value=="Completed" else 'yellow'})
        grid_options = gb.build()
        grid_response = AgGrid(df, gridOptions=grid_options, update_mode=GridUpdateMode.SELECTION_CHANGED)
        selected = grid_response["selected_rows"]
    except ModuleNotFoundError:
        st.warning("Optional module 'st-aggrid' not installed. Displaying simple table.")
        st.dataframe(df)
        selected = []

    if selected:
        st.markdown("### Selected Appointment Details")
        sel = selected[0]
        st.write(f"**Patient:** {sel['Name']}")
        st.write(f"**Service:** {sel['Service']}")
        st.write(f"**Date:** {sel['Date']}")
        st.write(f"**Notes:** {sel['Notes']}")
        st.write(f"**Assigned To:** {sel['AssignedTo']}")
        status = sel['Status']
        new_status = st.selectbox("Update Status", ["Pending","Completed"], index=0 if status=="Pending" else 1)
        if st.button("Update Status"):
            idx = df.index[df["Name"]==sel["Name"]][0]
            df.at[idx, "Status"] = new_status
            save_csv(df, "appointments.csv")
            st.success("Status updated!")
            st.experimental_rerun()
    
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
    
    # ---------- Analytics Charts ----------
    if st.session_state.role=="Admin":
        st.markdown("### Analytics Dashboard")
        df_all = load_csv("appointments.csv", ["Name","Email","Phone","Service","Date","Notes","SubmittedAt","Status","AssignedTo"])
        if not df_all.empty:
            service_chart = px.bar(df_all["Service"].value_counts().reset_index(), x='index', y='Service', labels={'index':'Service','Service':'Count'}, title="Appointments per Service")
            st.plotly_chart(service_chart)
            df_all["Date"] = pd.to_datetime(df_all["Date"])
            daily_chart = px.line(df_all.groupby("Date").size().reset_index(name="Appointments"), x="Date", y="Appointments", title="Appointments Over Time")
            st.plotly_chart(daily_chart)
        st.download_button("Download All Appointments CSV", df_all.to_csv(index=False), file_name="appointments.csv")

# ---------- Main App ----------
if not st.session_state.logged_in:
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        role = authenticate_user(email, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.session_state.user_email = email
            st.success(f"Logged in as {role}")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
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
