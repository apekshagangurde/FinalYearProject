import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Custom CSS for sidebar and layout
st.markdown("""
    <style>
        /* Sidebar Styling */
        .css-1d391kg {
            background-color: #2c3e50 !important; /* Dark background */
            color: white;
        }
        
        .css-1l02zno {
            background-color: #2c3e50 !important; /* Dark background */
            color: white;
        }

        /* Main Content Styling */
        .css-1avcm0n {
            background-color: #ecf0f1 !important; /* Light background */
        }

        /* Text and Title Colors */
        h1, h2, h3, h4 {
            color: #2980b9; /* Blue for titles */
        }

        /* Button Styles */
        .stButton>button {
            background-color: #e67e22 !important; /* Button color */
            color: white !important;
            border-radius: 8px;
            font-size: 16px;
        }

        /* Custom KPI Panel */
        .custom-box {
            background-color: #34495e; /* Dark box for KPIs */
            padding: 15px;
            border-radius: 10px;
            color: white;
            margin-bottom: 10px;
        }

        /* Map Border */
        .leaflet-container {
            border-radius: 10px;
        }

        /* Logo Style */
        .logo {
            width: 200px; /* Adjust logo width */
            margin-bottom: 20px;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("./images/logo.png", use_column_width=True, output_format='PNG', caption="GeoInsight RetailSite")  # Logo Path
st.sidebar.title("GeoInsight RetailSite")
st.sidebar.markdown("### Geospatial Market Analysis Tool")
menu_options = st.sidebar.radio("Navigation", ["Retail Location Map", "Location Analytics", "Competitor Insights", "Real Estate", "Business Forecast", "Strategies"])

# Displaying title based on selection
st.title("Retail Location Analysis")

# Folium map generation for geo-analysis
st.subheader("Interactive Map of Retail Locations")
map_center = [40.7128, -74.0060]  # New York City
m = folium.Map(location=map_center, zoom_start=14)

# Add example markers to mimic analysis points
folium.Marker(location=[40.7128, -74.0060], popup="Primary Retail Location", icon=folium.Icon(color="blue")).add_to(m)
folium.Marker(location=[40.730610, -73.935242], popup="Secondary Location", icon=folium.Icon(color="orange")).add_to(m)

# Display the map in Streamlit using folium
st_folium(m, width=700, height=500)

# KPI Display similar to right-hand panel in image
st.subheader("Key Metrics and Business Insights")

# Dummy data for the KPI display with icons
kpi_data = {
    "Metric": ["Population Growth", "Income Level", "Business Density", "Risk Factors"],
    "Value": [53.4, 34.7, 50.9, 41.8],
    "Icon": ["🔼", "💰", "🏢", "⚠️"]
}
kpi_df = pd.DataFrame(kpi_data)

# Display KPIs
for idx, row in kpi_df.iterrows():
    st.markdown(f"""
        <div class="custom-box">
            <h4>{row['Icon']} {row['Metric']}</h4>
            <p><b>{row['Value']}%</b></p>
        </div>
    """, unsafe_allow_html=True)

# Advanced interactive charts using Plotly for insights and analytics
st.subheader("Business Trends Over Time")

# Example time-series data (to be replaced with actual dataset)
time_series_data = pd.DataFrame({
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Revenue": [50000, 55000, 52000, 60000, 65000],
    "Growth": [2.4, 3.1, 2.8, 4.0, 4.5]
})

# Line chart for revenue growth over the years
fig = px.line(time_series_data, x="Year", y="Revenue", title="Yearly Revenue Growth", markers=True)
st.plotly_chart(fig)

# Download button to export data
st.subheader("Download Business Report")
st.download_button("Download Report", "Sample Report Data", file_name="business_report.csv", mime="text/csv")

# Adding tooltips or further interaction (This can be expanded for overlays)
st.sidebar.markdown("### Filter Analysis")
st.sidebar.slider("Select Radius (km)", 0, 50, 10)
