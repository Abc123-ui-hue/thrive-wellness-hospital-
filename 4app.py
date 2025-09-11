# app.py
import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# ---------------- Email Config ----------------
EMAIL_SENDER = "muthwiimeshack@gmail.com"
EMAIL_PASSWORD = "rkubtmzydtgymkrf"  # Gmail App Password
EMAIL_RECEIVER = "muthwiimeshack@gmail.com"

# ---------------- Initialize session state ----------------
if "submissions" not in st.session_state:
    st.session_state["submissions"] = pd.DataFrame(columns=[
        "Name", "Email", "Phone", "Service", "Date & Time", "Submitted At"
    ])

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Thrive Mental Wellness")
page = st.sidebar.radio("Navigate", ["Home", "Services", "Staff", "Book Appointment", "Admin", "Legal"])

# ---------------- Custom CSS & Animations ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Roboto&family=Lato&display=swap" rel="stylesheet">
<style>
body { font-family: 'Roboto', sans-serif; background-color:#f4f6f7; }
h1,h2,h3,h4 { font-family: 'Lato', sans-serif; }
.hero { background-color:#a0d8f1; padding:50px; border-radius:10px; text-align:center; color:#003366; animation: fadeIn 2s; }
.card { background-color:white; padding:20px; border-radius:10px; box-shadow:2px 2px 12px rgba(0,0,0,0.1); margin-bottom:20px; transition: transform 0.3s;}
.card:hover { transform: scale(1.03); }
.card img:hover { transform: scale(1.05); box-shadow: 4px 4px 20px rgba(0,0,0,0.2);}
button:hover { background-color: #009e8f; transition: 0.3s; }
a.button:hover { transform: scale(1.05); transition: 0.3s;}
@keyframes fadeIn { 0% {opacity: 0;} 100% {opacity: 1;} }
</style>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.image("images/thrive_logo.png", width=200)
    st.markdown("""
    <div class='hero'>
        <h1>🧠 Thrive Mental Wellness LLC</h1>
        <p>Comprehensive mental health care in a warm and welcoming environment</p>
        <a href='#appointment' class='button' style='background-color:#00bfa5;color:white;padding:10px 20px;border-radius:5px;text-decoration:none;'>Book Appointment</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)
    st.write("Welcome to Thrive Mental Wellness. Our team provides expert psychiatric care, including medication management and psychotherapy, tailored to your needs.")

# ---------------- SERVICES PAGE ----------------
elif page == "Services":
    st.title("Our Services")
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'><h3>Medication Management</h3><p>Comprehensive evaluation and monitoring of psychiatric medications.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><h3>Psychotherapy</h3><p>Individual, group, and family therapy sessions for mental health support.</p></div>", unsafe_allow_html=True)

# ---------------- STAFF PAGE ----------------
elif page == "Staff":
    st.title("Meet Our Staff")
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    
    st.write("Upload your photo below (admins/staff only):")
    uploaded_file = st.file_uploader("Upload Staff Photo", type=["png","jpg","jpeg"])
    camera_image = st.camera_input("Or take a photo with your camera")
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Staff Photo", use_column_width=True)
    elif camera_image:
        st.image(camera_image, caption="Captured Photo", use_column_width=True)
    
    name = st.text_input("Full Name")
    role = st.text_input("Role / Position")
    bio = st.text_area("Short Bio / Specialty")
    
    if st.button("Save Staff Profile"):
        if uploaded_file or camera_image:
            img_to_save = uploaded_file if uploaded_file else camera_image
            img_name = f"{name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            with open(f"images/{img_name}", "wb") as f:
                f.write(img_to_save.getbuffer())
            st.success(f"✅ Staff profile saved for {name} ({role})")
        else:
            st.error("Please upload a photo or take a photo before saving")

# ---------------- APPOINTMENT BOOKING PAGE ----------------
elif page == "Book Appointment":
    st.title("📅 Book an Appointment")
    st.markdown("<div id='appointment'></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><p>Please fill the form below and our staff will contact you to confirm your appointment.</p></div>", unsafe_allow_html=True)
    
    with st.form("appointment_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        service = st.selectbox("Select Service", ["Medication Management", "Psychotherapy"])
        date_time = st.date_input("Preferred Date")
        submit = st.form_submit_button("Submit Appointment")
    
    if submit:
        submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.submissions.loc[len(st.session_state.submissions)] = [name, email, phone, service, date_time, submitted_at]
        st.success("✅ Appointment submitted successfully!")
        try:
           msg_content = f"""New Appointment Submission
            Name: {name}
            Email: {email}
            Phone: {phone}
            Service: {service}
            Date: {date_time}
            Submitted At: {submitted_at}"""

            msg = MIMEText(msg_content)
            msg["Subject"] = "New Appointment Submission - Thrive Mental Wellness"
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)
            st.info("📧 Notification sent to clinic email.")
        except Exception as e:
            st.error(f"❌ Email failed: {e}")

# ---------------- ADMIN PAGE ----------------
elif page == "Admin":
    st.title("Admin Dashboard")
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    st.write("View all appointment submissions")
    st.dataframe(st.session_state.submissions)
    csv = st.session_state.submissions.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="appointments.csv")
    
    if not st.session_state.submissions.empty:
        st.subheader("Appointment Analytics")
        df = st.session_state.submissions
        st.write("Total Appointments:", len(df))
        st.bar_chart(df['Service'].value_counts())
        df['Submitted At'] = pd.to_datetime(df['Submitted At'])
        st.line_chart(df.groupby(df['Submitted At'].dt.date)['Name'].count())

# ---------------- LEGAL PAGE ----------------
elif page == "Legal":
    st.title("Legal Information")
    st.subheader("Privacy Policy")
    st.write("All patient data is kept confidential and stored securely. HIPAA compliance is maintained at all times.")
    st.subheader("Terms of Service")
    st.write("Use of this site constitutes agreement to our terms. Appointments are subject to clinic policies.")
