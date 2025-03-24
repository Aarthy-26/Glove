# import streamlit as st
# st.set_page_config(page_title="Doctor-Patient Interface", layout="wide")  # ✅ Must be the first Streamlit command

# from datetime import date
# import pandas as pd
# import random

# st.title("Welcome")

# # Predefined user credentials (Replace this with a database in a real app)
# USER_CREDENTIALS = {
#     "doctor": {"password": "doctor123", "role": "Doctor"},
#     "patient": {"password": "patient123", "role": "Patient"},
# }


# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False
# if "role" not in st.session_state:
#     st.session_state.role = None

# # Login Page
# def login():
#     st.title("🔐 Login Page")
    
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     login_button = st.button("Login")

#     if login_button:
#         if username in USER_CREDENTIALS and USER_CREDENTIALS[username]["password"] == password:
#             st.session_state.authenticated = True
#             st.session_state.role = USER_CREDENTIALS[username]["role"]
#             st.success(f"✅ Welcome, {username} ({st.session_state.role})!")
#             st.rerun()

#         else:
#             st.error("🚫 Incorrect Username or Password!")

# # Logout Function
# def logout():
#     st.session_state.authenticated = False
#     st.session_state.role = None
#     st.rerun()


# # If not logged in, show the login page
# if not st.session_state.authenticated:
#     login()
# else:
#     # Show Logout Button
#     st.sidebar.button("Logout", on_click=logout)

#     # Main App
    

#     # Sidebar Navigation
#     menu = ["Home", "Patient Data", "Doctor Details", "Gamified Rehab Dashboard"]
#     choice = st.sidebar.radio("📌 Menu", menu)

# # Sample user data (replace with actual data retrieval logic)
# user_data = {
#     "username": "Ram Kumar",
#     "progress": 70,  # Percentage completion
#     "level": 3,
#     "badges": ["Starter", "Consistency", "Halfway There"],
# }

# # Sample leaderboard data
# leaderboard = pd.DataFrame({
#     "Username": ["Anne", "Boss", "Ram Kumar", "Eva"],
#     "Level": [5, 4, 3, 2],
#     "Progress": [90, 80, 70, 60]
# }).sort_values(by="Progress", ascending=False)

# # Ensure that the patients' data persists across page refreshes
# if "patients" not in st.session_state:
#     st.session_state.patients = {"Ram Kumar": {}}  # Initialize with an empty dictionary for 'Ram Kumar'

# # Doctor Details
# doctors = {
#     "dr.Haran": {"name": "Dr. Haran", "specialization": "Cardiology"}
# }



# menu = ["Home", "Patient Data", "Doctor Details", "Gamified Rehab Dashboard"]
# choice = st.sidebar.radio("📌 Menu", menu)

# # ============================
# # Home Page
# # ============================
# if choice == "Home":
#     st.markdown("""
#         ### Welcome to the **Doctor-Patient Interface** 👨‍⚕️👩‍⚕️
#         This platform allows doctors to monitor and update patient health records.
#     """)

#     game_choice = st.selectbox("Choose a Game", ["Select a Game", "Number Guessing Game", "Trivia Quiz"])

#     if game_choice == "Number Guessing Game":
#         st.subheader("🎮 Number Guessing Game")
#         st.write("Guess the number between 1 and 100!")
        
#         # Initialize session state for the game
#         if "number" not in st.session_state:
#             st.session_state.number = random.randint(1, 100)
#             st.session_state.attempts = 0
        
#         guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
        
#         if st.button("Submit Guess"):
#             st.session_state.attempts += 1
#             if guess < st.session_state.number:
#                 st.write("Too low! Try again.")
#             elif guess > st.session_state.number:
#                 st.write("Too high! Try again.")
#             else:
#                 st.write(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.attempts} attempts.")
#                 # Reset the game after winning
#                 if st.button("Play Again"):
#                     st.session_state.number = random.randint(1, 100)
#                     st.session_state.attempts = 0

#     elif game_choice == "Trivia Quiz":
#         st.subheader("🧠 Trivia Quiz")
#         st.write("Answer the health-related questions below!")

#         # Question and answers
#         question = "What is the normal human body temperature?"
#         options = ["36.1°C", "37°C", "38.5°C", "39°C"]

#         answer = st.radio(question, options)

#         if st.button("Submit Answer"):
#             if answer == "37°C":
#                 st.write("Correct! The normal body temperature is 37°C.")
#             else:
#                 st.write("Incorrect! The correct answer is 37°C.")

#     # Create layout for SOS button (Positioning it in the top-right corner)
#     sos_button_container = st.empty()

#     with sos_button_container.container():
#         # This will add an SOS button in the top-right corner
#         sos_button = st.button("SOS", key="sos_button")

#     # Check if the SOS button is pressed
#     if sos_button:
#         st.write("SOS Button Pressed!")


# # ============================
# # Patient Data Page
# # ============================
# elif choice == "Patient Data":
#     st.subheader("📋 Patient Data")

#     # Patient info (Only one patient named 'Ram Kumar')
#     patient_id = "Ram Kumar"
#     st.write("Patient Name: Ram Kumar")
#     # Patient selects the date for which they want to update the data
#     date_input = st.date_input("Select Date", value=date.today())
    
#     # Retrieve existing data for the selected date (if any)
#     patient_data = st.session_state.patients[patient_id].get(str(date_input), {})

#     # Create columns for BP, Pulse, and Heartbeat
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         bp = st.text_input("🩸 Blood Pressure", patient_data.get("bp", ""))

#     with col2:
#         pulse = st.text_input("💓 Pulse", patient_data.get("pulse", ""))

#     with col3:
#         heartbeat = st.text_input("❤️ Heartbeat", patient_data.get("heartbeat", ""))
    
#     # Button to update the data
#     if st.button("Update Patient Data"):
#         if bp and pulse and heartbeat:
#             # Update or add data for the selected date
#             st.session_state.patients[patient_id][str(date_input)] = {"bp": bp, "pulse": pulse, "heartbeat": heartbeat}
#             st.success(f"Patient data updated for {date_input}!")
#         else:
#             st.error("Please fill in all fields!")

# # ============================
# # Doctor Details Page
# # ============================
# elif choice == "Doctor Details":
#     st.subheader("🩺 Doctor Details")

#     # Doctor info (Only one doctor 'Dr. Haran')
#     doctor_id = "dr.Haran"
    
#     # Show selected doctor's details
#     st.write(f"{doctors[doctor_id]['name']} - {doctors[doctor_id]['specialization']}")
    
#     # Doctor selects the patient (Only one patient 'Ram Kumar')
#     patient_id = st.selectbox("Select Patient", ["Ram Kumar"])  # Even though there's only one patient
    
#     if patient_id:
#         # Get all available dates for the selected patient
#         available_dates = list(st.session_state.patients[patient_id].keys())
        
#         if available_dates:
#             # Doctor selects the date to view the patient's data
#             date_input = st.date_input("Select Date", value=available_dates[0], min_value=min(available_dates), max_value=date.today())
            
#             # Retrieve and display patient data for the selected date
#             patient_data = st.session_state.patients[patient_id].get(str(date_input), {})
            
#             if patient_data:
#                 st.write(f"Patient Data for {date_input}:")
#                 st.write(f"Blood Pressure: {patient_data.get('bp', 'N/A')}")
#                 st.write(f"Pulse: {patient_data.get('pulse', 'N/A')}")
#                 st.write(f"Heartbeat: {patient_data.get('heartbeat', 'N/A')}")
#             else:
#                 st.write("No data available for this date.")
#         else:
#             st.write("No data available for the selected patient.")

# # ============================
# # Gamified Rehab Dashboard Page
# # ============================
# elif choice == "Gamified Rehab Dashboard":
#     st.title("🏆 Gamified Rehab Dashboard")
#     st.subheader(f"Welcome, {user_data['username']}!")

#     # Progress Bar
#     st.write("### Your Progress")
#     st.progress(user_data["progress"] / 100)
#     st.write(f"You have completed {user_data['progress']}% of your rehabilitation goals.")

#     # Current Level
#     st.write("### Your Level")
#     st.write(f"🎮 Level {user_data['level']}")

#     # Achievements / Badges
#     st.write("### Your Badges")
#     st.write(", ".join([f"🏅 {badge}" for badge in user_data["badges"]]))

#     # Leaderboard
#     st.write("### Leaderboard")
#     st.dataframe(leaderboard, hide_index=True)

#     # Simulation: Earn Random Progress
#     if st.button("Complete a session ✅"):
#         new_progress = min(100, user_data["progress"] + random.randint(5, 15))
#         user_data["progress"] = new_progress
#         if new_progress >= 100:
#             user_data["badges"].append("Champion")
#         st.rerun()

#     st.write("Keep going! You're making great progress! 💪")



# import streamlit as st
# import datetime

# # Set page configuration
# st.set_page_config(page_title="Doctor-Patient Interface", page_icon="🏥", layout="wide")

# # Session state initialization
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False
# if 'role' not in st.session_state:
#     st.session_state.role = None
# if 'patients' not in st.session_state:
#     st.session_state.patients = {}  # Stores patient health data
# if 'doctors' not in st.session_state:
#     st.session_state.doctors = {}
# if 'leaderboard' not in st.session_state:
#     st.session_state.leaderboard = {}

# # Sidebar menu for login/logout and navigation
# with st.sidebar:
#     st.title("User Authentication")
#     if not st.session_state.authenticated:
#         username = st.text_input("Username:")
#         password = st.text_input("Password:", type="password")
#         role = st.radio("Login as:", ["Patient", "Doctor"])
        
#         if st.button("Login"):
#             if username and password:
#                 st.session_state.authenticated = True
#                 st.session_state.role = role
#                 st.session_state.username = username
#                 st.success("Login successful!")
#                 st.rerun()  # Refresh the app
#             else:
#                 st.error("Please enter valid credentials.")
#     else:
#         st.write(f"Logged in as: {st.session_state.username} ({st.session_state.role})")
#         if st.button("Logout"):
#             st.session_state.authenticated = False
#             st.session_state.role = None
#             st.session_state.username = None
#             st.rerun()

# # Main application logic
# if st.session_state.authenticated:
#     st.title("Doctor-Patient Dashboard")

#     if st.session_state.role == "Patient":
#         st.header("Patient Portal")
#         date_input = st.date_input("Select Date:", datetime.date.today())
#         formatted_date = date_input.strftime('%Y-%m-%d')

#         # Patient enters health data
#         bp = st.text_input("Enter Blood Pressure (BP):")
#         heart_rate = st.text_input("Enter Heart Rate (bpm):")
#         pulse = st.text_input("Enter Pulse (bpm):")

#         if st.button("Submit Health Data"):
#             if bp and heart_rate and pulse:
#                 timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Capture time

#                 if st.session_state.username not in st.session_state.patients:
#                     st.session_state.patients[st.session_state.username] = {}

#                 st.session_state.patients[st.session_state.username][formatted_date] = {
#                     "BP": bp,
#                     "Heart Rate": heart_rate,
#                     "Pulse": pulse,
#                     "Timestamp": timestamp
#                 }
#                 st.success("Health data submitted!")
#             else:
#                 st.error("Please fill in all fields.")

#         # SOS Button
#         if st.button("SOS Alert 🚨"):
#             st.warning("SOS Alert Sent!")

#     elif st.session_state.role == "Doctor":
#         st.header("Doctor Portal")
#         st.write("Manage patient data and view progress.")

#         if st.session_state.patients:
#             selected_patient = st.selectbox("Select Patient:", list(st.session_state.patients.keys()))

#             if selected_patient in st.session_state.patients:
#                 st.write(f"Health data for {selected_patient}:")
                
#                 for date, data in st.session_state.patients[selected_patient].items():
#                     st.write(f"📅 Date: {date}")
#                     st.write(f"🕒 Recorded At: {data['Timestamp']}")
#                     st.write(f"💉 Blood Pressure: {data['BP']} mmHg")
#                     st.write(f"❤️ Heart Rate: {data['Heart Rate']} bpm")
#                     st.write(f"💓 Pulse: {data['Pulse']} bpm")
#                     st.markdown("---")
#         else:
#             st.info("No patient records available.")

#     # Gamified Rehab Section
#     st.subheader("Gamified Rehab Dashboard")
#     progress = st.slider("Select Progress:", 0, 100, 50)
#     if st.button("Submit Progress"):
#         st.session_state.leaderboard[st.session_state.username] = progress
#         st.success("Progress updated!")

#     # Leaderboard
#     if st.session_state.leaderboard:
#         sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
#         st.subheader("Leaderboard")
#         for rank, (user, score) in enumerate(sorted_leaderboard, start=1):
#             st.write(f"{rank}. {user}: {score}%")

# else:
#     st.write("Please log in to access the system.")







# import streamlit as st
# import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # 🔹 Initialize Firebase
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()  # Firestore Database Client

# # 🔹 Custom CSS for styling
# st.markdown("""
#     <style>
#         body {
#             font-family: 'Arial', sans-serif;
#         }
#         .centered-box {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 5vh;
#         }
#         .login-container {
#             width: 350px;
#             padding: 20px;
#             border-radius: 10px;
#             background: white;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#             text-align: center;
#         }
#         .sos-alert {
#             color: red;
#             font-weight: bold;
#             font-size: 20px;
#         }
#         .patient-container, .doctor-container {
#             padding: 20px;
#             border-radius: 10px;
#             background: #f8f9fa;
#             box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
#         }
#         .btn-primary {
#             background-color: #007bff;
#             color: white;
#             padding: 10px 15px;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#         .btn-primary:hover {
#             background-color: #0056b3;
#         }
#         .btn-danger {
#             background-color: red;
#             color: white;
#             padding: 10px 15px;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#         .btn-danger:hover {
#             background-color: darkred;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # 🔹 Session State Initialization
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False
# if 'role' not in st.session_state:
#     st.session_state.role = None
# if 'sos_triggered' not in st.session_state:
#     st.session_state.sos_triggered = False
# if 'sos_time' not in st.session_state:
#     st.session_state.sos_time = None

# # 🔹 Login Page
# if not st.session_state.authenticated:
#     #st.markdown("<div class='centered-box'>", unsafe_allow_html=True)
#     #st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
#     st.title("🔒 Login")
#     username = st.text_input("👤 Username:")
#     password = st.text_input("🔑 Password:", type="password")
#     role = st.radio("Login as:", ["Patient", "Doctor"])

#     if st.button("Login", key="login", help="Click to login"):
#         if username and password:
#             st.session_state.authenticated = True
#             st.session_state.role = role
#             st.session_state.username = username
#             st.success("✅ Login successful!")
#             st.rerun()
#         else:
#             st.error("⚠ Invalid credentials!")

#     st.markdown("</div></div>", unsafe_allow_html=True)

# else:
#     st.sidebar.write(f"👤 **Logged in as:** {st.session_state.username} ({st.session_state.role})")
#     if st.sidebar.button("Logout"):
#         st.session_state.authenticated = False
#         st.session_state.role = None
#         st.session_state.username = None
#         st.session_state.sos_triggered = False
#         st.rerun()

# # 🔹 Patient Portal
# if st.session_state.authenticated and st.session_state.role == "Patient":
#     #st.markdown("<div class='patient-container'>", unsafe_allow_html=True)
#     st.title("🏥 Patient Portal")
#     st.subheader("Enter your health data below:")

#     date_input = st.date_input("📅 Select Date:", datetime.date.today(), help="Pick a date")
#     formatted_date = date_input.strftime('%Y-%m-%d')

#     # 🔹 Input Health Data
#     bp = st.text_input("🩸 Blood Pressure (e.g., 120/80):")
#     heart_rate = st.text_input("💓 Heart Rate (BPM):")
#     pulse = st.text_input("🖐 Pulse Rate:")

#     if st.button("📤 Submit Data", key="submit", help="Save health records", 
#                  on_click=lambda: st.success("✅ Health data submitted successfully!")):
#         if bp and heart_rate and pulse:
#             patient_ref = db.collection("patients").document(st.session_state.username)
#             patient_ref.set({
#                 formatted_date: {
#                     "bp": bp,
#                     "heart_rate": heart_rate,
#                     "pulse": pulse,
#                     "timestamp": datetime.datetime.now().isoformat()
#                 }
#             }, merge=True)
#         else:
#             st.error("⚠ Please enter all health details.")

#     # 🔹 SOS Emergency Button
#     if st.button("🚨 SOS Emergency", key="sos", help="Alert the doctor in case of emergency", 
#                  on_click=lambda: st.warning("🚨 SOS Alert Sent!")):
#         sos_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         db.collection("sos_alerts").document("latest_sos").set({
#             "patient": st.session_state.username,
#             "time": sos_time
#         })

#     st.markdown("</div>", unsafe_allow_html=True)

# # 🔹 Doctor Portal
# elif st.session_state.authenticated and st.session_state.role == "Doctor":
#     #st.markdown("<div class='doctor-container'>", unsafe_allow_html=True)
#     st.title("👨‍⚕️ Doctor Portal")
#     st.subheader("Select a patient to view records.")

#     # 🔥 Check if an SOS alert exists
#     sos_doc = db.collection("sos_alerts").document("latest_sos").get()
#     sos_data = sos_doc.to_dict()

#     if sos_data:
#         st.markdown(f"<p class='sos-alert'>🚨 **SOS ALERT from {sos_data['patient']} at {sos_data['time']}!**</p>", 
#                     unsafe_allow_html=True)

#     # Fetch patient list
#     patients_ref = db.collection("patients").stream()
#     patient_list = [doc.id for doc in patients_ref]

#     if patient_list:
#         selected_patient = st.selectbox("Select Patient:", patient_list, help="Choose a patient to view records")
#         selected_date = st.date_input("📅 Select Date:", datetime.date.today(), help="Pick a date to view health data")
#         formatted_date = selected_date.strftime('%Y-%m-%d')

#         # Fetch selected patient's data
#         patient_data = db.collection("patients").document(selected_patient).get().to_dict()

#         if patient_data and formatted_date in patient_data:
#             st.write(f"### 🏥 Health Data for {selected_patient} on {formatted_date}:")
#             st.json(patient_data[formatted_date])
#         else:
#             st.warning("⚠ No health data found for this date.")
#     else:
#         st.info("⚠ No patient records found.")

#     st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# 🔹 Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("D:\\Glove\\newkey.json")

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
