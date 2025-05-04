import streamlit as st

# INTRODUCTION PAGE
intro_page = st.Page(
    page="sections/about_me/introduction.py",
    title="Introduction",
    icon=":material/account_circle:",
    default=True
)

# EDUCATION
education_page = st.Page(
    page="sections/about_me/education.py",
    title="Education",
    icon=":material/account_circle:",
)

# EXPERIENCE
experience_page = st.Page(
    page="sections/about_me/experience.py",
    title="Professional experience",
    icon=":material/account_circle:",
)

# EXPERIENCE
publication_tandem = st.Page(
    page="sections/publications/tandem_blade.py",
    title="Tandem-blade centrifugal compressor design and optimization by means of 3D inverse design",
    icon=":material/account_circle:",
)

# PROJECT PAGE
project_cross_correlations_python = st.Page(
    page="sections/projects/cross_correlations.py",
    title="Cross correlations",
    icon=":material/account_circle:"
)

# NAVIGATION
pg = st.navigation(
    {"About me": [intro_page, education_page, experience_page],
     "Publications": [publication_tandem],
     "Projects": [project_cross_correlations_python]
     }
)

pg.run()
