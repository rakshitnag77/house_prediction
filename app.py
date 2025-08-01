import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(layout="wide")

# Custom background and header styling
st.markdown(
    """
    <style>
    body {
        background-color: #fff9e6;  /* Light yellow */
    }
    .main {
        background-color: #fff9e6;  /* Light yellow */
        padding: 20px;
    }
    h1 {
        text-align: center;
        font-weight: bold;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔷 Bold Title at Top Center
st.markdown("<h1>ALBERTA HOUSE PREDICTION</h1>", unsafe_allow_html=True)

# Load your dataset
df = pd.read_csv(r"C:\Users\B Rakshit Nag\OneDrive\Desktop\WQ HOUSE_PRED\archive\House Price India.csv")

# Streamlit layout: 2 columns (Map | Filters)
col1, col2 = st.columns([3, 1], gap="large")

with col2:
    st.header("🔍 Filters")

    min_price = int(df["Price"].min())
    max_price = 890000
    price_range = st.slider("Price Range (₹)", min_price, max_price, (min_price, max_price))

    bedroom_max = int(df["number of bedrooms"].max())
    bedrooms = st.slider("Max Bedrooms", 1, bedroom_max, 4)

    # Filter dataset
    filtered_df = df[
        (df["Price"] >= price_range[0]) &
        (df["Price"] <= price_range[1]) &
        (df["number of bedrooms"] <= bedrooms)
    ]

with col1:
    st.header("📍 House Price Map")

    fig = px.scatter_mapbox(
        filtered_df,
        lat="Lattitude",
        lon="Longitude",
        color="Price",
        hover_data=["Price"],
        width=700,
        height=700,
        zoom=10
    )
    fig.update_layout(mapbox_style="open-street-map", margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=False)
