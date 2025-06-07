import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.tittle("Heart Drawing")

t = np.linspace(0, 2, * np.pi, 1000)
x = 15 * np.cos(t) - 5 * np.cos(2 *t) - 2 * np.cos(3*t) -np.sin(4*t)
y = 13 * np.sin(t) - 5 * np.sin(2*t) - 2 * np.sin(3*t) -np.sin(4*t)

fig, ax = plt.subplots()
fig.patch.set_facecolor('balack')
ax.set_facecolor('black')
ax.plot(x * 10, color='hotpink')
ax.axist('off')
ax.set_aspect('equal')

st.pyplot(fig)

st.markdown(
    "<center><h3 style='color:hotpink;'>Made with ❤️ using streamlit</h3></center>"
    unsafe_allow_html=true
)

