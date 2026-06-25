import pandas as pd 
import streamlit as st 
import plotly.express as px 
from loader.upload import get_gold_table    

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide") 
st.title("Superstore Sales Dashboard") 
st.markdown("Welcome to the Superstore Sales Dashboard! Explore sales performance, customer insights, and product trends to make informed business decisions.") 

st.subheader("📊 Loss Product Analysis") 
st.sidebar.header("Filters") 

df_all = get_gold_table("loss_product_overview") 

if not df_all.empty:
    df_all['Short_Product_Name'] = df_all['Product_Name'].apply(lambda x: str(x)[:25] + '...' if len(str(x)) > 25 else str(x))

    product_options = ["Show All Products"] + list(df_all["Product_Name"].unique()) 

    selected_product = st.sidebar.selectbox(
        "Select product to analyze", 
        options=product_options 
    )

    if selected_product == "Show All Products":
        filtered_df = df_all.head(10) 
        chart_title = "Top 10 Most Unprofitable Products (Highest Losses)"
    else:
        filtered_df = df_all[df_all["Product_Name"] == selected_product]
        chart_title = f"Profitability Performance for: {selected_product}"

    if not filtered_df.empty:
        fig = px.bar(
            filtered_df, 
            x="Short_Product_Name",    
            y="Total_Profit", 
            hover_name="Product_Name",  
            title=chart_title, 
            labels={"Total_Profit": "Net Profit ($)", "Short_Product_Name": "Product Name", "Total_Sales": "Total Sales ($)"}, 
            hover_data={"Product_Name": False, "Short_Product_Name": False, "Total_Sales": True}, 
            color="Total_Profit", 
            color_continuous_scale="Reds_r", 
            text_auto=".2s"
        ) 

        fig.update_layout(
            xaxis_tickangle=-30, 
            margin=dict(l=50, r=50, t=50, b=100), 
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, width='stretch')
    else:
        st.warning("There is no data for that product")
else:
    st.warning("⚠️ The dataset is empty. Please check the loader or the CSV file.")