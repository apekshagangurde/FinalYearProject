import streamlit as st
import psycopg2

# Function to establish database connection
def get_db_connection():
    db_info = st.secrets["postgres"]
    return psycopg2.connect(
        host=db_info["host"],       # Accessing the host
        dbname=db_info["database"],  # Accessing the database
        user=db_info["username"],    # Accessing the username
        password=db_info["password"], # Accessing the password
        port=db_info["port"]          # Accessing the port
    )
    

st.write(st.secrets)


# Function to insert preferences into PostgreSQL
def insert_preferences(preferences):
    try:
        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert statement for user table
        insert_query = """
        INSERT INTO "user" (
            preferred_area, 
            preferred_scale, 
            cuisines, 
            restaurant_type, 
            budget_range, 
            ambiance_preferences, 
            dietary_restrictions, 
            looking_for_offers
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute insert statement with data
        cursor.execute(insert_query, (
            preferences['Preferred Area'],
            preferences['Preferred_scale'],
            preferences['Cuisines'],
            preferences['Restaurant Type'],
            preferences['Budget Range'],
            preferences['Ambiance Preferences'],
            preferences['Dietary Restrictions'],
            preferences['Looking for Offers']
        ))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        return True

    except Exception as e:
        st.error(f"Error inserting preferences into database: {e}")
        return False
    if submitted:
    # Prepare the preferences data for insertion
        preferences_data = {
            'Preferred Area': preferred_area,
            'Preferred_scale': preferred_scale,
            'Cuisines': ', '.join(cuisines + [other_cuisine] if other_cuisine else cuisines),
            'Restaurant Type': restaurant_type,
            'Budget Range': f"₹{budget_range[0]} - ₹{budget_range[1]}",
            'Ambiance Preferences': ', '.join(ambiance),
            'Dietary Restrictions': f"Vegetarian: {dietary_restrictions}, Vegan: {vegan_option}, Gluten-Free: {gluten_free}",
            'Looking for Offers': looking_for_offers,
        }

        st.write("Inserting the following preferences:", preferences_data)  # Debug output

        # Insert preferences into PostgreSQL and show a success or failure message
        if insert_preferences(preferences_data):
            st.success("Thank you for providing your preferences!")
        else:
            st.error("Failed to submit your preferences. Please try again.")


def feedback():
    st.header("Please provide your preferences")

    with st.form(key='preferences_form'):
        # Collect preferences from user
        preferred_area = st.selectbox("Select Preferred Location", ["Nashik City", "Dindori", "Trambakeshwar", "Ozar"])
        preferred_scale = st.selectbox("Select Preferred Scale", ["Small", "Medium", "Large"])
        cuisines = st.multiselect("Select Preferred Cuisines", ["Indian", "Chinese", "Italian", "Fast Food", "Continental", "Other"])
        other_cuisine = st.text_input("Specify Other Cuisine (if any)")
        restaurant_type = st.selectbox("Type of Restaurant", ["Fine Dining", "Casual", "Takeaway", "Delivery"])
        budget_range = st.slider("Select Your Budget Range", 0, 2000, (200, 1000))
        ambiance = st.multiselect("Select Ambiance Preferences", ["Family-Friendly", "Romantic", "Outdoor Seating", "Casual"])
        dietary_restrictions = st.checkbox("Vegetarian")
        vegan_option = st.checkbox("Vegan")
        gluten_free = st.checkbox("Gluten-Free")
        looking_for_offers = st.checkbox("Looking for Special Offers or Discounts")

        # Submit button for the form
        submitted = st.form_submit_button("Submit")

        if submitted:
            # Prepare the preferences data for insertion
            preferences_data = {
                'Preferred Area': preferred_area,
                'Preferred_scale': preferred_scale,
                'Cuisines': ', '.join(cuisines + [other_cuisine] if other_cuisine else cuisines),
                'Restaurant Type': restaurant_type,
                'Budget Range': f"₹{budget_range[0]} - ₹{budget_range[1]}",
                'Ambiance Preferences': ', '.join(ambiance),
                'Dietary Restrictions': f"Vegetarian: {dietary_restrictions}, Vegan: {vegan_option}, Gluten-Free: {gluten_free}",
                'Looking for Offers': looking_for_offers,
            }

            # Insert preferences into PostgreSQL and show a success or failure message
            if insert_preferences(preferences_data):
                st.success("Thank you for providing your preferences!")
            else:
                st.error("Failed to submit your preferences. Please try again.")

# Call your feedback function to display it
if __name__ == "__main__":
    feedback()
