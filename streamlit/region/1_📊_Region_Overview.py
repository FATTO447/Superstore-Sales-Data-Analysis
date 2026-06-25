import streamlit as st
import plotly.express as px
from loader.upload import get_gold_table

st.subheader("📊 Region") 
st.title("📂 Region Overview Analysis")

df = get_gold_table("region_overview")

st.dataframe(df.head()) 

region_options = ["Show All Regions"] + list(df["Region"].unique()) 

selected_Region = st.sidebar.selectbox( 
    "Select Region to analyze", 
    options=region_options 
) 

metrics_options = [
    "Total_Sales", 
    "Avg_Sales", 
    "Total_Transactions", 
    "Avg_Profit", 
    "Total_Profit", 
    "Avg_Ship_Date", 
    "Total_Quantity"
]

selected_metrics = st.sidebar.multiselect(
    "Select metrics to compare", 
    options=metrics_options,
    default=["Total_Sales"] 
)

active_metric = selected_metrics[0] if selected_metrics else "Total_Sales"

if selected_Region == "Show All Regions": 
    filtered_df = df 
    chart_title = f"{active_metric.replace('_', ' ').title()} by Region" 
else: 
    filtered_df = df[df["Region"] == selected_Region] 
    chart_title = f"{active_metric.replace('_', ' ').title()} for: {selected_Region}" 

if not filtered_df.empty: 
    unit = " ($)" if "Sales" in active_metric or "Profit" in active_metric else ""
    
    fig = px.bar(
        filtered_df, 
        x="Region",    
        y=active_metric,
        hover_name="Region",  
        title=chart_title, 
        labels={active_metric: f"{active_metric.replace('_', ' ').title()}{unit}", "Region": "Region"}, 
        hover_data={"Region": False}, 
        color=active_metric, 
        color_continuous_scale="Viridis",
        text_auto=".2s"  
    )
    
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
else: 
    st.warning("There is no data for that Region")