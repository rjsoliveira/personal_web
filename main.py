import streamlit as st

intro_page = st.Page(
    page="sections/about_me/introduction.py",
    title="Introduction",
    icon=":material/account_circle:",
    default=True
)

education_page = st.Page(
    page="sections/about_me/education.py",
    title="Education",
    icon=":material/account_circle:",
)

project_cross_correlations_python = st.Page(
    page="sections/projects/cross_correlations.py",
    title="Cross correlations",
    icon=":material/account_circle:"
)

pg = st.navigation(
    {"About me": [intro_page, education_page],
     "Projects": [project_cross_correlations_python]
     }
)

pg.run()
