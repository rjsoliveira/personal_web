import streamlit as st

st.title("Experience")

st.markdown('####')

# ADT
column1, column2 = st.columns([0.3, 0.7], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/adtechnology_logo.jpeg", width=150)
with column2:
    st.html("<b>Advanced Design Technology</b> <br>"
            "Turbomachinery Design Engineer <br>"
            "<i>(2020 - 2024)</i>")
    st.html("<ul>"
            "  <li>Consultancy</li>"
            "  <li>Research and development</li>"
            "  <li>Sales and customer support</li>"
            "</ul>")

st.write("Work ")
st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

column1, column2 = st.columns([0.3, 0.7], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/nlr_logo.jpeg", width=150)
with column2:
    st.html("<b>Netherlands Aerospace Center</b> <br>"
            "CFD internship <br>"
            "<i>(Aug 2018 - Nov 2018)</i>")
    st.html("<ul>Comparison of CFD generated aerodynamic ship data against wind tunnel data involving the study of solver settings, "
            "turbulence models, mesh quality and boundary conditions. Post processing and comparison with wind tunnel "
            "experimental data.</ul>")