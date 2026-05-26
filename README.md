AI/ML-Based Predictive Maintenance System

An AI/ML-based Predictive Maintenance System developed for industrial refinery equipment such as pumps, motors, compressors, and turbines. The system monitors industrial sensor parameters and predicts machine failure risk using Machine Learning and industrial safety threshold analysis.

Features
Real-time machine health monitoring
Failure risk prediction
Interactive dashboard
Industrial alert system
Sensor anomaly detection
Graphical visualization
Machine shutdown detection
Risk percentage analysis
Technologies Used
Python
Streamlit
Scikit-learn
Pandas
NumPy
Matplotlib
Joblib
Machine Learning Algorithm
Random Forest Classifier

Used for:

Predictive analysis
Failure detection
Risk classification
Dataset Used

Azure Predictive Maintenance Dataset

Parameters used:

Temperature
Pressure
RPM
Vibration
Historical Failure Data
Equipment Monitored
Pumps
Motors
Compressors
Turbines
Project Structure
AI-ML-based-Predictive-Maintaince-System/
│
├── app.py
├── trained_model.py
├── requirements.txt
├── dataset/
├── model/
├── .gitignore
└── README.md
Installation
Clone Repository
git clone https://github.com/nikitab09/AI-ML-based-Predictive-Maintaince-System.git
Install Dependencies
pip install -r requirements.txt
Run the Application
streamlit run app.py
Dashboard Features
Live sensor monitoring
Risk score prediction
Machine health analysis
Alert notifications
Industrial graphs
Equipment status display
Risk Categories
Risk Score	Status
0–29	Healthy
30–59	Medium Risk
60+	High Failure Risk
Industrial Parameters
Parameter	Purpose
Temperature	Detect overheating
Pressure	Detect leakage/blockage
RPM	Detect mechanical stress
Vibration	Detect bearing faults
Future Enhancements
IoT sensor integration
Cloud deployment
Real-time analytics
Deep learning integration
Email/SMS alerts
Applications
Oil Refineries
Smart Manufacturing
Industrial Automation
Predictive Maintenance
Machine Health Monitoring
