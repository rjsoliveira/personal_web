import streamlit as st

st.title("Education")

st.markdown('####')

# PHD
column1, column2, c_separator, column3, column4  = st.columns([0.2, 0.1, 0.02, 0.48, 0.2], vertical_alignment='top')

with column2:
    st.image("./sections/about_me/centrale_lyon_logo.jpeg", use_container_width=True)
with column3:
    st.html('''
                <b>École Centrale Lyon</b> </br>
                PhD in advanced aeroelastic simulations of fans and high-speed compressors</br>
                <i>(2024 - Current)</i>
            ''')

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")


# ----------

column1, column2, c_separator, column3, column4  = st.columns([0.2, 0.1, 0.02, 0.48, 0.2], vertical_alignment='top')

with column2:
    st.image("./sections/about_me/TUD_Logo.png", use_container_width=True)
with column3:
    st.html('''
                <b>Technical University of Delft</b> </br>
                Masters in Aerospace Engineering - Power and Propulsion</br>
                <i>(2017 - 2020)</i>
            ''')

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")



column1, column2, c_separator, column3, column4  = st.columns([0.2, 0.1, 0.02, 0.48, 0.2], vertical_alignment='top')

with column2:
    st.image("./sections/about_me/IST_Logo.png", width = 150)
with column3:
    st.html('''
                <b>Instituto Superior Técnico</b> </br>
                Bachelor in Aerospace Engineering </br>
                <i>(2013 - 2017)</i>
            ''')

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")


#
#
#
#
#
#
#
# # PHD
# column1, column2, c3 = st.columns([0.07, 0.53, 0.3], vertical_alignment='top')
# with column1:
#     st.image("./sections/about_me/centrale_lyon_logo.jpeg", use_container_width=True)
# with column2:
#     st.html('''
#                 <b>École Centrale Lyon</b> </br>
#                 PhD in advanced aeroelastic simulations of fans and high-speed compressors</br>
#                 <i>(2024 - Current)</i>
#             ''')
#
# column1, column2 = st.columns([0.6, 0.3], vertical_alignment='top')
# with column1:
#     st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")
#
# # MASTERS
# column1, column2, c3 = st.columns([0.07, 0.53, 0.3], gap='small', vertical_alignment='top')
# with column1:
#     st.image("./sections/about_me/TUD_Logo.png", use_container_width=True)
# with column2:
#     st.html('''
#                 <b>Technical University of Delft</b> </br>
#                 Masters in Aerospace Engineering - Power and Propulsion</br>
#                 <i>(2017 - 2020)</i>
#             ''')
#
#
# column1, column2 = st.columns([0.6, 0.3], vertical_alignment='top')
# with column1:
#     st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")
#
# # BACHELOR
# column1, column2, c3 = st.columns([0.07, 0.53, 0.3], gap='small', vertical_alignment='top')
# with column1:
#     st.image("./sections/about_me/IST_Logo.png", use_container_width=True)
# with column2:
#     st.html('''
#                 <b>Instituto Superior Técnico</b> </br>
#                 Bachelor in Aerospace Engineering </br>
#                 <i>(2013 - 2017)</i>
#             ''')
#
# column1, column2 = st.columns([0.6, 0.3], gap='small', vertical_alignment='top')
# with column1:
#     st.html("<hr style=\"width:100%;text-align:left;margin-left:0\">")