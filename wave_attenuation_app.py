import streamlit as st
import numpy as np
import plotly.graph_objects as go
from matplotlib.pyplot import yscale

# Set up the Streamlit page
st.set_page_config(page_title='Wave attenuation through medium')
st.title('Wave attenuation through medium')

st.markdown("""
This example aims to illustrate the effect of propagation on a signal. We use a source level of $189$ dB re. 1μPa @ 1m, 
representative of fin whales source levels and signal attenuation through geometrical spreading (cylindrical) 
that will be covered later in this lecture.
""")

# User-defined frequency
frequency = st.slider('Select source signal frequency (Hz)', min_value=10, max_value=100, value=20, step=10)
distance = st.slider('Select receiver distance (m)', min_value=1, max_value=10000, value=10, step=5)

# Generate time values
t = np.linspace(0, 1, 10000)

# Generate sine wave values
SL = 189
amplitude = 1e-6*10**(189/20)
y = amplitude * np.sin(2 * np.pi * frequency * t)
TL = 10*np.log10(distance)
y_received = y*10**(-TL/10)

# Create the Plotly figure
fig = go.Figure()

# Add sine wave trace
fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name=f'Source signal'))
fig.add_trace(go.Scatter(x=t, y=y_received, mode='lines', name=f'Received signal'))

# Update layout
fig.update_layout(
    title='Representation of the source and received signals in Pascals',
    xaxis_title='Time (s)',
    yaxis_title='Amplitude (Pa)',
    template='plotly_dark'
)

# Show plot in Streamlit
st.plotly_chart(fig)


# Create the Plotly figure
fig2 = go.Figure()

# Add sine wave trace
fig2.add_trace(go.Scatter(x=t, y=20*np.log10(np.abs(y/1e-6)), mode='lines', name=f'Source signal'))
fig2.add_trace(go.Scatter(x=t, y=20*np.log10(np.abs(y_received/1e-6)), mode='lines', name=f'Received signal'))

# Update layout
fig2.update_layout(
    title='Representation of the source and received signals in dB',
    xaxis_title='Time (s)',
    yaxis_title='Amplitude (dB re. 1μPa)',
    template='plotly_dark',
    yaxis=dict(range=[40,200])
)

# Show plot in Streamlit
st.plotly_chart(fig2)
