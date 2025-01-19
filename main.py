import streamlit as st
st.title("Mars Image Classification")

# Set the page layout
# st.set_page_config(layout="wide")

# Create three columns for sidebars and the main content area
col1, col2, col3 = st.columns([1, 1, 2], gap="medium")

# Sidebar 1 (Simulated with a column)
with col1:
    st.markdown("### Sidebar 1")
    option1 = st.selectbox("Select an option:", ["Option A", "Option B", "Option C"])
    slider1 = st.slider("Adjust a value:", 0, 100, 50)
    st.button("Submit (Sidebar 1)")

# Sidebar 2 (Simulated with a column)
with col2:
    st.markdown("### Sidebar 2")
    checkbox = st.checkbox("Enable feature")
    option2 = st.radio("Choose a category:", ["Category X", "Category Y", "Category Z"])
    st.button("Submit (Sidebar 2)")

# Main Content Area
with col3:
    st.markdown("## Main Content Area")
    st.write("This is where the main content of your app will go.")

    # Display selections from sidebars
    st.write(f"Sidebar 1 Selection: {option1}, Slider Value: {slider1}")
    st.write(f"Sidebar 2 Checkbox: {checkbox}, Category: {option2}")

    # Example chart
    st.line_chart({"Data": [1, 2, 3, 4, 5]})
