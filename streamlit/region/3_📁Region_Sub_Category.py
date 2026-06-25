import streamlit as st
import plotly.express as px
from loader.upload import get_gold_table

st.subheader("📊 Region") 
st.title("📂 Region & Sub_Category Analysis")

df = get_gold_table("region_sub_category")

st.dataframe(df.head()) 

region_options = ["Show All Regions"] + list(df["Region"].unique()) 
selected_Region = st.sidebar.selectbox( 
    "Select Region to analyze", 
    options=region_options 
) 

sub_category_options = ["Show All Sub_Categories"] + list(df["Sub_Category"].unique())
selected_sub_category = st.sidebar.selectbox(
    "Select Sub_Category",
    options=sub_category_options
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

if selected_Region != "Show All Regions":
    filtered_df = filtered_df[filtered_df["Region"] == selected_Region]

if selected_sub_category != "Show All Sub_Categories":
    filtered_df = filtered_df[filtered_df["Sub_Category"] == selected_sub_category]

region_title_part = selected_Region if selected_Region != "Show All Regions" else "All Regions"
category_title_part = selected_sub_category if selected_sub_category != "Show All Categories" else "All Categories"
chart_title = f"{active_metric.replace('_', ' ').title()} by Category ({category_title_part}) - {region_title_part}"

if not filtered_df.empty: 
    unit = " ($)" if "Sales" in active_metric or "Profit" in active_metric else ""
    
    x_axis = "Region" if selected_sub_category != "Show All Sub_Category" and selected_Region == "Show All Regions" else "Sub_Category"
    
    fig = px.bar(
        filtered_df, 
        x=x_axis,    
        y=active_metric,
        hover_name="Region" if x_axis == "Sub_Category" else "Sub_Category",  
        title=chart_title, 
        labels={active_metric: f"{active_metric.replace('_', ' ').title()}{unit}", x_axis: x_axis}, 
        hover_data={"Region": True, "Sub_Category": True}, 
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