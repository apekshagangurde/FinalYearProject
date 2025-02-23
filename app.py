import streamlit as st
import pandas as pd
import folium
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Import custom modules
from map_utils import load_places_data, display_map, display_places_table
from feed_back import feedback
from data import show_gis_data


# Load CSS for styling

# Load CSS for styling
st.markdown(
    """
    <style>
        /* Background Gradient */
        .main {
            background: linear-gradient(to right, #f0f2f5, #dfe4ea);
            padding: 20px;
            border-radius: 10px;
        }

        /* Sidebar Styling */
        .stSidebar {
            background-color: #2C3E50;  /* Deep Blue */
            color: white;
        }

        /* Titles and Headings */
        h1, h2, h3 {
            color: #2c3e50;  /* Dark Navy */
            font-family: 'Arial', sans-serif;
            text-align: center;
        }

        /* Metric Box Styling */
        .stMetric {
            background: #ECF0F1; /* Light Gray */
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #3498db; /* Blue Highlight */
            color: #2c3e50;
        }

        /* Buttons */
        .stButton>button {
            background-color: #3498db; /* Blue */
            color: white;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px;
        }

        /* Tables */
        .dataframe {
            background-color: #F7F9F9;
            border-radius: 10px;
        }

        /* Maps */
        .folium-map {
            border: 3px solid #34495E; /* Dark Gray Border */
            border-radius: 10px;
        }
         
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animated-header {
            color: #2C3E50;  /* Dark Navy */
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }

        .animated-text {
            color: #34495E;  /* Dark Gray */
            font-size: 18px;
            text-align: center;
            font-weight: 500;
            animation: fadeIn 1.5s ease-in-out;
        }

        .highlight {
            color: #3498db;  /* Blue Highlight */
            font-weight: bold;
        }
        @keyframes fadeInBounce {
            0% { opacity: 0; transform: translateY(-20px); }
            50% { opacity: 0.5; transform: translateY(5px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Heading Style */
        .animated-header {
            color: #1F618D;  /* Deep Blue */
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            font-family: 'Poppins', sans-serif;
            animation: fadeInBounce 1.5s ease-in-out;
            text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3); /* Soft Shadow */
        }

        /* Highlight Effect */
        .highlight {
            color: #E74C3C;  /* Bright Red */
            font-weight: bold;
        }
    
    </style>
    """,
    unsafe_allow_html=True
)
# Display Animated Header & Text


st.markdown('<style>h1 {text-align: center; color: #4CAF50;}</style>', unsafe_allow_html=True)
st.markdown('<h1 animated-header">Nashik Demographics & Restaurant Insights</h1>', unsafe_allow_html=True)
# Load Data Functions
@st.cache_data
def load_demographic_data():
    return pd.read_csv("Area Population - Sheet1.csv")

@st.cache_data
def load_restaurant_data():
    return pd.read_csv("Restaurants data - Sheet1 (1).csv")

# Load Data
df_demographics = load_demographic_data()
df_restaurants = load_restaurant_data()

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Demographics", "Restaurants", "Input Form", "Data",  "GIS"])

if page == "Home":
    st.markdown(
    '<p class="animated-text">This dashboard provides insights into <span class="highlight">population</span>, <span class="highlight">income levels</span>, and <span class="highlight">dominant age groups</span> in different areas of Nashik, along with <span class="highlight">restaurant insights</span>.</p>', 
    unsafe_allow_html=True
)
    # Key Metrics
    total_population = df_demographics["Population"].sum()
    avg_income = df_demographics["Income Level (Lakhs)"].mean()

    col1, col2 = st.columns(2)
    col1.metric("🌆 Total Population", f"{total_population:,}")
    col2.metric("💰 Avg. Income Level (Lakhs)", f"{avg_income:.2f}")

    # Population Distribution Chart
    st.subheader("👥 Population Distribution")
    fig = px.pie(df_demographics, values="Population", names="Area Name", title="Population by Area")
    st.plotly_chart(fig)

elif page == "Demographics":
    st.subheader("📊 Demographic Insights")
    
    # Filter by Area
    selected_area = st.selectbox("Select an Area", df_demographics["Area Name"].unique())

    # Show Area Details
    area_details = df_demographics[df_demographics["Area Name"] == selected_area].iloc[0]
    st.write(f"**🌆 Area:** {area_details['Area Name']}")
    st.write(f"**👨‍👩‍👧 Population:** {area_details['Population']:,}")
    st.write(f"**💰 Avg. Income Level:** ₹{area_details['Income Level (Lakhs)']} Lakh")
    st.write(f"**👥 Dominant Age Group:** {area_details['Dominant Age Group (Years)']}")

    # Show Map
    st.subheader("📍 Area Map")
    map_center = [19.9975, 73.7898]  # Nashik city center
    m = folium.Map(location=map_center, zoom_start=12, tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df_demographics.iterrows():
        popup_text = f"<b>{row['Area Name']}</b><br>Population: {row['Population']:,}<br>Income Level: ₹{row['Income Level (Lakhs)']} Lakh"
        folium.Marker([row.get("Latitude", 19.95), row.get("Longitude", 73.75)], popup=popup_text).add_to(marker_cluster)

    folium_static(m, width=800, height=500)

elif page == "Restaurants":
    st.subheader("🍽️ Restaurant Insights")

    # Sidebar Filters
    st.sidebar.subheader("Filters")
    min_rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 3.0)
    max_price = st.sidebar.slider("Maximum Budget (₹)", 100, 2000, 500)
    min_competitor_count = st.sidebar.slider("Minimum Competitor Count", 0, 300, 0)
    cuisine_type = st.sidebar.multiselect("Cuisine Type", df_restaurants["Cuisine"].unique())

    # Filter Data
    filtered_data = df_restaurants[(df_restaurants["Rating"] >= min_rating) & 
                                   (df_restaurants["Price"] <= max_price) & 
                                   (df_restaurants["Competitor_Count"] >= min_competitor_count)
                                   ]
    
    if cuisine_type:
        filtered_data = filtered_data[filtered_data["Cuisine"].isin(cuisine_type)]
    selected_restaurant = st.selectbox("Select a Restaurant", df_restaurants["Name"].unique())
    # Show restaurant details
    st.subheader(f"Details for {selected_restaurant}")
    restaurant_data = df_restaurants[df_restaurants["Name"] == selected_restaurant]
    
    if not restaurant_data.empty:
        for index, row in restaurant_data.iterrows():
            col1, col2, col3 = st.columns(3)
            col1.metric(label="💰 Price", value=f"₹{row['Price']}")
            col2.metric(label="⭐ Rating", value=row['Rating'])
            col3.metric(label="👥 Total Raters", value=row['Total Raters'])
            st.markdown(f"#### 📍 Location: [{row['Name']} on Google Maps]({row['Map LOcation']})")
            
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**🍛 Cuisine:** {row['Cuisine']}")
                st.write(f"**📌 Address:** {row['Address']}")
                st.write(f"**🕒 Timing:** {row['Timing']}")
            st.write(f"**Place ID:** {row['Place_id']}")
            
            with col2:
                st.write(f"**🌎 Latitude:** {row['Latitude']} | **Longitude:** {row['Longitude']}")
                st.write(f"**🔄 Competitor Count:** {row['Competitor_Count']}")
                st.write(f"**🏙️ Area Name:** {row['Area Name']}")
                st.write("---")

    else:
        st.write("No data available for the selected restaurant.")

    # Create Restaurant Map
    def create_map(data, selected_restaurant=None):
        map_center = [19.9975, 73.7898]
        m = folium.Map(location=map_center, zoom_start=13, tiles="cartodbpositron")
        marker_cluster = MarkerCluster().add_to(m)

        for _, row in data.iterrows():
            popup_text = (f"<b>{row['Name']}</b><br>"
                        f"Cuisine: {row['Cuisine']}<br>"
                        f"Price: ₹{row['Price']}<br>"
                        f"Rating: {row['Rating']} ({row['Total Raters']} ratings)<br>")
        
        # Check if this is the selected restaurant
            if selected_restaurant and row['Name'] == selected_restaurant:
                folium.Marker(
                    [row['Latitude'], row['Longitude']], 
                    popup=popup_text, 
                    icon=folium.Icon(color="red", icon="info-sign")
                ).add_to(m)
            else:
                folium.Marker(
                    [row['Latitude'], row['Longitude']], 
                    popup=popup_text
                ).add_to(marker_cluster)
    
        return m

# Display Map with highlighted restaurant
    st.subheader("📍 Restaurant Locations with Highlighted Selection")
    folium_static(create_map(df_restaurants, selected_restaurant), width=700, height=450)
    # Key Metrics
    if not filtered_data.empty:
        st.subheader("📊 Key Insights")
        selected_restaurant = st.selectbox("Select a Restaurant", filtered_data["Name"])
        details = filtered_data[filtered_data["Name"] == selected_restaurant].iloc[0]

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("⭐ Rating", f"{details['Rating']}")
        col2.metric("🏪 Competitor Count", f"{details['Competitor_Count']} nearby")
        col3.metric("🏙️ Population Density", "1200/sq km")
        col4.metric("💰 Projected Revenue", "₹50,000")
        col5.metric("🍽️ Avg. Meal Price", f"₹{details['Price']}")

        # Competitor Insights
        with st.expander("📈 Competitor Insights"):
            fig = px.bar(filtered_data, x='Name', y='Competitor_Count', title="Competitor Density by Restaurant")
            st.plotly_chart(fig)

        # Revenue Forecast
        with st.expander("📊 Revenue Forecast"):
            fig = go.Figure(go.Scatter(x=filtered_data['Name'], y=filtered_data['Price'], mode='lines+markers'))
            fig.update_layout(title='Projected Revenue Trend', xaxis_title='Restaurant', yaxis_title='Revenue (₹)')
            st.plotly_chart(fig)

elif page == "Input Form":
    feedback()

elif page == "Data":
    show_gis_data()



elif page == "GIS":
    df_places = load_places_data()
    display_map(df_places)
    display_places_table(df_places)
