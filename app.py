import streamlit as st
import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# 🔹 Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()  # Firestore Database Client

# 🔹 Custom CSS for styling
st.markdown(    """
    <style>
        /* Full Page Background */
        body {
            background-image: url('https://www.publicdomainpictures.net/pictures/50000/velka/blue-medical-background.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-color: #f0f4f8; /* Fallback color */
        }

        /* Card Containers */
        .patient-container, .doctor-container {
            padding: 20px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.9);  /* Slight transparency */
            box-shadow: 0px 5px 8px rgba(0, 0, 0, 0.15);
        }

        /* Buttons */
        .btn-primary, .btn-danger {
            padding: 12px 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-primary {
            background-color: #007bff;
            color: white;
        }

        .btn-primary:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }

        .btn-danger {
            background-color: red;
            color: white;
        }

        .btn-danger:hover {
            background-color: darkred;
            transform: scale(1.05);
        }
    </style>
    """
, unsafe_allow_html=True)

# 🔹 Session State Initialization
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'role' not in st.session_state:
    st.session_state.role = None
if 'sos_triggered' not in st.session_state:
    st.session_state.sos_triggered = False
if 'sos_time' not in st.session_state:
    st.session_state.sos_time = None

# 🔹 Login Page
if not st.session_state.authenticated:
    st.markdown("<div class='centered-box'>", unsafe_allow_html=True)
    #st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    st.title("🔒 Login")
    username = st.text_input("👤 Username:")
    password = st.text_input("🔑 Password:", type="password")
    role = st.radio("Login as:", ["Patient", "Doctor"])

    if st.button("Login", key="login", help="Click to login"):
        if username and password:
            st.session_state.authenticated = True
            st.session_state.role = role
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("⚠ Invalid credentials!")

    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    st.sidebar.write(f"👤 **Logged in as:** {st.session_state.username} ({st.session_state.role})")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.username = None
        st.session_state.sos_triggered = False
        st.rerun()

# 🔹 Patient Portal
if st.session_state.authenticated and st.session_state.role == "Patient":
    #st.markdown("<div class='patient-container'>", unsafe_allow_html=True)
    st.title("🏥 Patient Portal")
    st.subheader("Enter your health data below:")

    date_input = st.date_input("📅 Select Date:", datetime.date.today(), help="Pick a date")
    formatted_date = date_input.strftime('%Y-%m-%d')

    # 🔹 Input Health Data
    bp = st.text_input("🩸 Blood Pressure (e.g., 120/80):")
    heart_rate = st.text_input("💓 Heart Rate (BPM):")
    pulse = st.text_input("🖐 Pulse Rate:")

    if st.button("📤 Submit Data", key="submit", help="Save health records", 
                 on_click=lambda: st.success("✅ Health data submitted successfully!")):
        if bp and heart_rate and pulse:
            patient_ref = db.collection("patients").document(st.session_state.username)
            patient_ref.set({
                formatted_date: {
                    "bp": bp,
                    "heart_rate": heart_rate,
                    "pulse": pulse,
                    "timestamp": datetime.datetime.now().isoformat()
                }
            }, merge=True)
        else:
            st.error("⚠ Please enter all health details.")

    # 🔹 SOS Emergency Button
    if st.button("🚨 SOS Emergency", key="sos", help="Alert the doctor in case of emergency", 
                 on_click=lambda: st.warning("🚨 SOS Alert Sent!")):
        sos_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.collection("sos_alerts").document("latest_sos").set({
            "patient": st.session_state.username,
            "time": sos_time
        })

    st.markdown("</div>", unsafe_allow_html=True)

# 🔹 Doctor Portal
elif st.session_state.authenticated and st.session_state.role == "Doctor":
    #st.markdown("<div class='doctor-container'>", unsafe_allow_html=True)
    st.title("👨‍⚕️ Doctor Portal")
    st.subheader("Select a patient to view records.")

    # 🔥 Check if an SOS alert exists
    sos_doc = db.collection("sos_alerts").document("latest_sos").get()
    sos_data = sos_doc.to_dict()

    if sos_data:
        st.markdown(f"<p class='sos-alert'>🚨 **SOS ALERT from {sos_data['patient']} at {sos_data['time']}!**</p>", 
                    unsafe_allow_html=True)

    # Fetch patient list
    patients_ref = db.collection("patients").stream()
    patient_list = [doc.id for doc in patients_ref]

    if patient_list:
        selected_patient = st.selectbox("Select Patient:", patient_list, help="Choose a patient to view records")
        selected_date = st.date_input("📅 Select Date:", datetime.date.today(), help="Pick a date to view health data")
        formatted_date = selected_date.strftime('%Y-%m-%d')

        # Fetch selected patient's data
        patient_data = db.collection("patients").document(selected_patient).get().to_dict()

        if patient_data and formatted_date in patient_data:
            st.write(f"### 🏥 Health Data for {selected_patient} on {formatted_date}:")
            st.json(patient_data[formatted_date])
        else:
            st.warning("⚠ No health data found for this date.")
    else:
        st.info("⚠ No patient records found.")

    st.markdown("</div>", unsafe_allow_html=True)
