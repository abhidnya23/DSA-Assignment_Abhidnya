import streamlit as st
import numpy as np
import joblib 

model=joblib.load('model.pkl')
scaler=joblib.load('scaler.pkl')
encoders=joblib.load('encoders.pkl')

st.title('House Price Prediction')

area=st.number_input('Area in square feet')
bedrooms=st.number_input('Number of bedrooms')
bathrooms=st.number_input('Number of bathrooms')
stories=st.number_input('Number of stories')
parkings=st.number_input('Number of parking spaces')
mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus=st.selectbox('Furnishing status', ['Unfurnished', 'Semi-furnished', 'Furnished'])

def encode_input(col, value):
    value = value.lower() 
    return encoders[col].transform([value])[0]
input_data = np.array([[
                        area, bedrooms, bathrooms, stories, parkings,
                        encode_input('mainroad', mainroad), 
                        encode_input('guestroom', guestroom),
                        encode_input('basement', basement),
                        encode_input('hotwaterheating', hotwaterheating), 
                        encode_input('airconditioning', airconditioning), 
                        encode_input('prefarea', prefarea), 
                        encode_input('furnishingstatus', furnishingstatus)
                        ]])
input_data_scaled = scaler.transform(input_data)

if st.button('Predict Price'):  
    prediction = model.predict(input_data_scaled)
   #st.write(f'Predicted House Price: {prediction[0]:.2f}')
    st.success(f'Estimated Price:  {int(prediction[0]):,}')