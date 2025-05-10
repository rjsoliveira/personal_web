import streamlit as st

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.title("Tandem-blade centrifugal compressor design and optimization by means of 3D inverse design")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("This work was performed while at Advanced Design Technology, and submitted to the 15th European Conference in Turbomachinery. The paper was then presented in April 2023 in Budapest. <br><br>"
            "The work consisted in the redesign of a open access centrifugal compressor design, by application of a tandem blade configuration. "
            "The goal was to develop a workflow leveraging the 3D inverse design method available at ADT that can be applied to tandem configurations, and investigate if efficiency improvements were "
            "possible with this configuration. <br><br>"
            "An entropy analysis, based in decomposing the flow field in different regions and quantifying entropy generation rate, was applied to understand where improvements were being "
            "obtained from. The final optimized design increased efficiency by approximately 0.5% and increased pressure ratio was achieved for the entire speedline. "
            "During the design process, the conclusion that loading distribution between inducer and exducer was key in achieving an optimized design was obtained. <br><br>")

column1, column2, c_sep,column3, column4  = st.columns([0.2, 0.35, 0.02, 0.23, 0.2], vertical_alignment='top')
with column2:
    st.image("./sections/publications/tandem_blade_1.png", use_container_width=True)
with column3:
    st.image("./sections/publications/tandem_blade.png", use_container_width=True)

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    with st.expander("Abstract"):
        st.write('''
            In centrifugal compressor design, previous studies have shown the potential of achieving enhanced performance through the inclusion of tandem blades. 
            The conventional design method for this type of machines is based in splitting a baseline impeller into main and tandem blade, and applying appropriate pitchwise and streamwise displacements. 
            This simple design method has been proven insufficient in achieving better performance than the baseline design, without extra design modifications. 
            In this paper, a design workflow based in a 3D inverse design method is specifically assembled and applied to the tandem-blade design of centrifugal compressors. 
            The blade geometry is controlled by imposing specified distributions of blade loading in tandem and main blades. 
            Starting from an initial full blade design, different tandem-blade designs are generated using the inverse design methodology. 
            Performance of the initial and optimized designs are then assessed by 3D CFD analysis at design and off-design conditions. 
            The mechanism of performance improvement is investigated in detail. 
            In addition, the structural performance of the generated designs is also assessed by means of FEA. 
        ''')

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    with st.expander("Links"):
        url = "https://www.euroturbo.eu/publications/proceedings-papers/etc2023-270/"
        st.write("[PDF](%s)" % url)

        url = "https://info.adtechnology.com/webinar-3d-inverse-design-of-a-centrifugal-compressor-with-tandem-blade-configuration"
        st.write("[Webinar](%s)" % url)