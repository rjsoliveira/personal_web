import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Project 1")

time = np.linspace(0, 30, 500)
s1 = np.sin(time)
shift = -np.pi / 4
s2 = np.sin(time + shift)

fig, ax = plt.subplots(figsize=(8, 2))
ax.plot(time, s1, label='Sensor 1', color='Seagreen')
ax.grid(True)

st.pyplot(fig)
