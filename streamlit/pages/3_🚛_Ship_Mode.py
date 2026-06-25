import pandas as pd 
import streamlit as st 
import plotly.express as px 
from loader.upload import get_gold_table 

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide") 
st.title(" Superstore Sales BY Ship Mode Dashboard") 

st.markdown("""
Welcome to the Superstore Sales Dashboard! Explore sales performance, customer insights, and logistics trends across different shipping modes to make informed business decisions.
""")

df_overview = get_gold_table("ship_mode_overview") 
df_sub_category = get_gold_table("ship_mode_sub_category") 
df_category = get_gold_table("ship_mode_category") 
df_segment = get_gold_table("ship_mode_segment") 

metric_dict = {
    "Total_Sales": "Total Sales"
}

ship_mode_options = ["Show All Ship Modes"] + list(df_overview['Ship_Mode'].unique()) 

selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode to analyze", 
    options=ship_mode_options 
) 

selected_metric_display = st.sidebar.selectbox( 
    "Select metric to compare", 
    options=list(metric_dict.values()) 
)

selected_compare_option = [k for k, v in metric_dict.items() if v == selected_metric_display][0]

if selected_ship_mode == "Show All Ship Modes":
    filtered_overview = df_overview
    filtered_category = df_category
    filtered_sub = df_sub_category
    filtered_segment = df_segment
    chart_title = f"{selected_metric_display} Analysis"
    color_by = "Ship_Mode" 
    barmode_type = "group"
else:
    filtered_overview = df_overview[df_overview["Ship_Mode"] == selected_ship_mode]
    filtered_category = df_category[df_category["Ship_Mode"] == selected_ship_mode]
    filtered_sub = df_sub_category[df_sub_category["Ship_Mode"] == selected_ship_mode]
    filtered_segment = df_segment[df_segment["Ship_Mode"] == selected_ship_mode]
    chart_title = f"{selected_metric_display} for: {selected_ship_mode}"
    color_by = selected_compare_option
    barmode_type = "relative"

unit = " ($)" if selected_compare_option in ["Total_Sales"] else " (Days)"

st.subheader(f"📊 {chart_title}") 

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Category", "Sub-Category", "Segment"]) 

# ─── Tab 1: Overview ───
with tab1: 
    if not filtered_overview.empty: 
        fig1 = px.bar(
            filtered_overview, 
            x="Ship_Mode",    
            y=selected_compare_option, 
            title=f"{selected_metric_display} by Ship Mode", 
            labels={selected_compare_option: f"{selected_metric_display}{unit}", "Ship_Mode": "Ship Mode"}, 
            color=selected_compare_option, 
            color_continuous_scale="Blues",
            text_auto=".2s" if selected_compare_option != "Avg_Days_to_Ship" else ".1f" 
        ) 
        fig1.update_layout(title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)') 
        st.plotly_chart(fig1, width='stretch') 
    else:
        st.warning("No data available.") 

# ─── Tab 2: Category ───
with tab2: 
    if not filtered_category.empty: 
        fig2 = px.bar(
            filtered_category, 
            x="Category",    
            y=selected_compare_option, 
            color=color_by, 
            barmode=barmode_type,
            title=f"{selected_metric_display} by Product Category", 
            labels={selected_compare_option: f"{selected_metric_display}{unit}"}, 
            color_continuous_scale="Blues" if color_by == selected_compare_option else None,
            text_auto=".2s" if selected_compare_option != "Avg_Days_to_Ship" else ".1f" 
        ) 
        fig2.update_layout(title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)') 
        st.plotly_chart(fig2, width='stretch') 
    else:
        st.warning("No data available.") 

# ─── Tab 3: Sub-Category ───
with tab3: 
    if not filtered_sub.empty: 
        fig3 = px.bar(
            filtered_sub, 
            x="Sub_Category",    
            y=selected_compare_option, 
            color=color_by, 
            barmode=barmode_type,
            title=f"{selected_metric_display} by Sub-Category", 
            labels={selected_compare_option: f"{selected_metric_display}{unit}", "Sub_Category": "Sub-Category"}, 
            color_continuous_scale="Blues" if color_by == selected_compare_option else None,
            text_auto=".2s" if selected_compare_option != "Avg_Days_to_Ship" else ".1f" 
        ) 
        fig3.update_layout(title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)') 
        st.plotly_chart(fig3, width='stretch') 
    else:
        st.warning("No data available.") 

# ─── Tab 4: Segment ───
with tab4: 
    if not filtered_segment.empty: 
        fig4 = px.bar(
            filtered_segment, 
            x="Segment",    
            y=selected_compare_option, 
            color=color_by, 
            barmode=barmode_type,
            title=f"{selected_metric_display} by Customer Segment", 
            labels={selected_compare_option: f"{selected_metric_display}{unit}"}, 
            color_continuous_scale="Blues" if color_by == selected_compare_option else None,
            text_auto=".2s" if selected_compare_option != "Avg_Days_to_Ship" else ".1f" 
        ) 
        fig4.update_layout(title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)') 
        st.plotly_chart(fig4, width='stretch') 
    else:
        st.warning("No data available.")