import streamlit as st

st.title("Education")

st.markdown('####')

# PHD
column1, column2 = st.columns([0.15, 0.85], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/centrale_lyon_logo.jpeg", width=90)
with column2:
    st.html("PhD in advanced aeroelastic simulations of fans and high-speed compressors. <br>"
            "<i>(2024 - Current)</i>")

st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

# MASTERS
column1, column2 = st.columns([0.15, 0.85], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/TUD_Logo.png", width=90)
with column2:
    st.html("Masters in <b>Aerospace Engineering - Power and Propulsion</b>. <br>"
            "<i>(2017 - 2020)</i>")

st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

# BACHELOR
column1, column2 = st.columns([0.15, 0.85], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/IST_Logo.png", width=90)
with column2:
    st.html("Bachelor in <b>Aerospace Engineering</b>. <br>"
            "<i>(2013 - 2017)</i>")

st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")