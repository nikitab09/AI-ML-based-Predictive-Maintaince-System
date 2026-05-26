# AI/ML-Based Predictive Maintenance System for Refinery Equipment

## Overview

This project is an AI/ML-based Predictive Maintenance System developed for industrial refinery equipment such as pumps, motors, compressors, and turbines.

The system monitors important industrial parameters including:

- Temperature
- Pressure
- RPM
- Vibration

to predict machine failure risks and improve maintenance efficiency.

The project combines Machine Learning techniques with industrial safety threshold analysis to provide:

- Real-time monitoring
- Anomaly detection
- Failure risk prediction
- Interactive dashboard visualization

---

# Features

- Real-time machine health monitoring
- Failure risk prediction using Machine Learning
- Interactive industrial dashboard
- Sensor anomaly detection
- Machine shutdown detection
- Risk categorization
- Industrial alert system
- Graph and visualization support
- Equipment-wise monitoring

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Frontend dashboard development |
| Scikit-learn | Machine learning implementation |
| Pandas | Data processing and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Joblib | Model saving and loading |

---

# Machine Learning Model

The project uses the **Random Forest Classifier** algorithm from Scikit-learn for predictive maintenance analysis and machine failure prediction.

---

# Dataset Used

## Azure Predictive Maintenance Dataset

Parameters used in the project:

- Temperature
- Pressure
- RPM
- Vibration
- Historical Failure Data

---

# Equipment Monitored

- Pumps
- Motors
- Compressors
- Turbines

---

# Project Structure

```bash
AI-ML-based-Predictive-Maintaince-System/
│
├── app.py
├── trained_model.py
├── requirements.txt
├── dataset/
├── model/
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/nikitab09/AI-ML-based-Predictive-Maintaince-System.git
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Dashboard Functionalities

- Live sensor value monitoring
- Risk score prediction
- Equipment health analysis
- Warning and critical alerts
- Industrial graphs and charts
- Machine status display

---

# Risk Categories

| Risk Score | Status |
|------------|---------|
| 0–29 | Healthy |
| 30–59 | Medium Risk |
| 60+ | High Failure Risk |

---

# Industrial Parameters Used

| Parameter | Purpose |
|------------|---------|
| Temperature | Detect overheating |
| Pressure | Detect leakage or blockage |
| RPM | Detect mechanical stress |
| Vibration | Detect imbalance and bearing faults |

---

# Future Enhancements

- IoT sensor integration
- Cloud deployment
- Real-time analytics
- Deep learning integration
- Automated maintenance scheduling
- Email/SMS alert system

---

# Applications

- Oil Refineries
- Smart Manufacturing
- Industrial Automation
- Predictive Maintenance Systems
- Machine Health Monitoring

---

# Objective

The main objective of this project is to reduce unexpected equipment failures, improve operational safety, minimize maintenance costs, and support predictive maintenance strategies using Artificial Intelligence and Machine Learning techniques.

---

# Author

**Nikita Borgohain**

---

# License

This project is developed for educational and internship purposes.
