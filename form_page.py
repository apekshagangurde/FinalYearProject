import streamlit as st

def show_form():
    

    # Restaurant form fields
    with st.form("restaurant_form"):
        st.header("Enter Restaurant Details")

        # Input fields for restaurant data
        restaurant_name = st.text_input("Restaurant Name")
        latitude = st.number_input("Latitude", format="%f")
        longitude = st.number_input("Longitude", format="%f")
        foot_traffic = st.number_input("Foot Traffic (people/day)", min_value=0, step=1)
        competitors = st.number_input("Number of Competitors Nearby", min_value=0, step=1)
        population_density = st.number_input("Population Density (people/sq km)", min_value=0, step=100)
        projected_revenue = st.number_input("Projected Revenue ($)", min_value=0, step=1000)
        average_meal_price = st.number_input("Average Meal Price ($)", min_value=0, step=5)

        # Form submit button
        submit_button = st.form_submit_button("Submit")

    # Action after form submission
    if submit_button:
        # Show a success message
        st.success(f"Restaurant '{restaurant_name}' has been successfully added!")
        
        # Show entered data (for testing purposes)
        st.write(f"Name: {restaurant_name}")
        st.write(f"Location: ({latitude}, {longitude})")
        st.write(f"Foot Traffic: {foot_traffic}")
        st.write(f"Competitors: {competitors}")
        st.write(f"Population Density: {population_density}")
        st.write(f"Projected Revenue: ${projected_revenue}")
        st.write(f"Average Meal Price: ${average_meal_price}")
