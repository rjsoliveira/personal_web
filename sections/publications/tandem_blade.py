import streamlit as st

st.title("Tandem-blade centrifugal compressor design and optimization by means of 3D inverse design")

column1, column2 = st.columns([0.5,0.5], vertical_alignment='top')
with column1:
    st.html("<i>This work was performed while at Advanced Design Technology, and submitted to the 15th European Conference in Turbomachinery. <br>"
            "The paper was then presented in April 2023 in Budapest. <br>"
            "The work consisted in the redesign of a open access test case of a centrifugal compressor, by application of a tandem blade configuration."
            "The goal was to develop a workflow leveraging the 3D inverse desing method available at ADT that can be applied to tandem configurations, and investigate if efficiency improvements were"
            "possible. Also, an entropy analysis, based in decomposing the flow field in different regions and quantifying entropy generation rate, was applied to understand where improvements were being "
            "obtained from. The final optimized design increased efficiency by approximatelly 0.5% and increased pressure ratio was also achieved for the entire speedline."
            "During the desing process, the conclusion that loading distribution between inducer and exducer was key in achieving an optimized design was reached. </i>")

with column2:
    st.image("./sections/publications/tandem_blade.png", use_container_width=True)

url = "https://www.euroturbo.eu/publications/proceedings-papers/etc2023-270/"
st.write("[PDF](%s)" % url)

url = "https://info.adtechnology.com/webinar-3d-inverse-design-of-a-centrifugal-compressor-with-tandem-blade-configuration"
st.write("[Webinar](%s)" % url)


