import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="IS 1608:2005 Explorer", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Key Definitions", "Test Procedures", "Calculations Lab"])

# --- Title Section ---
st.title("IS 1608:2005 Interactive Guide")
st.subheader("Metallic Materials – Tensile Testing at Ambient Temperature")

if page == "Overview":
    st.info("This standard specifies the method for tensile testing of metallic materials and defines the mechanical properties which can be determined.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Key Scopes
        * **Temperature Range:** $10^{\circ}C$ to $35^{\circ}C$ (Standard: $23^{\circ}C \pm 5^{\circ}C$).
        * **Principles:** Straining a test piece by tensile force to fracture.
        * **Apparatus:** Must be Class 1 or better (ISO 7500-1).
        """)
    with col2:
        st.write("### Test Piece Types")
        st.table(pd.DataFrame({
            "Product Type": ["Sheets/Strips", "Wire/Bars", "Tubes"],
            "Thickness/Dia": ["0.1 to 3mm", "< 4mm", "Full cross-section"],
            "Annex Reference": ["Annex A", "Annex B", "Annex D"]
        }))

elif page == "Key Definitions":
    st.header("Understanding the Terminology")
    
    with st.expander("1. Gauge Length (L)"):
        st.write("The length of the cylindrical or prismatic portion of the test piece on which elongation is measured.")
        st.latex(r"L_o = k\sqrt{S_o}")
        st.caption("Commonly, $k = 5.65$ for proportional test pieces.")
        st.caption("$S_o$: The original cross-sectional area.")

    with st.expander("2. Yield Strength (Re)"):
        st.write("**Upper Yield Strength ($R_{eH}$):** Value of stress at the moment when the first decrease in force is observed.")
        st.write("**Lower Yield Strength ($R_{eL}$):** Lowest value of stress during plastic yielding.")

    with st.expander("3. Tensile Strength (Rm)"):
        st.write("Stress corresponding to the maximum force ($F_m$).")

elif page == "Test Procedures":
    st.header("Standardized Testing Rates")
    st.warning("Speed control is critical for accurate Yield Strength determination.")
    
    st.markdown("""
    ### Rate of Stressing (Table 3)
    For materials with Modulus of Elasticity ($E$):
    - **< 150,000 N/mm²:** 2 to 20 $N/mm^2 \cdot s^{-1}$
    - **≥ 150,000 N/mm²:** 6 to 60 $N/mm^2 \cdot s^{-1}$
    """)
    
    st.write("### Gripping Method")
    st.write("Force must be applied as axially as possible to avoid bending moments, especially for brittle materials.")

elif page == "Calculations Lab":
    st.header("Interactive Calculations")
    st.write("Input your test data to see how the properties are calculated per IS 1608.")

    col_a, col_b = st.columns(2)
    
    with col_a:
        f_max = st.number_input("Maximum Force ($F_m$) in Newtons", value=50000)
        diameter = st.number_input("Original Diameter ($d$) in mm", value=10.0)
        l_original = st.number_input("Original Gauge Length ($L_o$) in mm", value=50.0)
        l_final = st.number_input("Final Gauge Length ($L_u$) in mm", value=62.5)

    # Logic
    area = (np.pi * (diameter**2)) / 4
    tensile_strength = f_max / area
    elongation = ((l_final - l_original) / l_original) * 100

    with col_b:
        st.metric("Original Area ($S_o$)", f"{area:.2f} mm²")
        st.metric("Tensile Strength ($R_m$)", f"{tensile_strength:.2f} N/mm²")
        st.metric("Percentage Elongation (A)", f"{elongation:.1f} %")

    if st.button("Generate Report Summary"):
        st.success(f"The material has a tensile strength of {tensile_strength:.2f} MPa.")
