import streamlit as st
import pandas as pd 
import plotly.express as px
from loader.upload import get_gold_table 

st.set_page_config(page_title="City Analysis Dashboard", layout="wide") 
st.title("City Analysis Dashboard")
st.markdown("Welcome to the City Analysis Dashboard! Explore sales performance across different cities, states and sub-categories to make informed business decisions.") 

df_overview = get_gold_table("city_overview") 
df_sub_category = get_gold_table("city_sub_category")
df_category = get_gold_table("city_category")

selected_tab = st.radio(
    "Choose Analysis View:", 
    ["📊 City Overview", "📁 Sub-Category Analysis", "📂 Category Analysis"], 
    horizontal=True,
    label_visibility="collapsed" 
)

# ------------------- Tab 1: City Overview -----------------
if selected_tab == "📊 City Overview": 
    st.subheader("📊 City Sales Analysis Overview") 
    
    st.sidebar.markdown("### ℹ️ Quick Info")
    st.sidebar.info("This is a high-level overview of the Top 10 cities by sales. Switch tabs above to filter by Category or Sub-Category.")
    city_options_overview = ["Show All Cities"] + list(df_overview["City"].unique()) 
    selected_city_overview = st.sidebar.selectbox(
        "Select City (Overview)",
        options=city_options_overview
    ) 

    top_cities = df_overview.copy() 
    if filtered_city := selected_city_overview if selected_city_overview != "Show All Cities" else None: 
        top_cities = top_cities[top_cities["City"] == filtered_city] 
    else: 
        top_cities = top_cities.sort_values(by="Total_Sales", ascending=False).head(10) 

    if not top_cities.empty: 
        fig_overview = px.bar( 
            top_cities, 
            x="City", 
            y="Total_Sales", 
            hover_name="City",  
            title="Top 10 Cities with Highest Sales Overall", 
            height=600,
            labels={"Total_Sales": "Total Sales ($)", "City": "City"}, 
            hover_data={"City": False, "City": False, "Total_Sales": ":$.2f", "Total_Profit": ":$.2f"}, 
            color="Total_Sales", 
            color_continuous_scale="Viridis",
            text_auto=".2s" 
        ) 

        fig_overview.update_layout( 
            xaxis_title="City", 
            yaxis_title="Total Sales ($)", 
            title_x=0.5, 
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)', 
            font=dict(size=12) 
        ) 

        st.plotly_chart(fig_overview, use_container_width=True) 
    else : 
        st.warning("There is no data for that city")

# ----------------- Tab 2: Sub-Category -----------------
elif selected_tab == "📁 Sub-Category Analysis": 
    st.subheader("📊 City Sales Analysis by Sub Category")
    
    st.sidebar.header("⚙️ Sub-Category Filters") 
    city_options = ["Show All Cities"] + list(df_sub_category["City"].unique()) 
    sub_category_options = ["Show All Sub Category"] + list(df_sub_category['Sub_Category'].unique()) 

    selected_city = st.sidebar.selectbox( 
        "Select City (Sub-Category View)", 
        options=city_options,
        key="city_sub_key" 
    ) 
    selected_city_sub_category = st.sidebar.selectbox(
        "Select Sub Category", 
        options=sub_category_options,
        key="sub_cat_key"
    ) 

    if selected_city == "Show All Cities" and selected_city_sub_category == "Show All Sub Category": 
        filtered_df = df_sub_category.head(10) 
        chart_title = "Top 10 Cities with Highest Sales" 
    elif selected_city != "Show All Cities" and selected_city_sub_category == "Show All Sub Category": 
        filtered_df = df_sub_category[df_sub_category["City"] == selected_city] 
        chart_title = f"Sales Performance for: {selected_city}" 
    elif selected_city == "Show All Cities" and selected_city_sub_category != "Show All Sub Category": 
        filtered_df = df_sub_category[df_sub_category["Sub_Category"] == selected_city_sub_category] 
        chart_title = f"Sales Performance for Sub Category: {selected_city_sub_category}"
    else : 
        filtered_df = df_sub_category[(df_sub_category["City"] == selected_city) & (df_sub_category["Sub_Category"] == selected_city_sub_category)] 
        chart_title = f"Sales Performance for: {selected_city} - Sub Category: {selected_city_sub_category}" 

    if not filtered_df.empty: 
        fig = px.bar( 
            filtered_df, 
            x="City", 
            y="Total_Sales", 
            hover_name="City",  
            title=chart_title, 
            height=600,
            labels={
                "Total_Sales": "Total Sales ($)", 
                "City": "City",
                "Sub_Category": "Sub Category",
                "Total_Profit": "Total Profit ($)"
            }, 
            hover_data={
                "City": False, 
                "City": False,
                "Sub_Category": True,
                "Total_Sales": ":$.2f",  
                "Total_Profit": ":$.2f"   
            }, 
            color="Total_Sales", 
            color_continuous_scale="Blues",
            text_auto=".2s"
        ) 

        fig.update_layout( 
            xaxis_title="City", 
            yaxis_title="Total Sales ($)", 
            title_x=0.5, 
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)', 
            font=dict(size=12) 
        ) 
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("There is no data for that city or sub category")

# ----------------- Tab 3: Category -----------------
elif selected_tab == "📂 Category Analysis": 
    st.subheader("📊 City Sales Analysis by Category")
    
    st.sidebar.header("⚙️ Category Filters") 
    city_options_cat = ['Show All Cities'] + list(df_category["City"].unique()) 
    category_options = ['Show All Categories'] + list(df_category["Category"].unique()) 

    selected_city_category = st.sidebar.selectbox( 
        "Select City (Category View)", 
        options=city_options_cat,
        key="city_cat_key"
    ) 
    selected_category = st.sidebar.selectbox( 
        "Select Category",  
        options=category_options,
        key="cat_key"
    ) 

    if selected_city_category == "Show All Cities" and selected_category == "Show All Categories":
        filtered_df_cat = df_category.head(10) 
        chart_title_cat = "Top 10 Cities with Highest Sales"
    elif selected_city_category != "Show All Cities" and selected_category == "Show All Categories":
        filtered_df_cat = df_category[df_category["City"] == selected_city_category] 
        chart_title_cat = f"Sales Performance for: {selected_city_category}"
    elif selected_city_category == "Show All Cities" and selected_category != "Show All Categories": 
        filtered_df_cat = df_category[df_category["Category"] == selected_category] 
        chart_title_cat = f"Sales Performance for Category: {selected_category}"
    else : 
        filtered_df_cat = df_category[(df_category["City"] == selected_city_category) & (df_category["Category"] == selected_category)] 
        chart_title_cat = f"Sales Performance for: {selected_city_category} - Category: {selected_category}"
        
    if not filtered_df_cat.empty:
        fig_cat = px.bar(
            filtered_df_cat, 
            x="City", 
            y="Total_Sales", 
            hover_name="City",  
            title=chart_title_cat, 
            height=600,
            labels={
                "Total_Sales": "Total Sales ($)", 
                "Short_City": "City",
                "Category": "Category",
                "Total_Profit": "Total Profit ($)"
            }, 
            hover_data={
                "City": False, 
                "City": False,
                "Category": True,
                "Total_Sales": ":$.2f",  
                "Total_Profit": ":$.2f"   
            }, 
            color="Total_Sales", 
            color_continuous_scale="Greens", 
            text_auto=".2s" 
        )
        
        fig_cat.update_layout( 
            xaxis_title="City", 
            yaxis_title="Total Sales ($)", 
            title_x=0.5, 
            plot_bgcolor='rgba(0,0,0,0)', 
            paper_bgcolor='rgba(0,0,0,0)', 
            font=dict(size=12) 
        ) 
        st.plotly_chart(fig_cat, use_container_width=True) 
    else: 
        st.warning("There is no data for that selection")