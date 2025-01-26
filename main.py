import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.resnet import preprocess_input
from PIL import Image
import pickle
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Set the page layout
# st.set_page_config(page_title="Sidebar Navigation", layout="wide")

# constants
IMG_SIZE = (224, 224)
IMG_ADDRESS = "https://www.mub.eps.manchester.ac.uk/science-engineering/wp-content/uploads/sites/59/2021/10/Mars-banner.jpg"
IMAGE_NAME = "user_image.png"
CLASS_LABEL = ["apxs", "apxs cal target", "chemin inlet open", "drill", "drt front", "drt side", "ground", "horizon", "inlet", "mahli cal target",  "mastcam cal target", "observation tray", "portion box", "portion tube", "portion tube opening", "rems uv sensor",  "scoop",  "wheel"]
CLASS_LABEL.sort()

IMAGE_URL = "https://media.istockphoto.com/id/1353996563/photo/following-shot-of-brave-astronaut-in-space-suit-confidently-walking-on-mars-to-earth-alien.jpg?s=612x612&w=0&k=20&c=uMcSSDzIB5uooR6CN0Uvytlliyc0dR5iAhKODQpUr2c="

@st.cache_resource
def get_ConvNeXtXLarge_model():

    # Download the model, valid alpha values [0.25,0.35,0.5,0.75,1]
    base_model = tf.keras.applications.ConvNeXtXLarge(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    # Add average pooling to the base
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    model_frozen = Model(inputs=base_model.input,outputs=x)

    return model_frozen


@st.cache_resource
def load_sklearn_models(model_path):

    with open(model_path, 'rb') as model_file:
        final_model = pickle.load(model_file)

    return final_model


def featurization(image_path, model):

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=IMG_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    predictions = model.predict(img_preprocessed)

    return predictions

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
    # get the featurization model
    ConvNeXtXLarge_featurized_model = get_ConvNeXtXLarge_model()
    # load ultrasound image
    classification_model = load_sklearn_models("MLP_best_model.pkl")


    # web app

    # title
    st.title("Mars Image Classification")
    # image
    st.image(IMG_ADDRESS, caption = "Mars Image Classification")

    # input image
    st.subheader("Please Upload a Mars image")

    # file uploader
    image = st.file_uploader("Please Upload a Mars Image", type = ["jpg", "png", "jpeg"], accept_multiple_files = False, help = "Upload an Image")

    if image:
        user_image = Image.open(image)
        # save the image to set the path
        user_image.save(IMAGE_NAME)
        # set the user image
        st.image(user_image, caption = "User Uploaded Image")

        #get the features
        with st.spinner("Processing......."):
            image_features = featurization(IMAGE_NAME, ConvNeXtXLarge_featurized_model)
            model_predict = classification_model.predict(image_features)
            result_label = CLASS_LABEL[model_predict[0]]
            st.success(f"Prediction: {result_label}")

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
