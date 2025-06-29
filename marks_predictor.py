import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

model = LinearRegression()
model.fit(X, y)

st.title("📚 Student Marks Predictor")
st.write("Enter the number of hours studied to predict your marks!")

hours = st.slider("Hours Studied", 0.0, 12.0, step=0.5)

if st.button("Predict Marks"):
    prediction = model.predict([[hours]])
    st.success(f"📊 Predicted Marks: **{prediction[0]:.2f}**")
