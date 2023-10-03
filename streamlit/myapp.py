import streamlit as st
import pandas as pd
import requests

st.title("Car evaluation web application")
st.write("""
# My first app
Hello *world!*        
""")

buying = st.radio(
    "what are your thoughts on the car's buying price?",
    ("vhigh", "high", "med", "low")
)

maint = st.radio(
    "What are your thoughts on the price of maintenance for the car?",
    ("vhigh", "high", "med", "low")
)

doors = st.select_slider(
    "How many doors does the car have?",
    options=["2", "3", "4", "5more"]
)

persons = st.select_slider(
    "How many passengers can the car carry?",
    options=["2", "4", "more"]
)

lug_boot = st.select_slider(
    "What is the size of the luggage boot?",
    options=["small", "med", "big"]
)

safety = st.select_slider(
    "What estimated level of safety does the car provide?",
    options=["low", "med", "high"]
)

class_values = {
    0: "unacceptable",
    1: "aceptable",
    2: "good",
    3: "very good"
}

if st.button("Submit"):
    inputs = {
        "inputs": [
            {
                "buying": buying,
                "maint": maint,
                "doors": doors,
                "persons": persons,
                "lug_boot": lug_boot,
                "safety": safety
            }
        ]
    }

    response = requests.post(
        f"http://host.docker.internal:8001/api/v1/predict/", json=inputs, verify=False)
    json_response = response.json()

    prediction = class_values[json_response.get("predictions")[0]]

    st.subheader(f"This car is **{prediction}!**")
