import streamlit as st
import pandas as pd
import folium
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
from feed_back import feedback
from data import show_gis_data
from tree import show_decision_tree
# Set page configuration (This should be the first Streamlit command)


# Set page configuration


# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()  # Call the function to load CSS

# Add a tagged heading for CSS styling or animation
st.markdown('<h1 class="animated-heading">Welcome to GeoInsight Restaurant Analysis</h1>', unsafe_allow_html=True)

# Continue with your app layout and content


page = st.sidebar.selectbox("Select Page", ["Home", " Input form","data" ,"tree"])
if page == "Home":
   
# Sample Data - Replace this with actual restaurant data
    def load_sample_data():
        restaurant_data = pd.DataFrame({
            'Location': ['Restaurant 1', 'Restaurant 2', 'Restaurant 3'],
            'Latitude': [19.9975, 19.9615, 19.9365],
            'Longitude': [73.7898, 73.8098, 73.8398],
            'Foot Traffic': [150, 220, 180],
            'Competitors': [2, 4, 3],
            'Population Density': [1200, 1400, 1300],
            'Projected Revenue': [45000, 62000, 58000],
            'Average Meal Price': [150, 200, 175]
        })
        return restaurant_data

# Function to create a Folium Map showing restaurant locations
    def create_map(data):
        map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
        m = folium.Map(location=map_center, zoom_start=12)
        
        for index, row in data.iterrows():
            popup_text = (f"Restaurant: {row['Location']}<br>"
                        f"Foot Traffic: {row['Foot Traffic']} people/day<br>"
                        f"Competitors: {row['Competitors']} nearby<br>"
                        f"Population Density: {row['Population Density']} people/sq km<br>"
                        f"Projected Revenue: ${row['Projected Revenue']}<br>"
                        f"Average Meal Price: ${row['Average Meal Price']}")
            folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(m)
        
        return m

# Sidebar with Filters
    st.sidebar.header("Filters")
    city = st.sidebar.selectbox("City", ["Nashik"], index=0)

# Area dropdown for locations within Nashik
    area = st.sidebar.selectbox("Select Area", ["Unvadi", "Govindnagar", "Panchavati", "Gangapur", "College Road", "Indiranagar"])
    date_range = st.sidebar.date_input("Select Date Range")
    category = st.sidebar.multiselect("Restaurant Category", ["Fast Food", "Fine Dining", "Cafes", "Street Food"])
    competitor_filter = st.sidebar.slider("Competitor Filter", 0, 10, 5)
    foot_traffic_filter = st.sidebar.slider("Foot Traffic Range", 100, 500, (200, 400))
    population_density_filter = st.sidebar.slider("Population Density", 500, 2000, (1000, 1500))
    average_meal_price_filter = st.sidebar.slider("Average Meal Price", 100, 300, (150, 250))

    # Main Area: Header
    

    # Tabs for Dashboard Sections
    tabs = st.tabs(["Location Analysis", "Competitor Insights", "Demographic Data", "Revenue Forecast", "Reports", "Settings"])

    # Sample data loaded
    restaurant_data = load_sample_data()

    # Tab 1: Location Analysis
    with tabs[0]:
        st.subheader("Restaurant Location Map")

        # Create and display the map
        restaurant_map = create_map(restaurant_data)
        folium_static(restaurant_map, width=700, height=450)

        # Key Metrics Section
        st.subheader("Key Metrics")
        selected_location = st.selectbox("Select Restaurant", restaurant_data["Location"])
        location_data = restaurant_data[restaurant_data["Location"] == selected_location].iloc[0]
        
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Restaurant Score", f"{location_data['Foot Traffic'] + location_data['Competitors']}")
        col2.metric("Competitor Count", f"{location_data['Competitors']} nearby")
        col3.metric("Population Density", f"{location_data['Population Density']}/sq km")
        col4.metric("Projected Revenue", f"${location_data['Projected Revenue']}")
        col5.metric("Average Meal Price", f"${location_data['Average Meal Price']}")

    # Tab 2: Competitor Insights
    with tabs[1]:
        st.subheader("Competitor Insights")
        fig = px.bar(restaurant_data, x='Location', y='Competitors', title="Competitor Density by Restaurant")
        st.plotly_chart(fig)

    # Tab 3: Demographic Data
    with tabs[2]:
        st.subheader("Demographic Data")
        fig = px.pie(restaurant_data, names='Location', values='Population Density', title="Population Density Breakdown")
        st.plotly_chart(fig)

    # Tab 4: Revenue Forecast
    with tabs[3]:
        st.subheader("Revenue Forecast")
        fig = go.Figure(go.Scatter(x=restaurant_data['Location'], y=restaurant_data['Projected Revenue'],
                                mode='lines+markers', name='Projected Revenue'))
        fig.update_layout(title='Projected Revenue Trend by Restaurant', xaxis_title='Restaurant', yaxis_title='Revenue ($)')
        st.plotly_chart(fig)

    # Tab 5: Reports and Export
    with tabs[4]:
        st.subheader("Generate and Download Reports")
        report_type = st.selectbox("Select Report Type", ["PDF", "Excel"])
        if st.button("Download Report"):
            st.write(f"Generating {report_type} report... (placeholder for report generation logic)")
    

    # Bottom Section: Run Analysis & Compare Locations
    st.sidebar.header("Actions")
    if st.sidebar.button("Run Analysis"):
        st.sidebar.success("Analysis complete! (Placeholder for analysis execution)")

    if st.sidebar.button("Compare Locations"):
        st.sidebar.info("Comparing restaurants... (Placeholder for comparison logic)")
elif page == " Input form":
    
    feedback()  # Call your form function to display it
    
#elif page == "feedback":
   # feedback()  
    
elif page == "data":
    show_gis_data()
elif page == "tree":
    show_decision_tree()