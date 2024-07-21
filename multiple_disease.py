import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from tensorflow.keras.models import load_model
import pandas as pd
import requests

from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

import numpy as np

from util import classify, set_background
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# loading the models

diabetes = pickle.load(open("models/diabetes_model.sav", "rb"))

heart_disease = pickle.load(open("models/heart_disease_model.sav", "rb"))

parkinsons_disease = pickle.load(
    open("models/parkinsons_disease_model.sav", "rb"))

breast_cancer = pickle.load(open("models/breast_cancer_model.sav", "rb"))

lung_cancer = pickle.load(open("models/lung_cancer_model.sav", "rb"))


# sidebar for navigation

with st.sidebar:

    selected = option_menu("MULTIPLE DISEASE PREDICTION SYSTEM",

                           ["Home", "Diabetes Prediction",
                            "Heart Disese Prediction",
                            "Parkinsons Disease Prediction",
                            "Breast Cancer Prediction",
                            "Lung Cancer Prediction", "Pneumonia"],

                           icons=["activity", "heart-fill", "people-fill",
                                  "gender-female", "apple"],

                           default_index=0)


# Home prediction page


if (selected == "Home"):

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Use local CSS

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    # ---- LOAD ASSETS ----
    lottie_coding1 = load_lottieurl(
        "https://lottie.host/a38af4d1-1332-40a3-9e4e-b5509f1ebe9f/2fmF8mUk8h.json")
    lottie_coding2 = load_lottieurl(
        "https://lottie.host/70d5834d-7a4d-49b8-a915-fb9fcd34b348/qv9UV8l4AG.json")
    lottie_coding3 = load_lottieurl(
        "https://lottie.host/03683837-643d-47c4-b986-0082ba1a89dc/n94ZX5C7xV.json")

    img_contact_form = Image.open("images/yt_contact_form.png")
    img_lottie_animation = Image.open("images/yt_lottie_animation.png")

    # ---- HEADER SECTION ----
    import streamlit as st

    st.markdown("""
        <div style='text-align: center; font-family: "Times New Roman",  Times, serif;'>
            <h1>MED PREDICT</h1>
            <p>YOUR PERSONAL MULTI-DISEASE DETECTION BUDDY.</p>
        </div>
    """, unsafe_allow_html=True)

    # ---- WHAT I DO ----
    st.write("---")

    with st.container():
        left_column, right_column = st.columns(2)

        with left_column:
            st.markdown("""
                <div style='text-align: center; font-family: "Courier New", Courier, monospace;'>
                    <h1 style='font-family: "Times New Roman", Times, serif;'>ABOUT US 🌐</h1>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(
                """
                  <div style='font-size: 30px;'>
                
                At Check-Com, we are passionate about leveraging the power of artificial intelligence to revolutionize healthcare. Our mission is to make disease detection more accessible, accurate, and proactive.
                Through cutting-edge machine learning algorithms, we aim to provide users with reliable predictions for a range of health conditions, including diabetes, heart disease, Parkinson's disease, breast cancer, lung cancer, and pneumonia. We prioritize user-friendly interfaces, ensuring that individuals can easily interact with our platform to receive valuable health insights
                Choose Check-Com for accurate predictions and personalized health guidance.
                </div>
                
                

                """, unsafe_allow_html=True
            )

        with right_column:
            st.lottie(lottie_coding1, height=300, key="coding")

    # ---- PROJECTS ----
    st.write("---")

    with st.container():
        left_column, right_column = st.columns(2)

        with right_column:
            st.markdown("""
                <div>
                    <h1 style='font-family: "Times New Roman", Times, serif;'>WHAT WE DO? 🤔</h1>
                </div>
            """, unsafe_allow_html=True)
            st.write(
                """
                - **Accessibility:** Models can be accessed remotely, providing quick initial assessments without physical presence.
                - **Efficiency:** Automated models can process vast amounts of data rapidly, potentially leading to quicker results than manual examinations.
                - **Affordability:** Using a model might be more cost-effective for initial screenings compared to in-person consultations.
                - **Availability:** Particularly in regions with limited access to healthcare, models can offer an initial assessment when a doctor may not be readily available.
                """

            )
            with left_column:
                st.lottie(lottie_coding2, height=300, key="coding1")

    # ---- CONTACT ----
    with st.container():

        st.write("---")
        st.header("GET IN TOUCH WITH US 😊")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.lottie(lottie_coding3, height=300, key="coding2")

            # ---- MAP ----

    # Assuming you already have lottie_coding loaded
# Assuming you already have lottie_coding loaded

    with st.container():
        st.write("---")
        st.header("OUR LOCATION ON MAP 🗺️")

        # Create a DataFrame with latitude and longitude
        location_df = pd.DataFrame({'lat': [12.956467], 'lon': [77.545472]})

        st.markdown(
            '<style>div.row-widget.stHorizontal {flex-direction: row;}</style>', unsafe_allow_html=True)
        st.markdown(
            '<style>div[data-baseweb="drawer-container"] {padding-top: 0;}</style>', unsafe_allow_html=True)

        # Create a three-column layout
        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.markdown(f'<iframe width="1150" height="600" src="https://maps.google.com/maps?q=12.956467,77.545472&z=15&output=embed" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

        with col2:
            st.write("")  # An empty space


# Diabetes Prediction Page

if (selected == "Diabetes Prediction"):

    # page title
    st.title("Diabetes Prediction using Machine Learning")
    set_background('./bgs/sthe.jpg', size="fill")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            "Diabetes Pedigree Function Value")

    with col2:
        Age = st.text_input("Age of the Person")


# code for Prediction
    diabetes_diagnosis = " "

    # creating a button for Prediction

    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diabetes_prediction[0] == 0):
            diabetes_diagnosis = "Hurrah! You have no Diabetes."
        else:
            diabetes_diagnosis = "Sorry! You have Diabetes."

    st.success(diabetes_diagnosis)


# Heart Disease Prediction Page:

if (selected == "Heart Disese Prediction"):

    # page title
    st.title("Heart Disease Prediction using Machine Learning")
    set_background('./bgs/sthe.jpg', size="fill")


# getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")

    with col2:
        sex = st.number_input("Sex")

    with col3:
        cp = st.number_input("Chest Pain Types")

    with col1:
        trestbps = st.number_input("Resting Blood Pressure")

    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.number_input("Resting Electrocardiographic Results")

    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.number_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.number_input("ST Depression induced by Exercise")

    with col2:
        slope = st.number_input("Slope of the peak exercise ST Segment")

    with col3:
        ca = st.number_input("Major vessels colored by Flourosopy")

    with col1:
        thal = st.number_input(
            "thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    # code for Prediction
    heart_diagnosis = " "

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 0):
            heart_diagnosis = "Hurrah! Your Heart is Good."
        else:
            heart_diagnosis = "Sorry! You have Heart Problem."

    st.success(heart_diagnosis)


# Parkinsons Disease Prediction Page:

if (selected == "Parkinsons Disease Prediction"):

    # page title
    st.title("Parkinsons Disease Prediction using Machine Learning")
    set_background('./bgs/sthe.jpg', size="fit")


# getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        RAP = st.text_input("MDVP:RAP")

    with col2:
        PPQ = st.text_input("MDVP:PPQ")

    with col3:
        DDP = st.text_input("Jitter:DDP")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col3:
        APQ = st.text_input("MDVP:APQ")

    with col4:
        DDA = st.text_input("Shimmer:DDA")

    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col4:
        spread1 = st.text_input("spread1")

    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        D2 = st.text_input("D2")

    with col2:
        PPE = st.text_input("PPE")

    # code for Prediction
    parkinsons_diagnosis = " "

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_disease.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 0):
            parkinsons_diagnosis = "Hurrah! You don't have Parkinson's Disease."
        else:
            parkinsons_diagnosis = "Sorry! You have Parkinson's Disease."

    st.success(parkinsons_diagnosis)


# Breast Cancer Prediction Page:

if (selected == "Breast Cancer Prediction"):

    # page title
    st.title("Breast Cancer Prediction using Machine Learning")
    set_background('./bgs/sthe.jpg', size="fit")


# getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        id = st.number_input("id")

    with col2:
        radius_mean = st.number_input("radius_mean")

    with col3:
        texture_mean = st.number_input("texture_mean")

    with col4:
        perimeter_mean = st.number_input("perimeter_mean")

    with col5:
        area_mean = st.number_input("area_mean")

    with col1:
        smoothness_mean = st.number_input("smoothness_mean")

    with col2:
        compactness_mean = st.number_input("compactness_mean")

    with col3:
        concavity_mean = st.number_input("concavity_mean")

    with col4:
        concave_points_mean = st.number_input("concave points_mean")

    with col5:
        symmetry_mean = st.number_input("symmetry_mean")

    with col1:
        fractal_dimension_mean = st.number_input("fractal_dimension_mean")

    with col2:
        radius_se = st.number_input("radius_se")

    with col3:
        texture_se = st.number_input("texture_se")

    with col4:
        perimeter_se = st.number_input("perimeter_se")

    with col5:
        area_se = st.number_input("area_se")

    with col1:
        smoothness_se = st.number_input("smoothness_se")

    with col2:
        compactness_se = st.number_input("compactness_se")

    with col3:
        concavity_se = st.number_input("concavity_se")

    with col4:
        concave_points_se = st.number_input("concave points_se")

    with col5:
        symmetry_se = st.number_input("ssymmetry_se")

    with col1:
        fractal_dimension_se = st.number_input("fractal_dimension_se")

    with col2:
        radius_worst = st.number_input("radius_worst")

    with col3:
        texture_worst = st.number_input("texture_worst")

    with col4:
        perimeter_worst = st.number_input("perimeter_worst")

    with col5:
        area_worst = st.number_input("area_worst")

    with col1:
        smoothness_worst = st.number_input("smoothness_worst")

    with col2:
        compactness_worst = st.number_input("compactness_worst")

    with col3:
        concavity_worst = st.number_input("concavity_worst")

    with col4:
        concave_points_worst = st.number_input("concave points_worst")

    with col5:
        symmetry_worst = st.number_input("symmetry_worst")

    with col1:
        fractal_dimension_worst = st.number_input("fractal_dimension_worst")

    # code for Prediction
    breast_cancer_check = " "

    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer.predict([[id, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                                                         compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

        if (breast_cancer_prediction[0] == 0):

            breast_cancer_check = "Hurrah! You don't have Breast Cancer."
        else:
            breast_cancer_check = "Sorry! You have Breast Cancer."

    st.success(breast_cancer_check)
if (selected == "Pneumonia"):
    # page title
    st.title("Pneumonia classification")
    st.header('Please upload a chest X-ray image')
    set_background('./bgs/sthe.jpg', size="fit")

    # upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

    # load classifier
    model = load_model('./model/pneumonia_classifier.h5')

    # load class names
    with open('./model/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
        f.close()

    # display image
    if file is not None:
        image = Image.open(file).convert('RGB')
        st.image(image, use_column_width=True)

        # classify image
        class_name, conf_score = classify(image, model, class_names)

        # write classification
        st.write("## {}".format(class_name))
        st.write("### score: {}%".format(int(conf_score * 1000) / 10))

# Lung Cancer Prediction Page:

if (selected == "Lung Cancer Prediction"):

    # page title
    st.title("Lung Cancer Prediction using Machine Learning")
    set_background('./bgs/sthe.jpg', size="fit")


# getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        GENDER = st.number_input("GENDER")

    with col2:
        AGE = st.number_input("AGE")

    with col3:
        SMOKING = st.number_input("SMOKING")

    with col4:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")

    with col1:
        ANXIETY = st.number_input("ANXIETY")

    with col2:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")

    with col3:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")

    with col4:
        FATIGUE = st.number_input("FATIGUE")

    with col1:
        ALLERGY = st.number_input("ALLERGY")

    with col2:
        WHEEZING = st.number_input("WHEEZING")

    with col3:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")

    with col4:
        COUGHING = st.number_input("COUGHING")

    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")

    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")

    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")


# code for Prediction
    lung_cancer_result = " "

    # creating a button for Prediction

    if st.button("Lung Cancer Test Result"):
        lung_cancer_report = lung_cancer.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE,
                                                 FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

        if (lung_cancer_report[0] == 0):
            lung_cancer_result = "Hurrah! You have no Lung Cancer."
        else:
            lung_cancer_result = "Sorry! You have Lung Cancer."

    st.success(lung_cancer_result)
