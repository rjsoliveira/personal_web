import streamlit as st
st.set_page_config(layout="wide")

# ABOUT ME
intro_page = st.Page(
    page="sections/about_me/introduction.py",
    title="Introduction",
    icon=":material/account_circle:",
    default=True
)

education_page = st.Page(
    page="sections/about_me/education.py",
    title="Education",
    icon=":material/school:",
)

experience_page = st.Page(
    page="sections/about_me/experience.py",
    title="Professional experience",
    icon=":material/cases:",
)

# PUBLICATIONS
publication_tandem = st.Page(
    page="sections/publications/tandem_blade.py",
    title="Tandem-blade centrifugal compressor design and optimization by means of 3D inverse design",
    icon=":material/book_ribbon:",
)

publication_orc = st.Page(
    page="sections/publications/orc_aeroelastic.py",
    title="Assessment and impact of aeroelastic effects on highly supersonic orginic rankine cycle turbine",
    icon=":material/book_ribbon:",
)

# PROJECT PAGE
project_cross_correlations_python = st.Page(
    page="sections/projects/cross_correlations.py",
    title="Project 1",
    icon=":material/account_circle:"
)

# NAVIGATION
pg = st.navigation(
    {"About me": [intro_page, education_page, experience_page],
     "Publications": [publication_tandem, publication_orc],
     "Projects": [project_cross_correlations_python]
     }
)

pg.run()
