# Fashion-Recommendation-System-using-Image-Features

Introduction to the Fashion Recommendation System This project can be thought of as a content-based image recommendation, only this time the recommended images refer to similar fashion items that match user-uploaded item. Implemented using TensorFlow, ResNet50 and Streamlit where a deep learning model writes the features of an image to be compared with images in that datase

# Project Overview

The Fashion Recommendation System using Image Features leverages image feature extraction to identify visually similar items based on a user-uploaded image. This project uses a pre-trained ResNet50 model to extract features, which are then stored and compared to provide recommendations.

# Features

Upload an image to get visually similar recommendations.

Add recommended items to a personal "Favorites" list.

Display favorites, with options to remove items.

Web-based interface using Streamlit for easy interaction.

# required libraries:

tensorflow

keras

numpy

scikit-learn

matplotlib 

streamlit 

pillow

# Usage

1.Feature Extraction:

  python feature_extraction.py
  
2.Start the Application:

  streamlit run main.py
  
3.Exploring Pages:

  Home Page: Introduction and navigation to other pages.
  
  Recommendation Page: Upload an image to get recommendations and add items to favorites.
  
  Favorites Page: View and manage your favorite items.
  
  About Page: Learn about the purpose and inspiration behind this project.
