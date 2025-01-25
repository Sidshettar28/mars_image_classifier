import streamlit as st
# from PIL import image

# Set the page layout
# st.set_page_config(page_title="Sidebar Navigation", layout="wide")

IMAGE_URL = "https://media.istockphoto.com/id/1353996563/photo/following-shot-of-brave-astronaut-in-space-suit-confidently-walking-on-mars-to-earth-alien.jpg?s=612x612&w=0&k=20&c=uMcSSDzIB5uooR6CN0Uvytlliyc0dR5iAhKODQpUr2c="

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
    st.write("As space exploration companies continue to explore planets in our solar system, it is important that they not only focus on the actual exploration of a planet, but also mapping it out for future missions. As AI continues to evolve, it's abilities are able to provide these companies with an easier way of analyzing images taken during said missions.")
    st.write("\nAfter brainstorming ways to create a model that is able to analyze and categorize images, I was able to use different machine learning processes to accurately carry out this task. To ensure that my model was as accurate as possible, I began by compiling different methods of machine learning and test which was most accurate.")
    st.write("\nTo summarize what I did, I used a dataset provided by _______ with numerous images of mars taken by past missions, to train, test, validate each machine learning method. After this, I used a python code to determine which one presented the most accurate results. Now, using github, I am able to deploy a service for indiviudals to utilize by themselves.")

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
