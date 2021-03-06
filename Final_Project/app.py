# For run this app use the below line. Type it in terminal and get output
# Streamlit run app.py

import streamlit as st
from joblib import dump, load
import numpy as np 


model = load("Diabetes.joblib")


def predict_diabetes(Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input = np.array([[Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]).astype(np.float64)
    prediction = model.predict(input)
    return prediction

def main():
    st.title("Diabetes Deployment")
    html_temp = """ 
    <div style="background-color:#025246 ;padding:10px">
    <h2 style= "color:white; text-aligin:center;">Diabetes Prediction ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    Pregnancies = st.text_input("Pregnancies", "Type Here")
    Glucose = st.text_input("Glucose", "Type Here")
    BP = st.text_input("BP", "Type Here")
    SkinThickness = st.text_input("SkinThickness", "Type Here")
    Insulin = st.text_input("Insulin", "Type Here")
    BMI = st.text_input("BMI", "Type Here")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction", "Type Here")
    Age = st.text_input("Age", "Type Here")

    safe_html="""
    <div style = "background-color:#F4D03F; padding:10px >
    <h2 style = "color:white; text-align:center;"> Diabetes : NO </h2>
    </div>
    """

    danger_html = """
    <div style = "background-color:#F08080; padding:10px >
    <h2 style = "color:black; text-align:center;"> Diabetes : Yes </h2>
    </div>
    """

    if st.button("Predict"):
        output = predict_diabetes(Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.success('The probability of having Diabetes is {}'.format(output))

        if output == 1:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)



if __name__ == "__main__":
    main()



