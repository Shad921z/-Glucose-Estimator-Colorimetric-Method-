import streamlit as st

# Add background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapers.com/images/high/dark-gradient-8km5m3gxmp08ny0f.webp");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def god_pod_glucose_estimation(A_test, A_standard, standard_concentration):
    if A_standard == 0:
        return "Error: Standard absorbance cannot be zero."
    glucose_conc = (A_test / A_standard) * standard_concentration
    return glucose_conc

def convert_to_mmol(glucose_mgdl):
    return glucose_mgdl / 18.018

st.title("🔬 GOD-POD Glucose Estimation Tool")
st.markdown("---")
st.subheader("Estimate glucose concentration from absorbance data using the GOD-POD method.")
st.markdown("---")
st.header("Input Data")

A_test = st.number_input("Enter Absorbance of Test (A_test):", min_value=0.0, format="%.4f")
A_standard = st.number_input("Enter Absorbance of Standard (A_standard):", min_value=0.0, format="%.4f")
standard_concentration = st.number_input("Standard Concentration (mg/dL):", value=100.0, format="%.2f")
dropdownunit = st.selectbox("Select Unit", ["mg/dL", "mmol/L"], index=0)

if dropdownunit == "mg/dL":
    pass
elif dropdownunit == "mmol/L":
    standard_concentration = convert_to_mmol(standard_concentration)


if st.button("Estimate Glucose Concentration"):
    result = int(god_pod_glucose_estimation(A_test, A_standard, standard_concentration))

    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Glucose Concentration: **{result:.2f} {dropdownunit}**")


    if dropdownunit == "mg/dL":
        if result > 80:
            st.warning("High glucose level detected.")
        elif result < 40:
            st.warning("Low glucose level detected.")
        else:
            st.success("Normal glucose level.")
    elif dropdownunit == "mmol/L":
        if result > 4.2:
            st.warning("HIGH glucose level detected.")
        elif result < 2.8:
            st.warning("LOW glucose level detected.")
        else:
            st.success("Normal glucose level.")


# Additional Information
st.markdown("---")
with st.expander("What does your glucose level mean?"):
    st.markdown("""
    | Condition               | Glucose (mg/dL) |
| ----------------------- | --------------- |
| Normal (Fasting)        | 70–99           |
| Prediabetes (Fasting)   | 100–125         |
| Diabetes (Fasting)      | ≥126            |
| Postprandial Normal     | <140            |
| Diabetes (Postprandial) | ≥200            |


    ❗These values may vary slightly depending on the lab or clinical guideline.
    """)


