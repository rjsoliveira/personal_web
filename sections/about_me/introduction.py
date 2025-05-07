import streamlit as st

st.title("Introduction")

column1, column2, c3 = st.columns([0.15, 0.7, 0.15], vertical_alignment='top')

with column1:
    st.image("./sections/about_me/profile_pic.jpeg", width=200)
with column2:
    st.html("My name is Ricardo Oliveira, I'm a Ph.D student at <b>École Centrale Lyon</b>.")

    st.html("My topic of studies is on aeroelastic simulations of an ultra-high bypass ration fan.<br>"
            "Check out more about the ECL5 UHBR open test case here:")

    st.html("My interests lie in turbomachinery design and analysis and in overall fluid mechanics and structural topics.")

column1, column2 = st.columns([0.85, 0.3], vertical_alignment='top')
with column1:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

st.html("With this page I intend to summarize projects, previous experience and my education path.")

column1, column2 = st.columns([0.85, 0.3], vertical_alignment='top')
with column1:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

st.html("I hope you enjoy it and feel free to contact me if you have any questions or comments! <br>"
        "ricardooliv22@gmail.com")
