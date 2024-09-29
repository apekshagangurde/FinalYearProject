import streamlit as st
import pandas as pd



# Sample GIS Data with additional attributes
gis_data = {
    "Location ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Latitude": [18.5204, 18.5205, 18.5206, 18.5207, 18.5208, 18.5209, 18.5210, 18.5211, 18.5212, 18.5213],
    "Longitude": [73.8567, 73.8568, 73.8569, 73.8570, 73.8571, 73.8572, 73.8573, 73.8574, 73.8575, 73.8576],
    "Roads": ["Main St", "Second St", "Third St", "Fourth St", "Fifth St", "Sixth St", "Seventh St", "Eighth St", "Ninth St", "Tenth St"],
    "Land Use": ["Commercial", "Residential", "Industrial", "Commercial", "Residential", "Industrial", "Commercial", "Residential", "Industrial", "Commercial"],
    "Zoning Regulations": ["Retail", "Residential", "Industrial", "Mixed-Use", "Residential", "Industrial", "Retail", "Mixed-Use", "Residential", "Commercial"],  # Necessary for understanding restrictions on land use
    "Nearby Facilities": ["Park", "School", "Hospital", "Grocery Store", "Gym", "Library", "Restaurant", "Cafe", "Pharmacy", "Community Center"]  # Important to attract customers
}

# Sample Demographic Data with additional attributes
demographic_data = {
    "Location ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Population Size": [1000, 1200, 800, 1500, 700, 900, 1100, 1300, 1600, 1400],
    "Average Income": [30000, 32000, 28000, 35000, 27000, 29000, 31000, 33000, 34000, 36000],
    "Predominant Age Group": ["18-25", "26-35", "36-45", "18-25", "26-35", "36-45", "18-25", "26-35", "36-45", "18-25"],
    "Household Size": [3, 4, 2, 5, 2, 3, 4, 3, 4, 3],  # Necessary to understand family dynamics and dining preferences
    "Ethnic Diversity": ["Low", "Medium", "High", "Medium", "Low", "Medium", "High", "Medium", "High", "Low"]  # Helps in tailoring marketing and menu options
}

# Sample Competitor Data with additional attributes
competitor_data = {
    "Competitor ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Restaurant Name": ["Dine Fine", "Taste Buds", "Yummy Corner", "Food Palace", "Culinary Haven", "Flavors Hub", "Epic Eats", "Savory Stop", "Delicious Bites", "Gourmet Garden"],
    "Location ID": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Customer Reviews": [150, 200, 120, 300, 250, 180, 220, 140, 160, 280],
    "Average Rating": [4.5, 4.0, 4.2, 4.7, 4.3, 4.6, 4.1, 4.4, 4.0, 4.8],
    "Cuisine Type": ["Italian", "Mexican", "Indian", "Chinese", "Thai", "Vegan", "Seafood", "American", "Japanese", "Mediterranean"],  # Necessary to analyze competition in the same cuisine category
    "Price Range": ["$$", "$$", "$$$", "$$", "$$", "$", "$$", "$$$", "$$", "$$$$"]  # Important to set competitive pricing
}

# Sample Market Trends Data with additional attributes
market_trends_data = {
    "Trend ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Popular Cuisine": ["Italian", "Mexican", "Indian", "Chinese", "Thai", "Vegan", "Seafood", "American", "Japanese", "Mediterranean"],
    "Seasonality": ["Year-round", "Summer", "Winter", "Year-round", "Spring", "Year-round", "Fall", "Year-round", "Summer", "Winter"],
    "Emerging Trends": ["Plant-Based", "Organic", "Sustainable", "Gluten-Free", "Locally Sourced", "Craft Beverages", "Ethnic Fusion", "Comfort Food", "Meal Kits", "Home Delivery"],  # Necessary for adapting business strategy to market changes
    "Consumer Preferences": ["Healthy", "Affordable", "Quick Service", "Dining Experience", "Takeout", "Family-Friendly", "Luxury Dining", "Special Diets", "Local Ingredients", "International Flavors"]  # Helps in aligning offerings with customer desires
}

# Function to show GIS data
def show_gis_data():
    
    st.title("Restaurant Location Analysis")
   
    # Show GIS Data
    st.header("GIS Data")
    gis_df = pd.DataFrame(gis_data)
    st.write(gis_df)

    # Show Demographic Data
    st.header("Demographic Data")
    demographic_df = pd.DataFrame(demographic_data)
    st.write(demographic_df)

    # Show Competitor Data
    st.header("Competitor Data")
    competitor_df = pd.DataFrame(competitor_data)
    st.write(competitor_df)

    # Show Market Trends Data
    st.header("Market Trends")
    market_trends_df = pd.DataFrame(market_trends_data)
    st.write(market_trends_df)
    st.write("""
### How the Decision Tree Works
- **Population Density**: This is the first decision point. If the population density is high, it may indicate more potential customers.
- **Competitor Density**: If the competitor density is low, it suggests less competition, making it favorable to open a new restaurant.
- **Market Trend Favorability**: If the market trend is favorable (e.g., demand for healthy options), it adds to the likelihood of success.
- **Accessibility Score**: A higher score indicates better accessibility, further increasing the chances of success.
""")

# Call the function to display the data
if __name__ == "__main__":
    show_gis_data()
