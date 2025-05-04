import streamlit as st

st.title("Introduction")

st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

column1, column2 = st.columns(2, gap='small', vertical_alignment='center')

with column1:
    st.image("./sections/about_me/profile_pic.jpeg", width=250)
with column2:
    st.html("My name is Ricardo Oliveira, I'm a Ph.D student at <b>École Centrale Lyon</b>.")

    st.html("My topic of studies is on aeroelastic simulations of a ultra-high bypass ration fan.<br>"
            "Check out more about the ECL5 UHBR open test case here:")

    st.html("My interests range lie in turbomachinery design and analysis and in overall fluid mechanics and structural topics.")

st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

st.html("With this page I intend to summarize my projects and previous experience and educational achievements.")

st.html("I hope you enjoy it and feel free to contact me if you have any questions or comments! <br>"
        "ricardooliv22@gmail.com")
