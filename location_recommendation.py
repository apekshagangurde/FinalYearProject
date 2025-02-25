import pandas as pd
import folium
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from streamlit_folium import folium_static  # To display map in Streamlit

def recommend_locations():
    # 🔹 Load datasets
    df_restaurants = pd.read_csv("Restaurants data - Sheet1.csv")
    df_population = pd.read_csv("Area Population - Sheet1.csv")

    # 🔹 Standardize Area Names
    df_restaurants["Area Name"] = df_restaurants["Area Name"].str.lower().str.strip()
    df_population["Area Name"] = df_population["Area Name"].str.lower().str.strip()

    # 🔹 Merge datasets
    df = df_population.merge(df_restaurants, on="Area Name", how="left")

    # 🔹 Ensure Population & Income Level are numeric
    df["Population"] = df["Population"].replace(",", "", regex=True).astype(float)
    df["Income Level (Lakhs)"] = pd.to_numeric(df["Income Level (Lakhs)"], errors="coerce").fillna(df["Income Level (Lakhs)"].mean())

    # 🔹 Fill missing competitor count with 0
    df["Competitor_Count"] = pd.to_numeric(df["Competitor_Count"], errors="coerce").fillna(0)

    # 🔹 Create Foot Traffic Score
    df["Foot_Traffic_Score"] = df["Population"] * df["Income Level (Lakhs)"]

    # 🔹 Ensure Latitude & Longitude are numeric
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

    # 🔹 Drop rows where Latitude or Longitude is missing
    df = df.dropna(subset=["Latitude", "Longitude"])

    # 🔹 Aggregate numeric values
    df_final = df.groupby("Area Name").agg({
        "Population": "mean",
        "Income Level (Lakhs)": "mean",
        "Foot_Traffic_Score": "mean",
        "Competitor_Count": "mean",
        "Latitude": "first",
        "Longitude": "first"
    }).reset_index()

    # 🔹 Select Features & Target
    X = df_final[["Population", "Income Level (Lakhs)", "Foot_Traffic_Score"]]
    y = df_final["Competitor_Count"]

    # 🔹 Standardize Features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 🔹 Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 🔹 Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 🔹 Predict Competitor Count
    df_final["Predicted_Competitor_Count"] = model.predict(X_scaled)

    # 🔹 Find Best Locations
    best_locations = df_final[df_final["Predicted_Competitor_Count"] < df_final["Predicted_Competitor_Count"].mean()]
    best_locations = best_locations.sort_values(by="Foot_Traffic_Score", ascending=False).head(5)

    # 🔹 Create Map
    map_center = [best_locations.iloc[0]["Latitude"], best_locations.iloc[0]["Longitude"]]
    m = folium.Map(location=map_center, zoom_start=12)

    # 🔹 Add Markers
    for _, row in best_locations.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"""
            📍 <b>{row['Area Name'].title()}</b><br>
            👥 Population: {int(row['Population'])}<br>
            💰 Income: {row['Income Level (Lakhs)']} Lakhs<br>
            🏢 Predicted Competitors: {round(row['Predicted_Competitor_Count'], 2)}
            """,
            tooltip=row["Area Name"].title(),
            icon=folium.Icon(color="green"),
        ).add_to(m)

    return m  # Return the map object
