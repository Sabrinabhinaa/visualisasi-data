import streamlit as st
st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("animal1.jpeg")
# Image Courtesy by unplash
st.write("Image Courtesy: unsplash.com")

# Image Courtesy
st.write("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    "animal1.jpeg",
    "animal2.jpeg",
    "animal3.jpeg",
    "animal4.jpeg"
]
# Displaying Multiple image with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unsplash")

import streamlit as st
import base64
# Function to set image as background
def add_local_background_image(image_path):
    with open(image_path, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.write("Image Courtesy: Unsplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:image/jpeg;base64,{encoded_string});
    background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")

# Calling image in function 
add_local_background_image('C:/xamppp/htdocs/VISDAT/praktikum1/praktikum1.py/animal1.jpeg')

import streamlit as st
from PIL import Image
import base64

def add_local_background_image(image_path):
    try:
        with open(image_path, "rb") as image:
            encoded_string = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("Background image")
    except FileNotFoundError:
        st.error(f"Gambar tidak ditemukan di path: {image_path}")


image_path = "C:/xamppp/htdocs/VISDAT/praktikum1/praktikum1.py/animal1.jpeg"

add_local_background_image(image_path)

# Original image
original_image = Image.open(image_path)
st.subheader("Original Image")
st.image(original_image, caption="Original Image")

# Resize image to 600x400
resized_image = original_image.resize((600, 400))

# Displaying resize image
st.subheader("Resized Image")
st.image(resized_image, caption="Resized Image (600x400)")
