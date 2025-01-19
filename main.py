import streamlit as st
# from PIL import image

# Set the page layout
# st.set_page_config(page_title="Sidebar Navigation", layout="wide")

IMAGE_URL = "https://media.istockphoto.com/id/1353996563/photo/following-shot-of-brave-astronaut-in-space-suit-confidently-walking-on-mars-to-earth-alien.jpg"

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page:",
    ["About",  "Classification", "History"]
)

# Main Content Area
if page == "About":
    st.image(IMAGE_URL, caption = "Image Classification")
    st.title("Welcome to the About Page")
    st.write("This is the about page of your app.")
    st.write("You can include introductory text, charts, or other content here.")
    st.bar_chart([3, 2, 4, 5])

elif page == "Classification":
    st.title("About Us")
    st.write("This is the about page of your app.")
    st.write("Here, you can describe the purpose of your app or provide background information.")
    st.image("https://via.placeholder.com/400", caption="About Us")

elif page == "History":
    st.title("Contact Us")
    st.write("This is the contact page of your app.")
    st.write("Provide a way for users to get in touch with you.")
    contact_form = """
    <form action="https://formsubmit.co/example@example.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
