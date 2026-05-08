import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import speech_recognition as sr
import pyttsx3

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Weather Voice Assistant",
    page_icon="🌦️",
    layout="wide"
)

# ---------------------------------------------------
# VOICE ENGINE
# ---------------------------------------------------

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------------------------------------------
# VOICE INPUT FUNCTION
# ---------------------------------------------------

def listen_city():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        st.info("🎤 Listening... Speak city name")

        audio = recognizer.listen(source)

        try:
            city_name = recognizer.recognize_google(audio)

            st.success(f"✅ Detected City: {city_name}")

            return city_name

        except:
            st.error("❌ Could not recognize voice")

            return ""

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #BBBBBB;
    font-size: 22px;
    margin-bottom: 30px;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown(
    '<div class="title">🌦️ AI Weather Voice Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-Time Weather Forecast & Smart Alerts</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

city = st.text_input(
    "📍 Enter City Name",
    placeholder="Example: Bangalore"
)

# ---------------------------------------------------
# VOICE BUTTON
# ---------------------------------------------------

if st.button("🎤 Speak City Name"):

    detected_city = listen_city()

    if detected_city:
        city = detected_city

# ---------------------------------------------------
# GET WEATHER BUTTON
# ---------------------------------------------------

if st.button("🚀 Get Weather"):

    if city == "":

        st.warning("⚠️ Please enter a city name")

    else:

        try:

            # FASTAPI URL
            url = f"http://127.0.0.1:8000/weather/{city}"

            response = requests.get(url)

            data = response.json()

            # DEBUG JSON
            st.json(data)

            # ERROR CHECK
            if "error" in data:

                st.error(data["error"])

            else:

                # ---------------------------------------------------
                # EXTRACT DATA
                # ---------------------------------------------------

                temperature = data["temperature"]
                humidity = data["humidity"]
                weather = data["weather"]
                wind_speed = data["wind_speed"]
                alerts = data["alerts"]

                # ---------------------------------------------------
                # WEATHER EMOJI
                # ---------------------------------------------------

                weather_emoji = "☀️"

                if "cloud" in weather.lower():
                    weather_emoji = "☁️"

                elif "rain" in weather.lower():
                    weather_emoji = "🌧️"

                elif "storm" in weather.lower():
                    weather_emoji = "⛈️"

                elif "snow" in weather.lower():
                    weather_emoji = "❄️"

                # ---------------------------------------------------
                # HEADER
                # ---------------------------------------------------

                st.markdown(f"# {weather_emoji} Weather in {city}")

                # ---------------------------------------------------
                # METRICS
                # ---------------------------------------------------

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "🌡️ Temperature",
                    f"{temperature} °C"
                )

                col2.metric(
                    "💧 Humidity",
                    f"{humidity}%"
                )

                col3.metric(
                    "🌪️ Wind Speed",
                    f"{wind_speed} m/s"
                )

                col4.metric(
                    "☁️ Condition",
                    weather.title()
                )

                st.divider()

                # ---------------------------------------------------
                # HUMIDITY PROGRESS BAR
                # ---------------------------------------------------

                st.subheader("💧 Humidity Level")

                st.progress(int(humidity))

                # ---------------------------------------------------
                # TEMPERATURE GAUGE
                # ---------------------------------------------------

                st.subheader("🌡️ Temperature Gauge")

                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=temperature,
                    title={'text': "Temperature °C"},
                    gauge={
                        'axis': {'range': [0, 50]},
                        'bar': {'color': "orange"},
                        'steps': [
                            {'range': [0, 20], 'color': "lightblue"},
                            {'range': [20, 35], 'color': "yellow"},
                            {'range': [35, 50], 'color': "red"}
                        ]
                    }
                ))

                st.plotly_chart(
                    fig_gauge,
                    use_container_width=True
                )

                # ---------------------------------------------------
                # WEATHER ANALYSIS CHART
                # ---------------------------------------------------

                st.subheader("📊 Weather Analysis")

                chart_data = pd.DataFrame({
                    "Metric": [
                        "Temperature",
                        "Humidity",
                        "Wind Speed"
                    ],
                    "Value": [
                        temperature,
                        humidity,
                        wind_speed
                    ]
                })

                fig = px.bar(
                    chart_data,
                    x="Metric",
                    y="Value",
                    text="Value",
                    title="Weather Metrics Visualization"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                # ---------------------------------------------------
                # AI WEATHER ASSISTANT
                # ---------------------------------------------------

                st.subheader("🤖 AI Weather Assistant")

                ai_message = ""

                if temperature > 35:

                    ai_message = (
                        "🔥 It's very hot today. Stay hydrated."
                    )

                elif humidity > 80:

                    ai_message = (
                        "💧 Humidity is high. Rain may occur."
                    )

                elif "rain" in weather.lower():

                    ai_message = (
                        "🌧️ Carry an umbrella today."
                    )

                elif wind_speed > 15:

                    ai_message = (
                        "🌪️ Strong winds detected. Be careful outside."
                    )

                else:

                    ai_message = (
                        "☀️ Weather looks pleasant today."
                    )

                st.info(ai_message)

                # SPEAK AI MESSAGE
                speak(ai_message)

                # ---------------------------------------------------
                # ALERT SECTION
                # ---------------------------------------------------

                st.subheader("⚠️ Weather Alerts")

                if len(alerts) > 0:

                    for alert in alerts:
                        st.error(alert)

                else:

                    st.success("✅ No weather alerts")

                # ---------------------------------------------------
                # RAW JSON VIEWER
                # ---------------------------------------------------

                with st.expander("🔍 View Raw JSON Data"):

                    st.json(data)

        except Exception as e:

            st.error(f"❌ Error: {e}")