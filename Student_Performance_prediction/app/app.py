import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load trained model
MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "student_performance_model.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Predict a student's final academic grade using machine learning.")

st.subheader("Enter Student Details")

with st.form("student_form"):

    age = st.slider("Age", 15, 22, 17)
    Medu = st.selectbox("Mother's Education", [0, 1, 2, 3, 4])
    Fedu = st.selectbox("Father's Education", [0, 1, 2, 3, 4])
    traveltime = st.selectbox("Travel Time", [1, 2, 3, 4])
    studytime = st.selectbox("Weekly Study Time", [1, 2, 3, 4])
    failures = st.selectbox("Past Class Failures", [0, 1, 2, 3])
    famrel = st.slider("Family Relationship Quality", 1, 5, 4)
    freetime = st.slider("Free Time", 1, 5, 3)
    goout = st.slider("Going Out", 1, 5, 3)
    Dalc = st.slider("Workday Alcohol Consumption", 1, 5, 1)
    Walc = st.slider("Weekend Alcohol Consumption", 1, 5, 1)
    health = st.slider("Health", 1, 5, 3)
    absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=0)
    G1 = st.slider("First Period Grade", 0, 20, 10)
    G2 = st.slider("Second Period Grade", 0, 20, 10)

    st.subheader("Additional Student Information")

    school = st.selectbox("School", ["GP", "MS"])
    sex = st.selectbox("Sex", ["F", "M"])
    address = st.selectbox("Home Address", ["U", "R"])
    famsize = st.selectbox("Family Size", ["GT3", "LE3"])
    Pstatus = st.selectbox("Parent Status", ["T", "A"])

    Mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
    Fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])

    reason = st.selectbox("Reason for Choosing School",
                          ["home", "reputation", "course", "other"])

    guardian = st.selectbox("Guardian", ["mother", "father", "other"])

    schoolsup = st.selectbox("Extra Educational Support", ["yes", "no"])
    famsup = st.selectbox("Family Educational Support", ["yes", "no"])
    paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
    activities = st.selectbox("Extra-curricular Activities", ["yes", "no"])
    nursery = st.selectbox("Attended Nursery School", ["yes", "no"])
    higher = st.selectbox("Wants Higher Education", ["yes", "no"])
    internet = st.selectbox("Internet Access", ["yes", "no"])
    romantic = st.selectbox("In a Romantic Relationship", ["yes", "no"])

    submitted = st.form_submit_button("Predict Student Performance")

if submitted:

    input_data = {
        "age": age,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2,
        "school_MS": int(school == "MS"),
        "sex_M": int(sex == "M"),
        "address_U": int(address == "U"),
        "famsize_LE3": int(famsize == "LE3"),
        "Pstatus_T": int(Pstatus == "T"),
        "Mjob_health": int(Mjob == "health"),
        "Mjob_other": int(Mjob == "other"),
        "Mjob_services": int(Mjob == "services"),
        "Mjob_teacher": int(Mjob == "teacher"),
        "Fjob_health": int(Fjob == "health"),
        "Fjob_other": int(Fjob == "other"),
        "Fjob_services": int(Fjob == "services"),
        "Fjob_teacher": int(Fjob == "teacher"),
        "reason_home": int(reason == "home"),
        "reason_other": int(reason == "other"),
        "reason_reputation": int(reason == "reputation"),
        "guardian_mother": int(guardian == "mother"),
        "guardian_other": int(guardian == "other"),
        "schoolsup_yes": int(schoolsup == "yes"),
        "famsup_yes": int(famsup == "yes"),
        "paid_yes": int(paid == "yes"),
        "activities_yes": int(activities == "yes"),
        "nursery_yes": int(nursery == "yes"),
        "higher_yes": int(higher == "yes"),
        "internet_yes": int(internet == "yes"),
        "romantic_yes": int(romantic == "yes")
    }

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success("Prediction Completed!")
    st.metric("Predicted Final Grade", f"{prediction:.2f} / 20")

    if prediction >= 15:
        st.write("🌟 Excellent Performance")
    elif prediction >= 12:
        st.write("👍 Good Performance")
    elif prediction >= 10:
        st.write("📘 Average Performance")
    else:
        st.write("⚠️ Needs Improvement")
        
    