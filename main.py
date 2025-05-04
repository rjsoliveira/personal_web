import streamlit as st

about_me_page = st.Page(
    page="sections/about_me.py",
    title="About me",
    icon=":material/account_circle:",
    default=True
)

projects_page = st.Page(
    page="sections/projects.py",
    title="Projects",
    icon=":material/account_circle:"
)

pg = st.navigation(
    {"About me": [about_me_page],
     "Projects": [projects_page]
     }
)

st.logo("assets/arancha_a_comer.jpg")
st.sidebar.text("Made by Ricardo")

pg.run()
