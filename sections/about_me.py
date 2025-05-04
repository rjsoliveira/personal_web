import streamlit as st

st.title("About me")

column1, column2 = st.columns(2, gap='small', vertical_alignment='center')

with column1:
    st.image("./assets/arancha_a_comer.png")
with column2:
    st.title("Arancha a comer", anchor=False)
    st.write(
        "Esta é a Arancha a comer num restaurante chinês em Madrid"
    )