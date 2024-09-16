import streamlit as st


# Set up the Streamlit page
st.set_page_config(page_title='Propagation examples')
st.title('Propagation examples')

import streamlit as st

st.header("Sonar equation")
# Display the equation in LaTeX
st.latex(r"SL - TL - (NL - PG) \geq DT")

# Explanation of variables
st.markdown("""
- **SL**: Source Level in dB re. 20µPa @ 1m,
- **Pl**: Propagation Loss in dB,
- **NL**: Ambient Noise Level in dB re. 20µPa,
- **PG**: Processing Gain in dB, and
- **DT**: Detection Threshold in dB re. 20µPa.
""")

st.divider()
st.header("Example 1: Evaluation of the source level of the White Bellbird")

# Text description and link
st.markdown("""
The White Bellbird holds a Guinness Book of World Records entry as the loudest bird in the world: 
[Youtube link](https://youtu.be/dvK-DujvpSY?si=Y-fX5posH9WcucCu)
""")

# Additional description
st.markdown("""
You're in charge of reproducing the measurement of its source level and plan to use the sonar equation as in (eq. 1).
""")

# Display the transformed equation in LaTeX
st.markdown("Transformed to determine $SL$ it becomes (eq. 2):")
st.latex(r"SL = DT + TL + NL - PG")

st.image("/Users/lb736/Documents/08. TEACHING/2024 Cornell/20230917 Sound Propagation/PropagationLossExamples/img/SourceLevel.png",
         caption=None,
         width=None,
         use_column_width=None,
         clamp=False,
         channels="RGB", output_format="auto")

st.markdown("""
To avoid damaging your recording equipment, you take the measurement at a distance where the propagation loss ($PL$) 
is estimated to be 65 dB in the bandwidth of the White Bellbird call. 

The recording is performed with a focal recorder with a parabolic reflector that gives you a processing gain ($PG$) of 4 dB, allowing a detection threshold ($DT$) of 0. 

In the same frequency band, the ambient noise at your field site is $NL = 60$ dB.
""")

# Solve using user inputs

# Function to calculate Source Level (SL)
def find_SL(DT, TL, NL, PG):
    SL = DT + TL + NL - PG
    # Using st.markdown for colored output in a green textbox
    st.markdown(f"""
    <div style="background-color:#d4edda;padding:10px;border-radius:5px;">
        <p style='color:#155724; font-size:20px;'>SL = {SL} dB re. 20µPa @ 1m</p>
    </div>
    """, unsafe_allow_html=True)

# Creating 4 columns for the sliders
col1, col2, col3, col4 = st.columns(4)

# Sliders in each column
with col1:
    DT = st.slider("Detection threshold (DT)", min_value=0, max_value=20, step=1, value=3)

with col2:
    TL = st.slider("Propagation Loss (PL)", min_value=0, max_value=120, step=5, value=60)

with col3:
    NL = st.slider("Noise Level (NL)", min_value=0, max_value=120, step=2, value=64)

with col4:
    PG = st.slider("Processing Gain (PG)", min_value=0, max_value=30, step=1, value=0)

# Call the function with slider values
find_SL(DT, TL, NL, PG)
