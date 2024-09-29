import streamlit as st
import pandas as pd

def feedback():
    # Streamlit Title
    

    # User Feedback Form
    st.header("Please provide your preferences")
    with st.form(key='preferences_form'):
        # Location Preferences
        preferred_area = st.selectbox("Select Preferred Location", ["Nashik City", "Dindori", "Trambakeshwar", "Ozar"])
        #proximity_poi = st.radio("Proximity to Points of Interest", ["Within 1 km", "Within 2 km", "No preference"])

        preferred_scale = st.selectbox("Select Preferred Scale", ["Small", "Medium", "Large"])

        # Cuisine Preferences
        cuisines = st.multiselect("Select Preferred Cuisines", ["Indian", "Chinese", "Italian", "Fast Food", "Continental", "Other"])
        other_cuisine = st.text_input("Specify Other Cuisine (if any)")

        # Restaurant Type
        restaurant_type = st.selectbox("Type of Restaurant", ["Fine Dining", "Casual", "Takeaway", "Delivery"])

        # Budget Range
        budget_range = st.slider("Select Your Budget Range", 0, 2000, (200, 1000))

        # User Ratings
        #min_rating = st.slider("Minimum Average Rating", 1, 5, 3)

        # Ambiance Preferences
        ambiance = st.multiselect("Select Ambiance Preferences", ["Family-Friendly", "Romantic", "Outdoor Seating", "Casual"])

        # Dietary Preferences
        dietary_restrictions = st.checkbox("Vegetarian")
        vegan_option = st.checkbox("Vegan")
        gluten_free = st.checkbox("Gluten-Free")

        # Special Offers
        looking_for_offers = st.checkbox("Looking for Special Offers or Discounts")

        # User Contact Information
        

        submitted = st.form_submit_button("Submit")

        if submitted:
            # Capture preferences in a DataFrame
            preferences_data = {
                'Preferred Area': [preferred_area],
                'Preferred_scale': [preferred_scale],

                #'Proximity to POI': [proximity_poi],
                'Cuisines': [', '.join(cuisines + [other_cuisine] if other_cuisine else cuisines)],
                'Restaurant Type': [restaurant_type],
                'Budget Range': [f"₹{budget_range[0]} - ₹{budget_range[1]}"],
                #'Min Rating': [min_rating],
                'Ambiance Preferences': [', '.join(ambiance)],
                'Dietary Restrictions': [f"Vegetarian: {dietary_restrictions}, Vegan: {vegan_option}, Gluten-Free: {gluten_free}"],
                'Looking for Offers': [looking_for_offers],
                
            }
            
            preferences_df = pd.DataFrame(preferences_data)

            # Save preferences to a CSV file
            preferences_df.to_csv('data/user_preferences.csv', mode='a', header=False, index=False)

            st.success("Thank you for providing your preferences!")
