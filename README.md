🌦️ AI-Powered Weather Forecast & Alert System 🚀

A next-generation real-time Weather Intelligence Platform built using Python, FastAPI, Streamlit, Plotly, and OpenWeather API with AI-style voice assistance, smart alerts, and interactive analytics.

🌍 Overview

The AI-Powered Weather Forecast & Alert System is an advanced real-time weather monitoring application designed to simulate an industry-grade weather intelligence platform used by logistics companies, agriculture sectors, travelers, event planners, and public safety systems.

This project combines:

🌦️ Live weather forecasting
🤖 AI-generated weather insights
🎤 Voice assistant interaction
⚠️ Smart alert generation
📊 Interactive visual analytics
☁️ Real-time API integration
🔥 Automation-driven weather monitoring

The application provides a complete full-stack architecture using:

FastAPI as backend API service
Streamlit as interactive frontend dashboard
OpenWeather API for real-time weather data
Plotly for professional data visualization
Speech Recognition + Text-to-Speech for AI voice interaction
✨ Core Features
🌡️ Real-Time Weather Monitoring
Live weather data fetching
Real-time temperature monitoring
Humidity tracking
Wind speed analysis
Weather condition updates
🤖 AI Weather Assistant

The system intelligently analyzes weather conditions and generates AI-style recommendations such as:

☀️ Weather looks pleasant today.
🌧️ Carry an umbrella today.
🔥 Stay hydrated in high temperatures.
🌪️ Strong winds detected.

The assistant behaves like a lightweight weather AI companion.

🎤 Voice Assistant Integration

Users can:

Speak city names using microphone input
Receive spoken weather insights
Interact hands-free with the dashboard

This feature is powered using:

SpeechRecognition
pyttsx3
📊 Interactive Dashboard Analytics

The dashboard includes:

📈 Interactive Plotly charts
🌡️ Temperature gauge meter
💧 Humidity progress indicators
📊 Dynamic weather metric visualization
⚠️ Alert cards
🔍 Expandable JSON weather viewer
⚠️ Smart Weather Alert System

The alert engine automatically detects:

High temperature conditions
Rain probability
High humidity
Strong wind conditions

Alerts are displayed in real-time through the dashboard.

Screenshot
<img width="960" height="540" alt="output1" src="https://github.com/user-attachments/assets/51481d30-760b-4f26-933b-afc9ec396863" />
<img width="960" height="540" alt="output2" src="https://github.com/user-attachments/assets/5a4da5a1-e5d9-46e7-ad44-5684ec4b5006" />
<img width="960" height="540" alt="output3" src="https://github.com/user-attachments/assets/828a2f7a-afa3-48fe-ade7-19691f7f9fd2" />
<img width="960" height="540" alt="output4" src="https://github.com/user-attachments/assets/048c45bb-f16e-4bb0-8cb0-f7ca5733663f" />
<img width="960" height="540" alt="output5" src="https://github.com/user-attachments/assets/95f27a7f-9ddb-4786-9f74-04fd07d3043c" />

🏗️ System Architecture
User
   ↓
Streamlit Interactive Dashboard
   ↓
FastAPI Backend Service
   ↓
OpenWeather API
   ↓
Real-Time Weather Data
   ↓
AI Alert Engine
   ↓
Voice Assistant + Analytics Dashboard
🛠️ Technology Stack
Technology	Purpose
Python	Core Programming
FastAPI	Backend API Development
Streamlit	Frontend Dashboard
OpenWeather API	Live Weather Data
Plotly	Interactive Visualizations
Pandas	Data Processing
Requests	API Communication
SpeechRecognition	Voice Input
pyttsx3	Text-to-Speech
📂 Project Structure
AI-Weather-Forecast-Alert-System/
│
├── images/
├── outputs/
├── reports/
├── venv/
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/AI-Weather-Forecast-Alert-System.git
2️⃣ Open Project Directory
cd AI-Weather-Forecast-Alert-System
3️⃣ Create Virtual Environment
Windows
python -m venv venv

Activate:

venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
🔑 API Setup

Create .env

API_KEY=your_openweather_api_key

Get free API key from:

OpenWeather API

▶️ Running the Project
Terminal 1 — FastAPI Backend
uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger API Docs:

http://127.0.0.1:8000/docs
Terminal 2 — Streamlit Dashboard
streamlit run app.py

Dashboard URL:

http://localhost:8501
🎤 Voice Assistant Usage
Click:
🎤 Speak City Name
Speak city name:
Bangalore
AI assistant:
detects city
fetches weather
speaks weather insights
📊 Dashboard Highlights

✅ Real-Time Weather Metrics
✅ Interactive Plotly Charts
✅ Temperature Gauge Meter
✅ Humidity Progress Bar
✅ Smart Alert Engine
✅ AI Weather Recommendations
✅ Voice Assistant Integration
✅ JSON Data Viewer
✅ Professional Dark UI

👩‍💻 Author
Arpita Bhendigeri

Focused on:

AI Projects
Python Development
Automation Systems
Dashboard Engineering
Real-Time Applications
