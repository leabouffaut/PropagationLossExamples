import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set up the Streamlit page
st.set_page_config(page_title='Propagation examples')
st.title('Propagation examples')


st.header("Sonar equation (eq. 1)")
# Display the equation in LaTeX
st.latex(r"SL - PL - (NL - PG) \geq DT")

# Explanation of variables
st.markdown("""
- **SL**: Source Level in dB re. 20µPa @ 1m,
- **PL**: Propagation Loss in dB,
- **NL**: Ambient Noise Level in dB re. 20µPa,
- **PG**: Processing Gain in dB, and
- **DT**: Detection Threshold in dB re. 20µPa.
""")

st.divider()
st.header("Example 2: Evaluation of the active space of Sperm whales in the Arctic")

# Heading and Introduction

st.subheader("Background on Sperm Whales and Slow Clicks")
st.markdown("""
Sperm whales are known to be the largest odontocete, a deep-diver that produces the loudest sounds in the 
animal kingdom! However, male sperm whales produce “slow clicks” that are not as loud as echolocation clicks 
and codas, repeated at a slower rate and, generally lower in frequency.

Sperm whales have been reported to produce slow clicks from the high latitude feeding grounds of the Arctic 
to the warmer breeding grounds of the Azores in the mid-Atlantic region. 

The current assumption is that slow clicks are used for male-to-male long-range communication, as opposed to 
echolocation clicks used in feeding contexts. You want to test if that would make sense in terms of acoustic 
propagation!
""")


# Direct link to the image
image_url = "https://github.com/leabouffaut/PropagationLossExamples/blob/main/ActiveSpace.png?raw=true"
st.image(image_url,
         caption=None,
         width=None,
         use_column_width=True,
         clamp=False,
         channels="RGB", output_format="auto")

# Sonar equation
st.markdown("""
At the maximum detection range, the sonar equation (eq. 1) can be written as (eq. 2):
""")

# Display equation using LaTeX
st.latex(r"SL - PL - NL + PG = DT")

st.markdown("""
To keep things simple, no assumptions are taken about the hearing of the receiver (a conspecific), 
and so we will consider the processing range to be $PG = 0$.
""")

st.subheader("1) Estimate the Propagation Loss (PL)")
st.markdown("""
Using the following numerical values $SL = 165$ dB re 1 μPa @1m, $NL = 85$ dB and $DT = 30$ dB that are true for the entire bandwidth of the slow click, what would be the value of $TL$ at the maximum range?

Isolating $PL$ from (eq. 2) it becomes (eq. 3):
""")
st.latex(r"PL = SL - NL - DT + PG")


# Function to calculate Transmission Loss (PL)
def find_TL(SL, NL, DT, PG):
    PL = SL - NL - DT + PG
    st.markdown(f"""
        <div style="background-color:#d4edda;padding:10px;border-radius:5px;">
            <p style='color:#155724; font-size:20px;'>PL = {PL} dB re. 1µPa</p>
        </div>
        """, unsafe_allow_html=True)



# Creating 4 columns for the sliders
col1, col2, col3, col4 = st.columns(4)

# Sliders in each column
with col1:
    SL = st.slider("Source Level (SL)", min_value=0, max_value=200, step=5, value=165)

with col2:
    DT = st.slider("Detection Threshold (DT)", min_value=0, max_value=60, step=5, value=30)

with col3:
    NL = st.slider("Ambient Noise Level (NL)", min_value=75, max_value=100, step=2, value=85)

with col4:
    PG = st.slider("Processing Gain (PG)", min_value=0, max_value=30, step=3, value=0)

# Call the function with slider values
find_TL(SL, NL, DT, PG)


st.subheader("2) Determine the maximum range and associated active space")
st.markdown("""
Data from bio-logging shows that slow clicks in the Arctic are produced close to the water surface.
In these colder regions, it means that the animal is vocalizing close to the minimum sound speed, 
minimizing the propagation loss, which are then mainly due to cylindrical spreading such as (eq. 4):
""")

st.latex(r"PL = 10\log_{10}(r).")

st.markdown("""
Using the previously calculated $PL$, what would be the maximum detection range?

Note:
""")

st.latex(r"y = a\log_{10}(x) <-> x = 10^{\frac{y}{a}}.")


# Heading and explanation
st.markdown("""
First, we can transform (eq. 4) to isolate the range (eq. 5):
""")
st.latex(r"r = 10^{\frac{PL}{10}}")

st.markdown("""
Then, the maximum range can be solved by replacing the previous expression of $PL$ from (eq. 3) in (eq. 5). 
It becomes:
""")

st.latex(r"r_{max} = 10^{\frac{SL - NL - DT}{10}}")


# Function to plot detection range
def plot_detection_range(SL, DT, NL, PG, geom_spreading):
    fig, ax = plt.subplots(figsize=(5, 5))

    # Calculate the radius of the circle
    radius = 10 ** ((SL - NL - DT + PG) / geom_spreading) / 1000
    plt.grid()
    # Create a circle representing the active space
    circle = plt.Circle((0, 0), radius, color='red', alpha=0.5)
    ax.add_artist(circle)

    # Set limits and labels
    ax.set_xlim([-500, 500])
    ax.set_ylim([-500, 500])
    ax.set_aspect('equal')

    #plt.title(f'Active Space = {radius:.2f} km')
    plt.xlabel('x (km)')
    plt.ylabel('y (km)')

    st.pyplot(fig)

    st.markdown(f"""
    <div style="background-color:#d4edda;padding:10px;border-radius:5px;">
    <p style='color:#155724; font-size:20px;'>Detection range = {radius} km, Active space = {np.pi*radius**2:.2f} km^2 </p>
    </div>
    """, unsafe_allow_html=True)


# Sliders for interactive input
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    geom_spreading = st.slider("Geometric Spreading (dB/km)", min_value=10, max_value=20, step=5, value=10)


# Plot the detection range
plot_detection_range(SL, DT, NL, PG, geom_spreading)

st.subheader("3) How does the active space change when increasing the noise level?")
