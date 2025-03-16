import streamlit as st
from datetime import date
import pandas as pd
import random

# Sample user data (replace with actual data retrieval logic)
user_data = {
    "username": "Ram Kumar",
    "progress": 70,  # Percentage completion
    "level": 3,
    "badges": ["Starter", "Consistency", "Halfway There"],
}

# Sample leaderboard data
leaderboard = pd.DataFrame({
    "Username": ["Anne", "Boss", "Ram Kumar", "Eva"],
    "Level": [5, 4, 3, 2],
    "Progress": [90, 80, 70, 60]
}).sort_values(by="Progress", ascending=False)

# Ensure that the patients' data persists across page refreshes
if "patients" not in st.session_state:
    st.session_state.patients = {"Ram Kumar": {}}  # Initialize with an empty dictionary for 'Ram Kumar'

# Doctor Details
doctors = {
    "dr.Haran": {"name": "Dr. Haran", "specialization": "Cardiology"}
}

# Streamlit App Title
st.set_page_config(page_title="Doctor-Patient Interface", layout="wide")
st.title("🏥 Doctor-Patient Interface")

menu = ["Home", "Patient Data", "Doctor Details", "Gamified Rehab Dashboard"]
choice = st.sidebar.radio("📌 Menu", menu)

# ============================
# Home Page
# ============================
if choice == "Home":
    st.markdown("""
        ### Welcome to the **Doctor-Patient Interface** 👨‍⚕️👩‍⚕️
        This platform allows doctors to monitor and update patient health records.
    """)

    game_choice = st.selectbox("Choose a Game", ["Select a Game", "Number Guessing Game", "Trivia Quiz"])

    if game_choice == "Number Guessing Game":
        st.subheader("🎮 Number Guessing Game")
        st.write("Guess the number between 1 and 100!")
        
        # Initialize session state for the game
        if "number" not in st.session_state:
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
        
        guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
        
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.number:
                st.write("Too low! Try again.")
            elif guess > st.session_state.number:
                st.write("Too high! Try again.")
            else:
                st.write(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.attempts} attempts.")
                # Reset the game after winning
                if st.button("Play Again"):
                    st.session_state.number = random.randint(1, 100)
                    st.session_state.attempts = 0

    elif game_choice == "Trivia Quiz":
        st.subheader("🧠 Trivia Quiz")
        st.write("Answer the health-related questions below!")

        # Question and answers
        question = "What is the normal human body temperature?"
        options = ["36.1°C", "37°C", "38.5°C", "39°C"]

        answer = st.radio(question, options)

        if st.button("Submit Answer"):
            if answer == "37°C":
                st.write("Correct! The normal body temperature is 37°C.")
            else:
                st.write("Incorrect! The correct answer is 37°C.")

    # Create layout for SOS button (Positioning it in the top-right corner)
    sos_button_container = st.empty()

    with sos_button_container.container():
        # This will add an SOS button in the top-right corner
        sos_button = st.button("SOS", key="sos_button")

    # Check if the SOS button is pressed
    if sos_button:
        st.write("SOS Button Pressed!")


# ============================
# Patient Data Page
# ============================
elif choice == "Patient Data":
    st.subheader("📋 Patient Data")

    # Patient info (Only one patient named 'Ram Kumar')
    patient_id = "Ram Kumar"
    st.write("Patient Name: Ram Kumar")
    # Patient selects the date for which they want to update the data
    date_input = st.date_input("Select Date", value=date.today())
    
    # Retrieve existing data for the selected date (if any)
    patient_data = st.session_state.patients[patient_id].get(str(date_input), {})

    # Create columns for BP, Pulse, and Heartbeat
    col1, col2, col3 = st.columns(3)
    
    with col1:
        bp = st.text_input("🩸 Blood Pressure", patient_data.get("bp", ""))

    with col2:
        pulse = st.text_input("💓 Pulse", patient_data.get("pulse", ""))

    with col3:
        heartbeat = st.text_input("❤️ Heartbeat", patient_data.get("heartbeat", ""))
    
    # Button to update the data
    if st.button("Update Patient Data"):
        if bp and pulse and heartbeat:
            # Update or add data for the selected date
            st.session_state.patients[patient_id][str(date_input)] = {"bp": bp, "pulse": pulse, "heartbeat": heartbeat}
            st.success(f"Patient data updated for {date_input}!")
        else:
            st.error("Please fill in all fields!")

# ============================
# Doctor Details Page
# ============================
elif choice == "Doctor Details":
    st.subheader("🩺 Doctor Details")

    # Doctor info (Only one doctor 'Dr. Haran')
    doctor_id = "dr.Haran"
    
    # Show selected doctor's details
    st.write(f"{doctors[doctor_id]['name']} - {doctors[doctor_id]['specialization']}")
    
    # Doctor selects the patient (Only one patient 'Ram Kumar')
    patient_id = st.selectbox("Select Patient", ["Ram Kumar"])  # Even though there's only one patient
    
    if patient_id:
        # Get all available dates for the selected patient
        available_dates = list(st.session_state.patients[patient_id].keys())
        
        if available_dates:
            # Doctor selects the date to view the patient's data
            date_input = st.date_input("Select Date", value=available_dates[0], min_value=min(available_dates), max_value=date.today())
            
            # Retrieve and display patient data for the selected date
            patient_data = st.session_state.patients[patient_id].get(str(date_input), {})
            
            if patient_data:
                st.write(f"Patient Data for {date_input}:")
                st.write(f"Blood Pressure: {patient_data.get('bp', 'N/A')}")
                st.write(f"Pulse: {patient_data.get('pulse', 'N/A')}")
                st.write(f"Heartbeat: {patient_data.get('heartbeat', 'N/A')}")
            else:
                st.write("No data available for this date.")
        else:
            st.write("No data available for the selected patient.")

# ============================
# Gamified Rehab Dashboard Page
# ============================
elif choice == "Gamified Rehab Dashboard":
    st.title("🏆 Gamified Rehab Dashboard")
    st.subheader(f"Welcome, {user_data['username']}!")

    # Progress Bar
    st.write("### Your Progress")
    st.progress(user_data["progress"] / 100)
    st.write(f"You have completed {user_data['progress']}% of your rehabilitation goals.")

    # Current Level
    st.write("### Your Level")
    st.write(f"🎮 Level {user_data['level']}")

    # Achievements / Badges
    st.write("### Your Badges")
    st.write(", ".join([f"🏅 {badge}" for badge in user_data["badges"]]))

    # Leaderboard
    st.write("### Leaderboard")
    st.dataframe(leaderboard, hide_index=True)

    # Simulation: Earn Random Progress
    if st.button("Complete a session ✅"):
        new_progress = min(100, user_data["progress"] + random.randint(5, 15))
        user_data["progress"] = new_progress
        if new_progress >= 100:
            user_data["badges"].append("Champion")
        st.rerun()

    st.write("Keep going! You're making great progress! 💪")
