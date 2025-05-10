import streamlit as st

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.title("Assessment and impact of aeroelastic effects on highly supersonic orginic rankine cycle turbine")

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    st.html("This work was performed at TUDelft and Stuttgart university (where a 4 month placement was performed), in the scope of my MSc Thesis. "
            "The goal of the thesis was to investigate the aeroelastic effects impacting an organic rankine cycle turbine "
            "An analysis chain focused on forced response analysis was developed using the NASA Rotor 67 test case and subsequently applied to the ORCHID ORC turbine developed at TUDelft. "
            )

column1, column2, column3  = st.columns([0.40, 0.2, 0.40], vertical_alignment='top')
with column2:
    st.image("./sections/publications/orc_aeroelastic_1.png", use_container_width=True)


column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    with st.expander("Abstract"):
        st.html('''
            The current high demands for the energy and transportation industries make it imperative to design efficient and reliable turbomachinery. 
            Aeroelastic phenomena such as forced response and flutter are one of the main concerns when designing these machines, and the incorrect prediction of these effects generates vibrations that can lead to structural failure due to high cycle fatigue. 
            Furthermore, the search for unconventional energy sources is also of great relevance to meet these demands. 
            Power generation using the Rankine cycle with organic fluids is one example of these technologies. 
            The different thermodynamic properties, when comparing to water, of these fluids, make it possible to use low temperature energy sources, having many practical applications such as waste heat recovery and combined power cycles. 
            </br></br>
            Organic fluids, due to their high molecular weight, are also characterized by a low speed of sound which results in a supersonic flow, leading to shock waves. 
            This unsteadiness propagates onto rotating blade rows downstream and acts as a harmonic forcing. 
            Investigating the impact of these effects on the structural integrity of small scale radial machines operating with organic fluids has not been done in the past and is the goal of this thesis. 
            <br><br>
            The assembly of a forced response analysis chain is made and is based in three main points. First, finding and characterizing resonant conditions. 
            Second, determining aerodynamic harmonic forcing and aerodynamic damping, and finally, place alternating and mean stresses against structural limits. 
            This method was applied to two test cases, the NASA rotor 67 and the ORCHID turbine. 
            The NASA rotor 67 is used as a benchmark case to assemble and validate the analysis chain due to the large amount of openly available experimental data. 
            ORCHID is a small scale ORC turbine designed at TU Delft and is used to explore the influence of the aeroelastic effects on this category of machines. 
            <br><br>
            For the ORCHID turbine, high unsteady pressures in the turbine rotor blades were observed by the simulations made. 
            This is due to the shock waves in the upstream supersonic stator, from tip leakage and from potential interactions. 
            In terms of flutter, a stable system was found for the resonant conditions studied. 
            The regions of higher unsteadiness were confined to the upstream most part of the rotor blade being excited, which correspond to areas of small modal displacements. 
            Furthermore, even with high rotational speeds, the small scale of the machine resulted in small centrifugal effects, and so in high allowable margins for alternating stresses. 
            In sum, even with a high unsteady pressure content, the mismatch between these and the mode shapes, and the positive aerodamping values, result in a safe system in terms of high cycle fatigue for the resonant conditions studied. 
            <br><br>
            The current work should be continued for the manufacture of the ORC turbine by investigating precise material properties, hub geometry and upstream inlet geometries that can lead to lower frequency resonant crossings. 
            Furthermore, the investigation of the influence of the aeroelastic issues identified on the efficiency and the incorporation of the work developed on multi­disciplinary optimization procedures is also of great relevance and a main recommendation for further studies.
        ''')

column1, column2, column3  = st.columns([0.2, 0.6, 0.2], vertical_alignment='top')
with column2:
    with st.expander("Links"):
        url = "https://repository.tudelft.nl/record/uuid:6d11770d-99bf-495a-9201-c52914077512"
        st.write("[PDF](%s)" % url)