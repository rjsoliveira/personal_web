import streamlit as st

st.title("Experience")

st.markdown('####')

# ADT
column1, column2, c3 = st.columns([0.07, 0.53, 0.3], vertical_alignment='top')
with column1:
    st.image("./sections/about_me/adtechnology_logo.jpeg", width=150)
with column2:
    st.html("<b>Advanced Design Technology</b> <br>"
            "Turbomachinery Design Engineer <br>"
            "<i>(2020 - 2024)</i>")
    st.write('''
        Engineering design and analysis role for turbomachinery development, involving consultancy projects for external clients, R&D for internal products and 
        sales and customer support tasks to showcase the companies capabilities.
    ''')

column1, column2 = st.columns([0.6, 0.3], vertical_alignment='top')
with column1:
    with st.expander("Details"):
        st.write('''
            - **Consultancy**
                - Turbomachinery design projects for various types: centrifugal and axial pumps and compressors; Radial Inflow Turbines and Hydraulic turbines
                - Objectives consisting in meeting client requirements in terms of efficiency; manufacturing constraints; off-design performance; cavitation; shut-off/maximum power.
            - **Research and development**
                - 15th European turbomachinery conference
                    - 3D Inverse Design of a Centrifugal Compressor with Tandem-Blade Configuration
                - Development of a machine learning predictive system for Design of Experiments automatic input setup
                - Robust design and optimization workflow considering manufacturing deviations.
            - **Software development**
                - Integration of in-house software module with ANSYS workbench using python
                - Development and integration of automatic parameterization system for meridional channel design or turbomachinery components
                - Responsible of feature development from engineering point of view (proxy customer and testing) in multiple features
            - **Sales and customer support**
                - Ensuring success of technical software demonstrations and trials.
                - Technical presentations (Conferences, webinars)
                - Continuous customer support
    ''')

column1, column2 = st.columns([0.6, 0.3], vertical_alignment='top')
with column1:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")

column1, column2 = st.columns([0.3, 0.7], gap='small', vertical_alignment='top')
with column1:
    st.image("./sections/about_me/nlr_logo.jpeg", width=150)
with column2:
    st.html("<b>Netherlands Aerospace Center</b> <br>"
            "CFD Engineer <br>"
            "<i>(Aug 2018 - Nov 2018)</i>")
    st.html("<ul>Internship in the scope of MSc degree at TUDelft. </ul>")

column1, column2 = st.columns([0.6, 0.3], vertical_alignment='top')
with column1:
    with st.expander("Details"):
        st.write('''
            - Comparison of CFD generated aerodynamic ship data against wind tunnel data involving the study of solver settings, 
                turbulence models, mesh quality and boundary conditions. 
            - Post processing and comparison with wind tunnel experimental data
        ''')