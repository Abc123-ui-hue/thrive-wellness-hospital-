import streamlit as st
import sqlite3
from hashlib import sha256
from datetime import datetime
import pandas as pd
import plotly.express as px

# ---------- Page Config ----------
st.set_page_config(page_title="Thrive Mental Wellness", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp { background: linear-gradient(to right, #74ebd5, #acb6e5); color: #0a3d62; }
h1,h2,h3,h4 { color:#0a3d62; font-family: 'Helvetica', sans-serif; }
.card { background-color: rgba(255,255,255,0.85); border-radius: 15px; padding: 20px; margin-bottom:20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);}
div.stButton > button { background-color:#0a3d62; color:white; border-radius:10px; height:40px; width:180px; font-size:16px; }
div.stButton > button:hover { background-color:#3c6382; }
.stAlert { border-left:5px solid #16a085; background-color:#d1f2eb; }
.stTabs [role="tab"] { color:#0a3d62; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------- Database Setup ----------
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

# Users Table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    role TEXT
)""")

# Requests Table
c.execute("""CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    type TEXT,
    description TEXT,
    date TEXT,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY(patient_id) REFERENCES users(id)
)""")

# Reports Table
c.execute("""CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    staff_id INTEGER,
    sickness TEXT,
    solution TEXT,
    date TEXT,
    FOREIGN KEY(patient_id) REFERENCES users(id),
    FOREIGN KEY(staff_id) REFERENCES users(id)
)""")
conn.commit()

# ---------- Helper Functions ----------
def hash_password(password): return sha256(password.encode()).hexdigest()
def register_user(name,email,password,role='patient'):
    try: c.execute("INSERT INTO users (name,email,password,role) VALUES (?,?,?,?)",(name,email,hash_password(password),role)); conn.commit(); return True
    except sqlite3.IntegrityError: return False
def login_user(email,password): c.execute("SELECT * FROM users WHERE email=? AND password=?",(email,hash_password(password))); return c.fetchone()
def submit_request(patient_id,type_,desc,date): c.execute("INSERT INTO requests (patient_id,type,description,date) VALUES (?,?,?,?)",(patient_id,type_,desc,date)); conn.commit()
def get_user_requests(patient_id): c.execute("SELECT * FROM requests WHERE patient_id=?",(patient_id,)); return c.fetchall()
def get_all_requests(): c.execute("""SELECT requests.id, users.name, users.email, requests.type, requests.description, requests.date, requests.status 
    FROM requests JOIN users ON requests.patient_id=users.id"""); return c.fetchall()
def update_request_status(request_id,status): c.execute("UPDATE requests SET status=? WHERE id=?",(status,request_id)); conn.commit()
def submit_report(patient_id,staff_id,sickness,solution,date): c.execute("INSERT INTO reports (patient_id,staff_id,sickness,solution,date) VALUES (?,?,?,?,?)",(patient_id,staff_id,sickness,solution,date)); conn.commit()
def get_patient_reports(patient_id): c.execute("SELECT * FROM reports WHERE patient_id=?",(patient_id,)); return c.fetchall()
def get_all_reports(): c.execute("""SELECT reports.id, p.name, s.name, reports.sickness, reports.solution, reports.date 
    FROM reports JOIN users p ON reports.patient_id=p.id JOIN users s ON reports.staff_id=s.id"""); return c.fetchall()
def get_kpi(): 
    c.execute("SELECT COUNT(*) FROM users WHERE role='patient'"); total_patients=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE role='staff'"); total_staff=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM requests"); total_requests=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM requests WHERE status='Pending'"); pending=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM requests WHERE status='Approved'"); approved=c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM requests WHERE status='Rejected'"); rejected=c.fetchone()[0]
    return total_patients,total_staff,total_requests,pending,approved,rejected

# ---------- Streamlit UI ----------
menu = ["Home","Register","Login"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------- Home ----------
if choice=="Home":
    st.markdown('<div class="card"><h1>Welcome to Thrive Mental Wellness Portal</h1><p>Professional mental wellness management for patients and staff.</p></div>',unsafe_allow_html=True)

# ---------- Register ----------
elif choice=="Register":
    st.markdown('<div class="card"><h2>Create Account</h2></div>',unsafe_allow_html=True)
    name=st.text_input("Full Name"); email=st.text_input("Email"); password=st.text_input("Password",type="password")
    role=st.selectbox("Role",["patient","staff","admin"])
    if st.button("Register"):
        if register_user(name,email,password,role): st.success("Registration successful! Login now.")
        else: st.error("Email already exists. Try a different one.")

# ---------- Login ----------
elif choice=="Login":
    st.markdown('<div class="card"><h2>Login</h2></div>',unsafe_allow_html=True)
    email=st.text_input("Email"); password=st.text_input("Password",type="password")
    if st.button("Login"):
        user=login_user(email,password)
        if user: st.session_state['user']=user; st.success(f"Welcome {user[1]}! Role: {user[4]}")
        else: st.error("Invalid email or password")

# ---------- Dashboard ----------
if 'user' in st.session_state:
    user=st.session_state['user']
    st.markdown(f'<div class="card"><h2>Dashboard</h2><p>Logged in as <b>{user[1]}</b> | Role: <b>{user[4]}</b></p></div>',unsafe_allow_html=True)

    # ---------- Patient ----------
    if user[4]=="patient":
        tab1,tab2=st.tabs(["My Requests","My Reports"])
        with tab1:
            st.markdown('<div class="card"><h3>Submit Therapy/Wellness Request</h3></div>',unsafe_allow_html=True)
            req_type=st.selectbox("Request Type",["Therapy Session","General Wellness"]); desc=st.text_area("Description"); date=st.date_input("Preferred Date",datetime.today())
            if st.button("Submit Request", key="patient_submit_request"):
                submit_request(user[0], req_type, desc, date)
                st.success("Request Submitted!")

            st.markdown('<div class="card"><h3>My Requests Status</h3></div>',unsafe_allow_html=True)
            requests=get_user_requests(user[0])
            for r in requests:
                color={"Pending":"orange","Approved":"green","Rejected":"red"}[r[5]]
                st.markdown(f'<b>{r[2]}</b>: {r[3]} | Date: {r[4]} | <span style="color:{color};font-weight:bold;">{r[5]}</span>',unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card"><h3>My Reports</h3></div>',unsafe_allow_html=True)
            reports=get_patient_reports(user[0])
            for r in reports:
                st.info(f"Sickness: {r[3]}, Solution: {r[4]}, Date: {r[5]}")

    # ---------- Staff ----------
    elif user[4]=="staff":
        tab1,tab2=st.tabs(["Patient Requests","Submit Report"])
        with tab1:
            st.markdown('<div class="card"><h3>All Patient Requests</h3></div>',unsafe_allow_html=True)
            requests=get_all_requests()
            for r in requests:
                if r[6]=="Pending":
                    st.markdown(f'Patient: {r[1]} | Type: {r[3]} | Desc: {r[4]} | Date: {r[5]} | Status: {r[6]}')

        with tab2:
            st.markdown('<div class="card"><h3>Submit Sickness Report & Solution</h3></div>',unsafe_allow_html=True)
            c.execute("SELECT id,name FROM users WHERE role='patient'"); patients=c.fetchall()
            patient_select=st.selectbox("Select Patient",[f"{p[1]}|{p[0]}" for p in patients])
            sickness=st.text_area("Sickness"); solution=st.text_area("Solution"); date=st.date_input("Report Date",datetime.today())
            if st.button("Submit Report", key=f"submit_report_{patient_select}"):
                pid=int(patient_select.split("|")[1])
                submit_report(pid,user[0],sickness,solution,date)
                st.success("Report Submitted!")

    # ---------- Admin ----------
    elif user[4]=="admin":
        tab1,tab2,tab3,tab4=st.tabs(["Users","Manage Requests","Analytics","KPIs"])
        with tab1:
            st.markdown('<div class="card"><h3>Registered Users</h3></div>',unsafe_allow_html=True)
            c.execute("SELECT id,name,email,role FROM users"); users=c.fetchall()
            for u in users: st.info(f"ID:{u[0]}, Name:{u[1]}, Email:{u[2]}, Role:{u[3]}")

        with tab2:
            st.markdown('<div class="card"><h3>Manage Requests</h3></div>',unsafe_allow_html=True)
            requests=get_all_requests()
            for r in requests:
                color={"Pending":"orange","Approved":"green","Rejected":"red"}[r[6]]
                st.markdown(f'Patient:{r[1]} | Type:{r[3]} | Desc:{r[4]} | Date:{r[5]} | <span style="color:{color};font-weight:bold;">{r[6]}</span>',unsafe_allow_html=True)
                cols=st.columns(2)
                if cols[0].button(f"Approve {r[0]}",key=f"approve_{r[0]}"):
                    update_request_status(r[0],"Approved")
                    st.success(f"Request {r[0]} Approved")
                if cols[1].button(f"Reject {r[0]}",key=f"reject_{r[0]}"):
                    update_request_status(r[0],"Rejected")
                    st.error(f"Request {r[0]} Rejected")

        with tab3:
            st.markdown('<div class="card"><h3>Analytics Dashboard</h3></div>',unsafe_allow_html=True)
            df=pd.read_sql_query("SELECT type,status,date FROM requests",conn)
            if not df.empty:
                status_count=df['status'].value_counts().reset_index(); status_count.columns=['Status','Count']
                fig1=px.pie(status_count,names='Status',values='Count',title="Requests by Status"); st.plotly_chart(fig1,use_container_width=True)
                type_count=df['type'].value_counts().reset_index(); type_count.columns=['Type','Count']
                fig2=px.bar(type_count,x='Type',y='Count',color='Type',title="Requests by Type"); st.plotly_chart(fig2,use_container_width=True)
                df['date']=pd.to_datetime(df['date']); time_count=df.groupby(df['date'].dt.date).size().reset_index(name='Count')
                fig3=px.line(time_count,x='date',y='Count',title="Requests Over Time"); st.plotly_chart(fig3,use_container_width=True)
            else: st.info("No requests to show analytics.")

        with tab4:
            st.markdown('<div class="card"><h3>Key KPIs</h3></div>',unsafe_allow_html=True)
            total_patients,total_staff,total_requests,pending,approved,rejected=get_kpi()
            st.success(f"Total Patients: {total_patients}")
            st.info(f"Total Staff: {total_staff}")
            st.warning(f"Pending Requests: {pending}")
            st.success(f"Approved Requests: {approved}")
            st.error(f"Rejected Requests: {rejected}")

    # ---------- Logout ----------
    if st.button("Logout", key="logout_button"):
        del st.session_state['user']
        st.success("Logged out successfully.")
