import streamlit as st

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.title("Introduction")

st.write("###")

column1, column2, column3, column4  = st.columns([0.2, 0.1, 0.5, 0.2], vertical_alignment='top')

with column2:
    st.image("./sections/about_me/profile_pic.jpeg", width=200)

with column3:
    # st.html("My name is Ricardo Oliveira, I'm a Ph.D student at <b>École Centrale Lyon</b>.")
    st.html("<div style=\"text-align: center\"> My name is Ricardo Oliveira, I'm a Ph.D student at <b>École Centrale Lyon</b> </div>")

    st.html("<div style=\"text-align: center\"> My topic of studies is on aeroelastic simulations of an ultra-high bypass ration fan.<br>"
            "Check out more about the ECL5 UHBR open test case here: </div>")

    st.html("<div style=\"text-align: center\"> My interests lie in turbomachinery design and analysis and in overall fluid mechanics and structural topics.</b> </div>")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("With this page I intend to summarize projects, previous experience and my education path.")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("I hope you enjoy it and feel free to contact me if you have any questions or comments! <br>"
        "ricardooliv22@gmail.com")