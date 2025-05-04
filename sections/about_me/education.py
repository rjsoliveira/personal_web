import streamlit as st

st.title("Education")

# st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

# BACHELOR
column1, column2 = st.columns(2, gap='small', vertical_alignment='center')
with column1:
    st.image("./sections/about_me/IST_logo.png", width=100)
with column2:
    st.html("Bachelor in <b>Aerospace Engineering</b>.")

# st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")
