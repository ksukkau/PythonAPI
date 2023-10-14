import streamlit as st

st.title("weather forecast for the Next days")
place = st.text_input("Place:")
days = st.slider("forecast days:", min_value=1, max_value=5,
                 help="Select the number of days for forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

