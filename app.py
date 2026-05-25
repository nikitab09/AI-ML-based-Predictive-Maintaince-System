import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib


# PAGE CONFIG

st.set_page_config(
    page_title="IOCL Predictive Maintenance",
    layout="wide"
)


# LOAD DATASET

data = pd.read_csv("dataset/PdM_telemetry.csv")

# Create temperature column
data['temperature'] = data['volt'] * 0.5


# LOAD TRAINED MODEL

model = joblib.load("model.pkl")


# TITLE

st.title("🏭 IOCL Predictive Maintenance System")

st.subheader("AI/ML Based Refinery Equipment Monitoring Dashboard")


# SIDEBAR INPUTS

st.sidebar.header("Machine Parameters")

temperature = st.sidebar.slider(
    "Temperature",
    0,
    100,
    50
)

pressure = st.sidebar.slider(
    "Pressure",
    0,
    200,
    100
)

rpm = st.sidebar.slider(
    "RPM",
    0,
    5000,
    2000
)

vibration = st.sidebar.slider(
    "Vibration",
    0.0,
    5.0,
    1.0
)

# MACHINE SELECTION

machine = st.sidebar.selectbox(
    "Select Machine",
    [
        "Pump-101",
        "Compressor-202",
        "Turbine-303",
        "Motor-404"
    ]
)


# SENSOR FAILURE PREDICTION

input_data = np.array([
    [
        temperature,
        pressure,
        rpm,
        vibration
    ]
])

# -----------------------------
# INITIAL RISK SCORE
# -----------------------------

risk_score = 0

# -----------------------------
# MACHINE STOP CHECK
# -----------------------------

if rpm == 0:

    st.error("❌ Machine Stopped")

    risk_score = 100

# -----------------------------
# SENSOR FAILURE CHECK
# -----------------------------

elif temperature == 0 or pressure == 0:

    st.warning("⚠️ Sensor Failure Possible")

    risk_score = 40

# -----------------------------
# NORMAL RISK ANALYSIS
# -----------------------------

else:

    # Temperature Risk
    if temperature < 30:
        risk_score += 20
        st.warning("⚠️ Temperature Too Low")

    elif temperature > 85:
        risk_score += 40
        st.error("❌ Temperature Too High")

    elif temperature > 70:
        risk_score += 20

    # Pressure Risk
    if pressure < 80:
        risk_score += 20
        st.warning("⚠️ Pressure Too Low")

    elif pressure > 180:
        risk_score += 30
        st.error("❌ Pressure Too High")

    elif pressure > 150:
        risk_score += 15

    # RPM Risk
    if rpm < 1000:
        risk_score += 20
        st.warning("⚠️ RPM Too Low")

    elif rpm > 4500:
        risk_score += 20
        st.error("❌ RPM Too High")

    elif rpm > 3500:
        risk_score += 10

    # Vibration Risk
    if vibration < 0.2:
        risk_score += 15
        st.warning("⚠️ Vibration Too Low")

    elif vibration > 3.5:
        risk_score += 30
        st.error("❌ Dangerous Vibration")

    elif vibration > 2:
        risk_score += 15

# HEALTH STATUS

st.subheader("Machine Health")

if risk_score < 30:
    st.success("✅ Machine Healthy")

elif risk_score < 60:
    st.warning("⚠️ Medium Risk")

else:
    st.error("❌ High Failure Risk")        

# DASHBOARD METRICS

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Machine",
        machine
    )

with col2:
    st.metric(
        "Failure Risk",
        f"{risk_score:.2f}%"
    )

with col3:
    if risk_score < 30:
        st.metric(
            "Status",
            "Healthy"
        )

    elif risk_score < 60:
        st.metric(
            "Status",
            "Warning"
        )

    else:
        st.metric(
            "Status",
            "Critical"
        )


# ALERT SECTION

st.subheader("⚠️ Alerts")

if vibration > 3:
    st.error("High Vibration Detected")

if pressure > 170:
    st.warning("Pressure Above Safe Limit")

if temperature > 80:
    st.warning("Temperature Increasing Rapidly")

if risk_score > 60:
    st.error("High Failure Risk Detected")



# SENSOR VALUES

st.subheader("Live Sensor Readings")

sensor_col1, sensor_col2 = st.columns(2)

with sensor_col1:
    st.write(f"Temperature : {temperature} °C")
    st.write(f"Pressure : {pressure} PSI")

with sensor_col2:
    st.write(f"RPM : {rpm}")
    st.write(f"Vibration : {vibration}")


# PRESSURE GRAPH

st.subheader("Pressure Trend")

fig1, ax1 = plt.subplots()

ax1.plot(data['pressure'][:100])

ax1.set_xlabel("Time")

ax1.set_ylabel("Pressure")

st.pyplot(fig1)


# RPM GRAPH

st.subheader("RPM Trend")

fig2, ax2 = plt.subplots()

ax2.plot(data['rotate'][:100])

ax2.set_xlabel("Time")

ax2.set_ylabel("RPM")

st.pyplot(fig2)


# VIBRATION GRAPH

st.subheader("Vibration Analysis")

fig3, ax3 = plt.subplots()

ax3.plot(data['vibration'][:100])

ax3.set_xlabel("Time")

ax3.set_ylabel("Vibration")

st.pyplot(fig3)


# TEMPERATURE GRAPH

st.subheader("Temperature Trend")

fig4, ax4 = plt.subplots()

ax4.plot(data['temperature'][:100])

ax4.set_xlabel("Time")

ax4.set_ylabel("Temperature")

st.pyplot(fig4)


# MACHINE DATA TABLE

st.subheader("Machine Telemetry Data")

st.dataframe(data.head(20))


# FINAL SUMMARY

st.subheader("System Summary")

st.write("""
This AI/ML predictive maintenance system monitors refinery equipment
using sensor parameters such as temperature, pressure, RPM,
and vibration.

The Random Forest Machine Learning model predicts the
probability of machine failure and generates alerts for
preventive maintenance.
""")