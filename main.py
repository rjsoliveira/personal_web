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

projects_page = st.Page(
    page="sections/projects.py",
    title="Projects",
    icon=":material/account_circle:"
)

pg = st.navigation(
    {"About me": [intro_page, education_page],
     "Projects": [projects_page]
     }
)

pg.run()
