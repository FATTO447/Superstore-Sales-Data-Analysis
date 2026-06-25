import pandas as pd
import streamlit as st
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, ".." , "data") 
REGION_DIR = os.path.join(DATA_DIR, "region") 
CITY_DIR = os.path.join(DATA_DIR, "city") 
SHIP_MODE_DIR = os.path.join(DATA_DIR, "ship_mode") 
LOSS_PRODUCT_DIR = os.path.join(DATA_DIR, "loss_product") 

CSV_TABLES = {

    # ── City pages ───────────────────────────────────────────
    "city_overview":
        os.path.join(CITY_DIR, "city_py.csv"),
    "city_category":
        os.path.join(CITY_DIR, "city_category_py.csv"),
    "city_sub_category":
        os.path.join(CITY_DIR, "city_sub_category_py.csv"),

    # ── Region pages ─────────────────────────────────────────
    "region_overview":
        os.path.join(REGION_DIR, "region_year_py.csv"),
    "region_month":
        os.path.join(REGION_DIR, "region_month_py.csv"),
    "region_year" : 
        os.path.join(REGION_DIR, "region_year_py.csv"),
    "region_category":
        os.path.join(REGION_DIR, "region_category_py.csv"),
    "region_sub_category":
        os.path.join(REGION_DIR, "region_sub_category_py.csv"),
    "region_segment":
        os.path.join(REGION_DIR, "region_segment_py.csv"),

    # ── Ship Mode pages ──────────────────────────────────────
    "ship_mode_overview":
        os.path.join(SHIP_MODE_DIR, "ship_mode_py.csv"),
    "ship_mode_category":
        os.path.join(SHIP_MODE_DIR, "category_ship_mode_py.csv"),
    "ship_mode_sub_category":
        os.path.join(SHIP_MODE_DIR, "sub_category_py.csv"),
    "ship_mode_segment":
        os.path.join(SHIP_MODE_DIR, "segment_py.csv") ,

    # ── Loss Product pages ───────────────────────────────────── 
    "loss_product_overview": 
        os.path.join(LOSS_PRODUCT_DIR, "loss_product_py.csv") 
}


@st.cache_data 

def get_gold_table(table_name: str) -> pd.DataFrame:
    """
    Load a gold table from the data directory based on the provided table name.

    Args:
        table_name (str): The name of the gold table to load. 
    """ 

    if table_name not in CSV_TABLES:
        raise ValueError(f"Table '{table_name}' not found in CSV_TABLES.")
    
    file_path = CSV_TABLES[table_name]
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    
    df = pd.read_csv(file_path)
    return df 
