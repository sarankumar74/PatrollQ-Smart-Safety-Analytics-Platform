import streamlit as st
import os
from PIL import Image


st.set_page_config(page_title="Crime Clustering Dashboard", layout="wide")

st.title("🧠 Chicago Crime Clustering Dashboard")
st.markdown("Explore all clustering models and visualizations below.")


BASE_DIR = "C:/Users/saran/OneDrive/Desktop/PatrollQ/Plots"  


categories = {}
if os.path.exists(BASE_DIR):
    for folder in sorted(os.listdir(BASE_DIR)):
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(folder_path):
            image_files = [
                os.path.join(folder_path, img)
                for img in sorted(os.listdir(folder_path))
                if img.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
            if image_files:
                categories[folder] = image_files


st.sidebar.header("📂 Select Analysis Category")

if not categories:
    st.sidebar.warning("⚠️ No image folders found in the 'images/' directory.")
else:
    category = st.sidebar.selectbox("Choose Category", list(categories.keys()))

   
    image_paths = categories[category]

    st.markdown(f"## 📊 {category}")

    
    cols = st.columns(2)  
    for i, img_path in enumerate(image_paths):
        col = cols[i % 2] 
        with col:
            try:
                image = Image.open(img_path)
                st.image(image, caption=os.path.basename(img_path), use_container_width=True)
            except Exception as e:
                st.error(f"Error loading image {img_path}: {e}")

