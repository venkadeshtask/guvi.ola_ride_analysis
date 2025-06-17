
import streamlit as st
import altair as alt
import pandas as pd

# Load data
df = pd.read_csv("ola.csv")

st.set_page_config(page_title="OLA Ride Booking Analysis", layout="wide")

st.title("OLA Ride Booking Analysis")

# Display Raw Data
st.header("Raw Data")
st.dataframe(df)

# Booking Status Distribution
st.header("Booking Status Distribution")
booking_status_counts = df['Booking_Status'].value_counts().reset_index()
booking_status_counts.columns = ['Booking_Status', 'Count']
chart1 = alt.Chart(booking_status_counts).mark_bar().encode(
    x=alt.X('Booking_Status', sort='-y'),
    y='Count',
    tooltip=['Booking_Status', 'Count']
).properties(
    title='Distribution of Booking Status'
)
st.altair_chart(chart1, use_container_width=True)

# Vehicle Type Distribution
st.header("Vehicle Type Distribution")
vehicle_type_counts = df['Vehicle_Type'].value_counts().reset_index()
vehicle_type_counts.columns = ['Vehicle_Type', 'Count']
chart2 = alt.Chart(vehicle_type_counts).mark_bar().encode(
    x=alt.X('Vehicle_Type', sort='-y'),
    y='Count',
    tooltip=['Vehicle_Type', 'Count']
).properties(
    title='Distribution of Vehicle Types'
)
st.altair_chart(chart2, use_container_width=True)

# Average Booking Value and Ride Distance by Vehicle Type
st.header("Average Booking Value and Ride Distance by Vehicle Type")
avg_metrics_by_vehicle = df.groupby('Vehicle_Type').agg(
    Avg_Booking_Value=('Booking_Value', 'mean'),
    Avg_Ride_Distance=('Ride_Distance', 'mean')
).reset_index()

chart3 = alt.Chart(avg_metrics_by_vehicle).mark_bar().encode(
    x=alt.X('Vehicle_Type', sort='-y'),
    y='Avg_Booking_Value',
    tooltip=['Vehicle_Type', 'Avg_Booking_Value']
).properties(
    title='Average Booking Value by Vehicle Type'
)
st.altair_chart(chart3, use_container_width=True)

chart4 = alt.Chart(avg_metrics_by_vehicle).mark_bar().encode(
    x=alt.X('Vehicle_Type', sort='-y'),
    y='Avg_Ride_Distance',
    tooltip=['Vehicle_Type', 'Avg_Ride_Distance']
).properties(
    title='Average Ride Distance by Vehicle Type'
)
st.altair_chart(chart4, use_container_width=True)
