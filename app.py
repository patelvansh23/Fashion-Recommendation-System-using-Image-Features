import streamlit as st
import pickle as pkl
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPool2D
from sklearn.neighbors import NearestNeighbors
import os

def load_model():
    featurevector = pkl.load(open('Images_features.pkl', 'rb'))
    filenames = pkl.load(open('filenames.pkl', 'rb'))
    return featurevector, filenames

def extract_features_from_images(image_path, model):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_expand_dim = np.expand_dims(img_array, axis=0)
    img_preprocess = preprocess_input(img_expand_dim)
    result = model.predict(img_preprocess).flatten()
    return result / np.linalg.norm(result)

def run_app():
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []

    st.title("Fashion Recommendation App")
    
    featurevector, filenames = load_model()
    
    model = tf.keras.models.Sequential([
        ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3)),
        GlobalMaxPool2D()
    ])
    
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(featurevector)

    upload_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if upload_file is not None:
        upload_path = os.path.join('upload', upload_file.name)
        with open(upload_path, 'wb') as f:
            f.write(upload_file.getbuffer())
        
        st.subheader('Uploaded Image')
        st.image(upload_file)

        input_img_features = extract_features_from_images(upload_path, model)
        distances, indices = neighbors.kneighbors([input_img_features])

        st.subheader('Recommended Images')
        cols = st.columns(5)
        for i in range(1, 6):
            with cols[i-1]:
                st.image(filenames[indices[0][i]])
                if st.button("Add to Favorites", key=f"add_{filenames[indices[0][i]]}"):
                    item = {'name': filenames[indices[0][i]], 'image': filenames[indices[0][i]], 'price': np.random.randint(20, 100)}
                    st.session_state.favorites.append(item)
                    st.success(f"Added {item['name']} to favorites!")

def run_favorites():
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []

    st.title("Your Favorite Items")

    if st.session_state.favorites:
        cols = st.columns(3)
        to_remove = []

        for i, item in enumerate(st.session_state.favorites):
            with cols[i % 3]:
                st.image(item['image'], use_column_width=True)
                st.write(item['name'])
                st.write(f"Price: ${item['price']}")
                if st.button("Remove from Favorites", key=f"remove_{item['name']}"):
                    to_remove.append(item)

        for item in to_remove:
            st.session_state.favorites.remove(item)
            st.success(f"Removed {item['name']} from favorites.")
    else:
        st.write("No favorite items yet. Start adding some!")
