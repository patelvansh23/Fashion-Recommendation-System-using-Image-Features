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

# Screenshots

![image](https://github.com/user-attachments/assets/5af50d95-a4a9-4960-8eba-2565ed31df4b)

![image](https://github.com/user-attachments/assets/e966d5b6-fc7f-4e63-a431-d0f4ec5ca958)

![image](https://github.com/user-attachments/assets/a71e4c98-4ec5-4b29-a18c-41af7d312862)

![image](https://github.com/user-attachments/assets/19e55e5e-6b2f-4958-8545-30c731fb3a3c)

# Dataset

dataset 1:https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset

dataset 2:https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images

# Acknowledgments

This project uses ResNet50 for feature extraction, with weights trained on the ImageNet dataset.

Built with Streamlit for interactive web-based applications.
