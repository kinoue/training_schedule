import streamlit as st
from coach import marathon_training_schedule

event_distance = {
    'Marathon': 42.195,
    'Halfmarathon': 21.098,
    '10K': 10,
    '5K': 5
}

# event_type = st.selectbox('Event Type', event_distance.keys())

# st.write('Distance: {}km'.format(event_distance[event_type]))


import streamlit as st

# Simplified function for marathon training schedule

st.title("Marathon Training Schedule Generator")

st.header("Training Parameters")
target_marathon_time = st.number_input("Target Marathon Time (in minutes)", min_value=120, max_value=600, value=240)
training_weeks = st.number_input("Weeks to Train", min_value=4, max_value=52, value=16)
unit = st.radio("Select Distance Unit", ('km', 'miles'))
unit_singular = 'km' if unit == 'km' else 'mile'

# Button to generate schedule
if st.button('Generate Training Schedule'):
    training_schedule = marathon_training_schedule(target_marathon_time, training_weeks, unit)
    for week, schedule in enumerate(training_schedule, 1):
        st.subheader(f"Week {week}")
        for workout_type, (distance, pace) in schedule.items():
            st.write(f"{workout_type}: {distance:.2f} {unit} at {pace:.2f} min/{unit_singular}")
else:
    st.write("Enter your training parameters and press 'Generate Training Schedule'.")
