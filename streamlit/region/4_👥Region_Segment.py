import streamlit as st
import plotly.express as px
from loader.upload import get_gold_table

st.subheader("📊 Region") 
st.title("📂 Region & Segment Analysis")

df = get_gold_table("region_segment")

st.dataframe(df.head()) 

region_options = ["Show All Regions"] + list(df["Region"].unique()) 
selected_region = st.sidebar.selectbox( 
    "Select Region to analyze", 
    options=region_options 
) 

segment_options = ["Show All Segments"] + list(df["Segment"].unique())
selected_segment = st.sidebar.selectbox(
    "Select Segment",
    options=segment_options
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

filtered_df = df.copy()

if selected_region != "Show All Regions":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_segment != "Show All Segments":
    filtered_df = filtered_df[filtered_df["Segment"] == selected_segment]

region_title_part = selected_region if selected_region != "Show All Regions" else "All Regions"
segment_title_part = selected_segment if selected_segment != "Show All Segments" else "All Segments"
chart_title = f"{active_metric.replace('_', ' ').title()} by Segment ({segment_title_part}) - {region_title_part}"

if not filtered_df.empty: 
    unit = " ($)" if "Sales" in active_metric or "Profit" in active_metric else ""
    
    x_axis = "Region" if selected_segment != "Show All Segments" and selected_region == "Show All Regions" else "Segment"
    
    fig = px.bar(
        filtered_df, 
        x=x_axis,    
        y=active_metric,
        hover_name="Region" if x_axis == "Segment" else "Segment",  
        title=chart_title, 
        labels={active_metric: f"{active_metric.replace('_', ' ').title()}{unit}", x_axis: x_axis}, 
        hover_data={"Region": True, "Segment": True}, 
        color=active_metric, 
        color_continuous_scale="Viridis",
        text_auto=".2s"  
    )
    
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, width="stretch")
else: 
    st.warning("⚠️ No data matches the selected filters. Try choosing different options.")