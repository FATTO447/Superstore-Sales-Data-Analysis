import streamlit as st 
import plotly.express as px 
from loader.upload import get_gold_table 

st.set_page_config(page_title="Region Analysis", layout="wide") 
st.title("🗺️ Region & Trend Analysis") 

st.markdown(
    """
### Welcome to the Region & Trend Analysis Dashboard! Explore sales performance, customer insights, and product trends across different regions to make informed business decisions. 📊 
"""
)
st.divider() 

df_year = get_gold_table("region_year") 
df_month = get_gold_table("region_month") 

tab1 , tab2 = st.tabs(["📊 Yearly Trend Analysis", "📈 Monthly Trend Analysis"]) 

with tab1 : 
    st.subheader("📊 Yearly Trend Analysis") 
    if not df_year.empty: 

        fig_year = px.line(
            df_year, 
            x="Year", 
            y="Total_Sales", 
            color="Region", 
            title="Yearly Sales Trend by Region", 
            labels={"Total_Sales": "Total Sales ($)", "Year": "Year"}, 
            hover_data={"Region": True, "Total_Sales": ":,.2f"}, 
        ) 
        fig_year.update_traces(mode="lines+markers", hovertemplate="<b>%{x}</b><br>Region: %{legendgroup}<br>Total Sales: $%{y:,.2f}<extra></extra>") 
        fig_year.update_layout(legend_title_text="Region", hovermode="x unified") 
        st.plotly_chart(fig_year, use_container_width=True) 

    else: 
        st.warning("No data available for Yearly Trend Analysis.") 

with tab2 : 
    st.subheader("📈 Monthly Trend Analysis") 
    if not df_month.empty: 

        fig_month = px.line(
            df_month, 
            x="Month", 
            y="Total_Sales", 
            color="Region", 
            title="Monthly Sales Trend by Region", 
            labels={"Total_Sales": "Total Sales ($)", "Month": "Month"}, 
            hover_data={"Region": True, "Total_Sales": ":,.2f"}, 
        ) 
        fig_month.update_traces(mode="lines+markers", hovertemplate="<b>%{x}</b><br>Region: %{legendgroup}<br>Total Sales: $%{y:,.2f}<extra></extra>") 
        fig_month.update_layout(legend_title_text="Region", hovermode="x unified") 
        st.plotly_chart(fig_month, use_container_width=True) 

    else: 
        st.warning("No data available for Monthly Trend Analysis.") 