import streamlit as st
import os
import importlib.util
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("🗺️ Region Deep-Dive Analysis")

REGION_DIR = "region"

if os.path.exists(REGION_DIR):
    page_files = [f for f in os.listdir(REGION_DIR) if f.endswith(".py") and f != "__init__.py"]
else:
    page_files = []
    st.error(f"Folder '{REGION_DIR}' not found.")

pages_dict = {}
for file in page_files:
    clean_name = file.replace(".py", "").replace("_", " ").title()
    pages_dict[clean_name] = file

if pages_dict:
    selected_sub_page = st.sidebar.radio(
        "📊 Choose a page ", 
        options=list(pages_dict.keys())
    )
    selected_file = pages_dict[selected_sub_page]

    file_path = os.path.join(REGION_DIR, selected_file)
    spec = importlib.util.spec_from_file_location("sub_module", file_path)
    sub_module = importlib.util.module_from_spec(spec)
    
    spec.loader.exec_module(sub_module)
else:
    st.info("There are no pages in this folder.")